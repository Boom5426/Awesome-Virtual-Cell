#!/usr/bin/env python3
"""Read-only, source-linked audit of every catalog paper and existing code URL.

This collects evidence, not automatic topic assignments or publication upgrades.
No catalog files are modified. HTTP failures are explicitly recorded.
"""
from __future__ import annotations
import base64
import concurrent.futures
import difflib
import html
import json
import os
import re
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'curation-evidence'
UA = 'Awesome-Virtual-Cell-Curation/1.0 (+https://github.com/Boom5426/Awesome-Virtual-Cell)'
LOCK = threading.Lock()
CACHE: dict[str, dict] = {}


def norm(text):
    return re.sub(r'[^a-z0-9]+', ' ', str(text).lower()).strip()


def plain(text):
    text = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', str(text), flags=re.S | re.I)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', text))).strip()


def request(url, github=False):
    key = str(url)
    with LOCK:
        cached = CACHE.get(key)
    if cached is not None:
        return cached
    headers = {'User-Agent': UA, 'Accept': 'application/json' if github else '*/*'}
    if github and os.getenv('GH_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
    record = {'url': url, 'status': None, 'final_url': url, 'text': ''}
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=14) as response:
                record.update(status=response.status, final_url=response.url,
                              text=response.read(3500000).decode('utf-8', errors='replace'))
            break
        except urllib.error.HTTPError as exc:
            record['status'] = exc.code
            record['error'] = str(exc)
            if exc.code not in (429, 502, 503, 504):
                break
        except Exception as exc:
            record['error'] = type(exc).__name__ + ': ' + str(exc)
        if attempt == 0:
            time.sleep(1)
    with LOCK:
        CACHE[key] = record
    return record


def get_json(url, github=False):
    result = request(url, github)
    try:
        return json.loads(result['text']), result
    except (ValueError, TypeError):
        return {}, result


def source_doi(url):
    match = re.search(r'(10\.\d{4,9}/[^\s?#]+)', url or '')
    return re.sub(r'v\d+(?:\.full)?$', '', match.group(1)).rstrip(').,') if match else None


def repo_root(url):
    match = re.match(r'https?://github\.com/([^/]+/[^/#?]+)', url or '', re.I)
    return match.group(1).removesuffix('.git') if match else None


def repo_evidence(url, paper):
    name = repo_root(url)
    if not name:
        return {'url': url, 'status': 'non_github_link'}
    meta, response = get_json('https://api.github.com/repos/' + name, True)
    result = {'url': url, 'http_status': response['status'], 'exists': response['status'] == 200}
    if response['status'] != 200:
        return result
    result.update(canonical_url=meta.get('html_url'), fork=meta.get('fork'),
                  archived=meta.get('archived'), description=meta.get('description'))
    readme, rr = get_json('https://api.github.com/repos/' + meta.get('full_name', name) + '/readme', True)
    text = ''
    if readme.get('encoding') == 'base64':
        text = base64.b64decode(readme.get('content', '')).decode('utf-8', errors='replace')
    result['readme_status'] = rr['status']
    dois = {source_doi(paper.get(k)) for k in ('paper_url', 'preprint_url')}
    if paper.get('doi'):
        dois.add(paper['doi'])
    dois.discard(None)
    exact_ids = [value for value in dois if value.lower() in text.lower()]
    arxiv_ids = re.findall(r'arxiv\.org/(?:abs|html)/(\d{4}\.\d{4,5})',
                           (paper.get('paper_url') or '') + ' ' + (paper.get('preprint_url') or ''))
    exact_ids += [value for value in arxiv_ids if value in text]
    title_in_readme = norm(paper['title']) in norm(text)
    result.update(exact_identifiers=exact_ids, exact_title=title_in_readme)
    relevant = [line.strip() for line in text.splitlines()
                if any(value.lower() in line.lower() for value in exact_ids)
                or (paper.get('label') and paper['label'].lower() in line.lower())]
    result['readme_evidence'] = plain(' '.join(relevant[:6]))[:900]
    path = urllib.parse.urlparse(url).path.strip('/').split('/')
    if len(path) > 2 and path[2] in ('tree', 'blob'):
        checked = request(url)
        result['subpath_status'] = checked['status']
    return result


