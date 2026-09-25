// Browser-independent smoke tests of the exact JavaScript shipped in the generated catalog.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const root=path.join(__dirname,'..');
const html=fs.readFileSync(path.join(root,'index.html'),'utf8');
const code=html.split('<script>')[1].split('</script>')[0];
const els={};
for(const id of ['q','year','tag','status','sort','code','match','selectedTopics','quickFilters','total','published','withcode','topiccount','count','grid','downloadCsv','downloadBib','reset']){
 els[id]={value:'',innerHTML:'',textContent:'',disabled:false,events:{},addEventListener(k,fn){this.events[k]=fn;},insertAdjacentHTML(){},focus(){},setAttribute(){}};
}
els.sort.value='recent';els.match.value='all';
const context=vm.createContext({URLSearchParams,URL,Blob,setTimeout,console,
 document:{getElementById:id=>els[id],querySelectorAll:()=>[],addEventListener(){},activeElement:{tagName:'BODY'}},
 location:{pathname:'/',search:'?tag=Perturbation&tag=Multimodal',hash:'',protocol:'https:'},
 history:{replaceState(){}},window:{addEventListener(){},scrollTo(){}}});
vm.runInContext(code,context,{timeout:5000});
const evaluate=expr=>vm.runInContext(expr,context);
assert.equal(evaluate('PAPERS.length'),275);
assert(evaluate('selected.has("Perturbation")&&selected.has("Multimodal")'));
assert(evaluate('filteredRows().every(p=>p.tags.includes("Perturbation")&&p.tags.includes("Multimodal"))'));
const andCount=evaluate('filteredRows().length');assert(andCount>0);
els.match.value='any';assert(evaluate('filteredRows().length')>=andCount);
els.reset.events.click();assert.equal(evaluate('filteredRows().length'),275);
els.q.value='Multimodal Perturbation';assert(evaluate('filteredRows().length')>0);
assert(evaluate('filteredRows().every(p=>[p.title,p.label,p.venue,...p.tags].join(" ").toLowerCase().includes("perturbation"))'));
els.q.value='';els.code.value='documented';assert(evaluate('filteredRows().every(p=>documented(p))'));
assert(!evaluate('filteredRows().some(p=>p.id==="biom-jepa")'));
els.code.value='missing';assert(evaluate('filteredRows().every(p=>!p.code_url)'));
els.reset.events.click();els.q.value='nothing-that-matches-0000';evaluate('render()');assert(els.downloadCsv.disabled);
els.reset.events.click();
assert(evaluate('filteredCsv(filteredRows()).includes("code_status")'));
assert.equal(evaluate('(filteredBib(filteredRows()).match(/^@/gm)||[]).length'),275);
assert.equal(evaluate('link("bad","javascript:alert(1)")'),'');
for(const f of ['docs/index.html','docs/catalog.html'])assert.equal(fs.readFileSync(path.join(root,f),'utf8'),html);
console.log('Catalog JS smoke tests passed: AND/OR topics, URLs, text search, code filters, reset, empty state, exports, generated parity.');
