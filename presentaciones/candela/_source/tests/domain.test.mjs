import assert from 'node:assert/strict';
import{criteria,evaluateSupplier,indicator,canRelease,flowNodes,flowEdges,tourIds,chapters,stepCounts}from'../src/domain.js';
assert.equal(criteria.reduce((s,c)=>s+c[1],0),100);
assert.equal(evaluateSupplier(criteria.map(()=>null)).score,null);
assert.equal(evaluateSupplier(criteria.map(()=>2)).status,'Aprobar');
for(let i=0;i<criteria.length;i++)if(criteria[i][2])for(const v of [0,1,null]){const s=criteria.map(()=>2);s[i]=v;assert.notEqual(evaluateSupplier(s).status,'Aprobar');}
assert.equal(indicator(0,0),'N/A');assert.equal(indicator(9,10),90);assert.equal(indicator(11,10),null);assert.equal(indicator(-1,10),null);assert.equal(indicator(1.2,10),null);
for(let n=0;n<16;n++){const keys=['evidence','b1','total','signature'];const c=Object.fromEntries(keys.map((k,i)=>[k,!!(n&(1<<i))]));assert.equal(canRelease(c),n===15);}
assert.equal(new Set(flowNodes.map(n=>n.id)).size,flowNodes.length);
for(const [a,b]of flowEdges){assert.ok(flowNodes.some(n=>n.id===a));assert.ok(flowNodes.some(n=>n.id===b));}
assert.equal(new Set(tourIds).size,flowNodes.length);assert.equal(stepCounts.cadena,tourIds.length+2);
for(const n of flowNodes)assert.ok(n.who&&n.input&&n.action&&n.record&&n.result);
const outgoing=id=>flowEdges.filter(e=>e[0]===id);
for(const n of flowNodes.filter(n=>n.type==='decision'))assert.deepEqual(outgoing(n.id).map(e=>e[2]).sort(),['No','Sí']);
assert.ok(!outgoing('missing').some(e=>e[1]==='stock'));assert.ok(!outgoing('bad').some(e=>e[1]==='stock'));assert.deepEqual(flowEdges.filter(e=>e[1]==='stock').map(e=>e[0]),['sign']);
assert.equal(chapters.length,17);console.log('OK: reglas críticas, 16 combinaciones de liberación, indicador, pesos, decisiones y rutas del flujograma.');
const {isoBlocks,whyQuestions,causeDetails}=await import('../src/iso-data.js');
for(const b of Object.values(isoBlocks))for(const c of b.clauses){assert.ok(c.summary&&c.application&&c.evidence&&c.stage);for(const f of c.focus)assert.ok(flowNodes.some(n=>n.id===f));assert.ok(c.legal.length>0);}
assert.equal(whyQuestions.length,5);assert.equal(causeDetails.length,6);console.log('OK: ISO trazable a etapas reales del flujograma, síntesis y aplicación separadas, cinco preguntas y seis ramas.');