def audit(item):
    index, paper = item
    row = {'index': index, 'id': paper['id'], 'title': paper['title'],
           'old_tags': paper.get('tags', []), 'code_url': paper.get('code_url'),
           'sources': [], 'abstract': '', 'code_candidates': [], 'checks': []}
    doi = paper.get('doi') or source_doi(paper.get('paper_url')) or source_doi(paper.get('preprint_url'))
    # Exact-identifier metadata before any title-based inference.
    urls = [u for u in (paper.get('paper_url'), paper.get('preprint_url')) if u]
    if doi and (doi.startswith('10.1101/') or doi.startswith('10.64898/')):
        server = 'medrxiv' if any('medrxiv' in u for u in urls) else 'biorxiv'
        api = 'https://api.biorxiv.org/details/' + server + '/' + doi
        data, r = get_json(api)
        row['checks'].append({'url': api, 'status': r['status']})
        items = data.get('collection') or []
        if items:
            value = items[-1]
            row['sources'].append({'url': api, 'title': value.get('title'), 'kind': 'preprint_metadata'})
            row['abstract'] = plain(value.get('abstract', ''))
            if value.get('jatsxml'):
                urls.insert(0, value['jatsxml'])
    elif doi:
        api = 'https://api.crossref.org/works/' + urllib.parse.quote(doi, safe='/')
        data, r = get_json(api)
        row['checks'].append({'url': api, 'status': r['status']})
        value = data.get('message', {})
        if isinstance(value, dict) and value.get('title'):
            row['sources'].append({'url': api, 'title': value['title'][0], 'kind': 'publisher_metadata'})
            row['abstract'] = plain(value.get('abstract', ''))
    # Inspect actual paper pages for code availability, not just repository name matches.
    for url in list(dict.fromkeys(urls))[:3]:
        r = request(url)
        row['checks'].append({'url': url, 'status': r['status'], 'final_url': r['final_url']})
        if r['status'] != 200 or r['text'].startswith('%PDF'):
            continue
        text = r['text']
        title = re.search(r'<meta[^>]*(?:name|property)=["\'](?:citation_title|og:title)["\'][^>]*content=["\']([^"\']+)', text, re.I)
        row['sources'].append({'url': r['final_url'], 'title': html.unescape(title.group(1)) if title else None,
                               'kind': 'paper_page'})
        if not row['abstract']:
            abstract = re.search(r'<(?:abstract|blockquote)[^>]*>(.*?)</(?:abstract|blockquote)>', text, re.S | re.I)
            if not abstract:
                abstract = re.search(r'<meta[^>]*(?:name|property)=["\'](?:description|og:description|DC.Description)["\'][^>]*content=["\']([^"\']+)', text, re.I)
            if abstract:
                row['abstract'] = plain(abstract.group(1))
        for match in re.finditer(r'https?://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:/[^\s<>"\']*)?', html.unescape(text)):
            link = match.group(0).rstrip(').,;')
            context = plain(text[max(0, match.start()-280):match.end()+220])[:500]
            if repo_root(link):
                row['code_candidates'].append({'url': link, 'source': r['final_url'], 'context': context})
    if not row['abstract'] and doi:
        api = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode(
            {'query': 'DOI:' + doi, 'resultType': 'core', 'format': 'json'})
        data, r = get_json(api)
        row['checks'].append({'url': api, 'status': r['status']})
        results = data.get('resultList', {}).get('result') or []
        if results:
            value = results[0]
            row['abstract'] = plain(value.get('abstractText', ''))
            row['sources'].append({'url': api, 'title': value.get('title'), 'kind': 'indexed_abstract'})
    if paper.get('code_url'):
        row['repository'] = repo_evidence(paper['code_url'], paper)
    # Deduplicate links without replacing or asserting that any are official.
    distinct = {}
    for candidate in row['code_candidates']:
        distinct.setdefault(candidate['url'], candidate)
    row['code_candidates'] = list(distinct.values())
    if not paper.get('code_url'):
        candidates = row['code_candidates']
        for candidate in candidates[:4]:
            candidate['repository'] = repo_evidence(candidate['url'], paper)
    return row


def main():
    papers = json.loads((ROOT/'data/papers.json').read_text(encoding='utf-8'))['papers']
    OUT.mkdir(exist_ok=True)
    rows = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for row in pool.map(audit, enumerate(papers)):
            rows.append(row)
            compact = dict(row)
            compact['abstract'] = compact['abstract'][:2100]
            print('PAPER_AUDIT ' + json.dumps(compact, ensure_ascii=False), flush=True)
    (OUT/'evidence.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
    summary = {'papers': len(rows), 'abstracts_retrieved': sum(bool(r['abstract']) for r in rows),
               'existing_code_links': sum(bool(r['code_url']) for r in rows),
               'existing_repos_reachable': sum(r.get('repository', {}).get('exists', False) for r in rows)}
    print('AUDIT_SUMMARY ' + json.dumps(summary), flush=True)

if __name__ == '__main__':
    main()
