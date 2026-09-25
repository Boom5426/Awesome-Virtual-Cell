#!/usr/bin/env python3
"""Apply an exact, checked curation package locally; upload Git blobs, never move refs."""
from __future__ import annotations
import argparse,base64,collections,concurrent.futures,hashlib,json,lzma,os,subprocess,urllib.request
from pathlib import Path

def run(*args):
    subprocess.run(args,check=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--package',required=True);ap.add_argument('--evidence',required=True);ap.add_argument('--upload',action='store_true');a=ap.parse_args()
    package=json.loads(lzma.decompress(base64.b64decode(Path(a.package).read_text())))
    original=Path('data/papers.json').read_bytes()
    assert hashlib.sha256(original).hexdigest()==package['catalog_base_sha256'],'Catalog changed; rebuild/review the patch before applying.'
    data=json.loads(original);old=json.loads(original)['papers'];evidence=json.loads(Path(a.evidence).read_text())
    ops=package['operations'];papers=data['papers']
    assert [p['id'] for p in papers]==[p['id'] for p in ops]==[p['id'] for p in evidence]
    receipts=[]
    for before,p,op,ev in zip(old,papers,ops,evidence):
        p.update(op['set'])
        sources=list(dict.fromkeys(x['url'] for x in ev['sources'] if x.get('url')))
        if ev.get('repository_readme_url'):sources.append(ev['repository_readme_url'])
        sources=list(dict.fromkeys(sources))
        if not sources and (before.get('paper_url') or before.get('preprint_url')):sources=[before.get('paper_url') or before.get('preprint_url')]
        receipts.append({'id':p['id'],'reviewed_at':'2026-09-26','old_tags':before['tags'],'tags':p['tags'],'tag_basis':p['tag_review_basis'],
                        'tag_rationale':op['rationale'],'sources':sources,'old_code_url':before['code_url'],'code_url':p['code_url'],
                        'code_status':p['code_status'],'code_sources':p['code_sources'],'code_note':op['code_note'],
                        'repository_http_status':ev.get('repository',{}).get('http_status'),
                        'repository_readme_status':ev.get('repository',{}).get('readme_status')})
    for name,text in package['files'].items():
        path=Path(name);assert not path.is_absolute() and '..' not in path.parts
        path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding='utf-8')
    Path('data/papers.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    path=Path('data/curation/2026-09-26.json');path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps({'review_date':'2026-09-26','scope':'All 275 Research Papers records; source access and association checks, not executable reproduction.','records':receipts},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    # Apply only the hand-written README rearrangement; rebuild its generated block using Python.
    md=Path('README.md').read_text();start='<!-- GENERATED:RESEARCH-PAPERS:START -->';end='<!-- GENERATED:RESEARCH-PAPERS:END -->'
    i=md.index(start);j=md.index(end)
    Path('README.md').write_text(md[:i]+'__RESEARCH_PLACEHOLDER__\n'+md[j+len(end):])
    subprocess.run(['git','apply','--whitespace=nowarn','-'],input=package['readme_patch'],text=True,check=True)
    md=Path('README.md').read_text().replace('__RESEARCH_PLACEHOLDER__\n',start+'\n\n'+end)
    Path('README.md').write_text(md)
    # Human-readable receipt contains only original summaries, no copied abstracts.
    count=collections.Counter(x['code_status'] for x in receipts);basis=collections.Counter(x['tag_basis'] for x in receipts)
    text=f'''# Catalog curation — 2026-09-26\n\nReviewed **{len(receipts)} Research Papers records**. All {len(papers)} records are preserved. Changed topic assignments for {sum(a['tags']!=b['tags'] for a,b in zip(old,papers))} records; {sum(len(p['tags'])>1 for p in papers)} records now have more than one tag.\n\nThis is a source/metadata and repository-correspondence audit, not a full-text systematic review or an execution/reproduction audit. Evidence basis: {basis['abstract']} abstracts, {basis['project_documentation']} project documents, {basis['title_and_metadata']} provisional title/metadata classifications.\n\nCode correspondence: {dict(count)}. The five added implementation links are Scouter, PRnet, scDrugMap, PertDiff and MultiTME. DrugReflector now links to the authors' repository while retaining its software archive; TamGen follows the old official repository's explicit maintainer redirect. BioM-JEPA's unrelated/unsupported code slot was removed, and scLDM.CD4 is a related resource for the Context Not Scale position paper, not a verified implementation of that paper.\n\nAll decisions and source URLs are in [the machine-readable receipt](../data/curation/2026-09-26.json). Repository access errors and missing code are not interpreted as proof of absence.\n\n| Paper | Tags | Tag evidence | Code correspondence |\n| --- | --- | --- | --- |\n'''
    for p,r in zip(papers,receipts):
        url=p.get('paper_url') or p.get('preprint_url') or '#';label=(p.get('label') or p['title']).replace('|',' / ')
        text+=f"| [{label}]({url}) | {', '.join(p['tags'])} | {r['tag_basis']} | {r['code_status']} |\n"
    Path('docs/curation-2026-09-26.md').write_text(text,encoding='utf-8')
    run('python','scripts/validate_catalog.py');run('python','scripts/build_readme.py');run('python','scripts/build_catalog.py');run('python','scripts/build_exports.py')
    run('python','-m','unittest','discover','-s','tests','-v');run('node','tests/test_catalog_ui.cjs');run('python','scripts/build_readme.py','--check')
    for name,expected in package['expected'].items():
        actual=hashlib.sha256(Path(name).read_bytes()).hexdigest()
        assert actual==expected,f'Output mismatch {name}: {actual} != {expected}'
    print('ALL_OUTPUT_HASHES_VERIFIED',len(package['expected']),flush=True)
    if not a.upload:return
    # Creates unreachable Git blobs only; the authenticated connector moves main after review.
    token=os.environ['GH_TOKEN'];repo=os.environ['GITHUB_REPOSITORY']
    def upload(name):
        body=json.dumps({'content':Path(name).read_text(encoding='utf-8'),'encoding':'utf-8'}).encode()
        req=urllib.request.Request('https://api.github.com/repos/'+repo+'/git/blobs',data=body,method='POST',headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','User-Agent':'Awesome-Virtual-Cell-Curation','Content-Type':'application/json'})
        with urllib.request.urlopen(req,timeout=60) as res: sha=json.load(res)['sha']
        return {'path':name,'mode':'100644','type':'blob','sha':sha}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:elements=list(pool.map(upload,package['expected']))
    out=Path('verified-curation-build');out.mkdir(exist_ok=True)
    (out/'tree-elements.json').write_text(json.dumps({'base_commit':os.environ['GITHUB_SHA'],'tree_elements':elements,'output_sha256':package['expected']},indent=2)+'\n')
    print('BLOBS_UPLOADED_NO_REF_MOVED',len(elements),flush=True)

if __name__=='__main__':main()
