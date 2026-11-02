export const money=(n,d=0)=>new Intl.NumberFormat('es-PE',{style:'currency',currency:'USD',maximumFractionDigits:d,minimumFractionDigits:d}).format(n);
export function economics(price=8,cost=6.4,quantity=20000){const sales=price*quantity,variable=cost*quantity,contribution=sales-variable;return{sales,variable,contribution,margin:sales?contribution/sales:0};}
export function balance(fresh=1000){return{fresh,product:fresh*.1,main:fresh*.09,offcuts:fresh*.01,organic:fresh*.45,compost:fresh*.36,pending:fresh*.09,water:fresh*.45,valorization:80};}
export function cargo(lots=1){return{kg:5000*lots,boxes:500*lots,pallets:10*lots,boxVolume:15*lots,palletVolume:16.8*lots,height:1.4};}
export const visibleActor=(a,types,relations)=>(!types.length||types.includes(a.type))&&(!relations.length||relations.includes(a.relation));
export const fitScale=(height,space)=>Math.min(1,Math.max(.1,space/Math.max(1,height)));

export function coverageKg(price,cost=6.4,additional=10000){const unit=Math.round((price-cost)*100)/100;return unit>0?Math.ceil(additional/unit-1e-9):null;}

// Matriz 2x2: solo niveles Bajo y Alto.
export function stakeholderStrategy(a){
 if(!['Bajo','Alto'].includes(a.power)||!['Bajo','Alto'].includes(a.interest))throw Error('Nivel de stakeholder no válido');
 return a.power==='Alto'?(a.interest==='Alto'?'Administrar de cerca':'Mantener satisfechos'):(a.interest==='Alto'?'Mantener informados':'Monitorear');
}
export function matrixPosition(a,all){
 const matrixStrategy=stakeholderStrategy(a),group=all.filter(b=>stakeholderStrategy(b)===matrixStrategy),index=group.findIndex(b=>b.id===a.id),center=a.interest==='Alto'?75:25;
 return{matrixStrategy,x:group.length===1?center:center-16+index*32/(group.length-1),y:a.power==='Alto'?68:22};
}
