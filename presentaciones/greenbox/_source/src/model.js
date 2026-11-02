export const money=(n,d=0)=>new Intl.NumberFormat('es-PE',{style:'currency',currency:'USD',maximumFractionDigits:d,minimumFractionDigits:d}).format(n);
export function economics(price=8,cost=6.4,quantity=20000){const sales=price*quantity,variable=cost*quantity,contribution=sales-variable;return{sales,variable,contribution,margin:sales?contribution/sales:0};}
export function balance(fresh=1000){return{fresh,product:fresh*.1,main:fresh*.09,offcuts:fresh*.01,organic:fresh*.45,compost:fresh*.36,pending:fresh*.09,water:fresh*.45,valorization:80};}
export function cargo(lots=1){return{kg:5000*lots,boxes:500*lots,pallets:10*lots,boxVolume:15*lots,palletVolume:16.8*lots,height:1.4};}
export const visibleActor=(a,types,relations)=>(!types.length||types.includes(a.type))&&(!relations.length||relations.includes(a.relation));
export const fitScale=(height,space)=>Math.min(1,Math.max(.1,space/Math.max(1,height)));

export function coverageKg(price,cost=6.4,additional=10000){const unit=Math.round((price-cost)*100)/100;return unit>0?Math.ceil(additional/unit-1e-9):null;}
