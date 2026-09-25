#!/usr/bin/env python3
"""Read-only identifier resolution and repository evidence enrichment."""
import base64, concurrent.futures, json, re, urllib.parse
from pathlib import Path
import collect_curation_evidence as c
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'curation-evidence'
def field(v): return v.get('value','') if isinstance(v,dict) else v

def enrich(pair):
    p,r=pair
    r['enrichment']=[]
    urls=[u for u in [p.get('paper_url'),p.get('preprint_url')] if u]
    doi=p.get('doi')
    for u in urls:
        m=re.search(r'nature.com/articles/([^/?#]+)',u)
        if not doi and m: doi='10.1038/'+m.group(1)
        m=re.search(r'(10\.(?:1101|64898)/\d{4}\.\d{2}\.\d{2}\.\d+)',u)
        if not doi and m: doi=m.group(1)
    if doi and not r['abstract']:
        endpoint='https://api.crossref.org/works/'+urllib.parse.quote(doi,safe='/')
        data,res=c.get_json(endpoint)
        value=data.get('message') or {}
        if isinstance(value,dict) and value.get('title'):
            r['sources'].append({'url':endpoint,'title':value['title'][0],'kind':'publisher_metadata'})
            r['abstract']=c.plain(value.get('abstract',''))
            r['authors']=value.get('author',[])
        r['enrichment'].append({'url':endpoint,'status':res['status']})
        if not r['abstract'] and doi.startswith(('10.1101/','10.64898/')):
            endpoint='https://api.biorxiv.org/details/biorxiv/'+doi
            data,res=c.get_json(endpoint)
            values=data.get('collection') or []
            if values:
                value=values[-1]
                r['abstract']=c.plain(value.get('abstract',''))
                r['sources'].append({'url':endpoint,'title':value.get('title'),'kind':'preprint_metadata'})
        if not r['abstract']:
            endpoint='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':'DOI:'+doi,'resultType':'core','format':'json'})
            data,res=c.get_json(endpoint)
            values=data.get('resultList',{}).get('result') or []
            if values:
                value=values[0]
                r['abstract']=c.plain(value.get('abstractText',''))
                r['sources'].append({'url':endpoint,'title':value.get('title'),'kind':'indexed_abstract'})
            r['enrichment'].append({'url':endpoint,'status':res['status']})
    for u in urls:
        if 'arxiv.org/pdf/' in u and not r['abstract']:
            target=u.replace('/pdf/','/abs/').removesuffix('.pdf')
            res=c.request(target)
            m=re.search(r'<blockquote[^>]*>(.*?)</blockquote>',res['text'],re.S|re.I)
            if m:
                r['abstract']=c.plain(m.group(1))
                r['sources'].append({'url':target,'title':p['title'],'kind':'paper_page'})
        if 'openreview.net/forum' in u and not r['abstract']:
            pid=urllib.parse.parse_qs(urllib.parse.urlparse(u).query).get('id',[''])[0]
            for host in ('api2.openreview.net','api.openreview.net'):
                endpoint='https://'+host+'/notes?id='+urllib.parse.quote(pid)
                data,res=c.get_json(endpoint)
                notes=data.get('notes') or []
                if notes:
                    content=notes[0].get('content',{})
                    r['abstract']=c.plain(field(content.get('abstract','')))
                    r['sources'].append({'url':endpoint,'title':field(content.get('title','')),'kind':'conference_metadata'})
                    r['openreview_content']=content
                    break
    rep=r.get('repository',{})
    if p.get('code_url') and not(rep.get('exact_identifiers') or rep.get('exact_title')):
        name=c.repo_root(rep.get('canonical_url') or p['code_url'])
        if name:
            endpoint='https://api.github.com/repos/'+name+'/readme'
            data,res=c.get_json(endpoint,True)
            if data.get('encoding')=='base64':
                r['repository_readme']=base64.b64decode(data.get('content','')).decode('utf-8',errors='replace')
                r['repository_readme_url']=data.get('html_url') or endpoint
    text=r['abstract']+' '+json.dumps(r.get('openreview_content',{}))
    for m in re.finditer(r'https?://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',text):
        url=m.group(0).rstrip('.,;')
        if not any(x['url']==url for x in r['code_candidates']):
            x={'url':url,'source':r['sources'][-1]['url'] if r['sources'] else '', 'context':text[max(0,m.start()-120):m.end()+100]}
            if not p.get('code_url'): x['repository']=c.repo_evidence(url,p)
            r['code_candidates'].append(x)
    return r

def main():
    ps=json.loads((ROOT/'data/papers.json').read_text())['papers']
    rs=json.loads((OUT/'evidence.json').read_text())
    assert [p['id'] for p in ps]==[r['id'] for r in rs]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        rows=list(pool.map(enrich,zip(ps,rs)))
    (OUT/'evidence-enriched.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'papers':len(rows),'abstracts':sum(bool(r['abstract']) for r in rows),'missing':[r['id'] for r in rows if not r['abstract']]},ensure_ascii=False))
if __name__=='__main__': main()
