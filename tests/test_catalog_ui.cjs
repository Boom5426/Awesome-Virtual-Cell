// Browser-independent smoke tests of the exact JavaScript shipped in the generated catalog.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const root=path.join(__dirname,'..');
const html=fs.readFileSync(path.join(root,'index.html'),'utf8');
const expectedCount=JSON.parse(fs.readFileSync(path.join(root,'data','papers.json'),'utf8')).paper_count;
const code=html.split('<script>')[1].split('</script>')[0];
const els={};
for(const id of ['q','year','tag','status','sort','code','match','task','modality','perturbationType','generalization','paperType','selectedTopics','quickFilters','total','published','withcode','topiccount','count','grid','downloadCsv','downloadBib','reset']){
 els[id]={value:'',innerHTML:'',textContent:'',disabled:false,events:{},addEventListener(k,fn){this.events[k]=fn;},insertAdjacentHTML(){},focus(){},setAttribute(){}};
}
els.sort.value='recent';els.match.value='all';
const context=vm.createContext({URLSearchParams,URL,Blob,setTimeout,console,
 document:{getElementById:id=>els[id],querySelectorAll:()=>[],addEventListener(){},activeElement:{tagName:'BODY'}},
 location:{pathname:'/',search:'?tag=Perturbation&tag=Multimodal',hash:'',protocol:'https:'},
 history:{replaceState(){}},window:{addEventListener(){},scrollTo(){}}});
vm.runInContext(code,context,{timeout:5000});
const evaluate=expr=>vm.runInContext(expr,context);
assert.equal(evaluate('PAPERS.length'),expectedCount);
assert(evaluate('selected.has("Perturbation")&&selected.has("Multimodal")'));
assert(evaluate('filteredRows().every(p=>p.tags.includes("Perturbation")&&p.tags.includes("Multimodal"))'));
const andCount=evaluate('filteredRows().length');assert(andCount>0);
els.match.value='any';assert(evaluate('filteredRows().length')>=andCount);
els.reset.events.click();assert.equal(evaluate('filteredRows().length'),expectedCount);
els.task.value='Intervention Design';assert(evaluate('filteredRows().length')>0);assert(evaluate('filteredRows().every(p=>(p.facets.task||[]).includes("Intervention Design"))'));els.task.value='';
els.generalization.value='Cross-Species';assert(evaluate('filteredRows().length')>0);assert(evaluate('filteredRows().every(p=>(p.facets.generalization||[]).includes("Cross-Species"))'));els.generalization.value='';
els.q.value='Multimodal Perturbation';assert(evaluate('filteredRows().length')>0);
assert(evaluate('filteredRows().every(p=>[p.title,p.label,p.venue,...p.tags].join(" ").toLowerCase().includes("perturbation"))'));
els.q.value='';els.code.value='documented';assert(evaluate('filteredRows().every(p=>documented(p))'));
assert(!evaluate('filteredRows().some(p=>p.id==="biom-jepa")'));
els.code.value='missing';assert(evaluate('filteredRows().every(p=>!p.code_url)'));
els.reset.events.click();els.q.value='nothing-that-matches-0000';evaluate('render()');assert(els.downloadCsv.disabled);
els.reset.events.click();
assert(evaluate('filteredCsv(filteredRows()).includes("code_status")'));assert(evaluate('filteredCsv(filteredRows()).includes("facet_review_basis")'));
assert.equal(evaluate('(filteredBib(filteredRows()).match(/^@/gm)||[]).length'),expectedCount);
assert.equal(evaluate('link("bad","javascript:alert(1)")'),'');
for(const f of ['docs/index.html','docs/catalog.html'])assert.equal(fs.readFileSync(path.join(root,f),'utf8'),html);
// Code-link audit regressions: status semantics and observed omissions.
els.reset.events.click();els.code.value='linked';
for(const id of ['nudge-cell-fate','regformer','spamosaic','coladan'])assert(evaluate('filteredRows().some(p=>p.id==='+JSON.stringify(id)+')'));
for(const id of ['pertreason','holocell','biom-jepa','scvision'])assert(!evaluate('filteredRows().some(p=>p.id==='+JSON.stringify(id)+')'));
for(const status of ['data_only','release_pending','not_found','related_only']){
 const synthetic=JSON.stringify({code_url:'https://github.com/example/resource',code_status:status});
 assert.equal(evaluate('hasCode('+synthetic+')'),false);
 assert.equal(evaluate('documented('+synthetic+')'),false);
}
assert(evaluate('hasCode({code_url:"https://github.com/example/code",code_status:"repository_linked"})'));
assert(!evaluate('documented({code_url:"https://github.com/example/code",code_status:"project_match"})'));
els.code.value='missing';assert(evaluate('filteredRows().some(p=>p.id==="pertreason")'));
assert(evaluate('PAPERS.find(p=>p.id==="pertreason").links.some(l=>l.label==="dataset")'));
els.reset.events.click();
console.log('Catalog JS smoke tests passed: AND/OR topics, URLs, text search, code filters, reset, empty state, exports, generated parity.');
