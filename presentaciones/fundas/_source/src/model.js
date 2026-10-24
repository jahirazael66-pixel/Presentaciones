export const months=[0,0,60,60,120,120,120,180,180,180,180,240];
export const cash=[3058.6,2067.2,1659.2,1251.2,1426.6,1602,1777.4,2536.2,3295,4053.8,4812.6,6154.8];
export const delayed=cash.map((v,i)=>v-months[i]*14);
export const money=(n,d=0)=>new Intl.NumberFormat('es-PE',{style:'currency',currency:'USD',maximumFractionDigits:d,minimumFractionDigits:d}).format(n);
export function result(q=1440,p=28,c=13.5,f=950){let revenue=q*p,variable=q*(c+40/60+.05*p),contribution=revenue-variable,pretax=contribution-f*12-400-1750;return{revenue,variable,contribution,pretax,net:pretax>0?pretax*.9:pretax};}
export function landed(freight=300,origin=true,retail=78){let tariff=origin?.125:.188,cost=28*(1+tariff)+(freight+70)/60;return{cost,margin:(retail-cost)/retail,limit:60*(retail*.5-28*(1+tariff))-70};}
export function npv(recovery=true,rate=.2){let flows=recovery?[-7000,6068.6,5893.6,9943.6]:[-7000,2072.6,1897.6,5947.6];return{flows,value:flows.reduce((s,v,i)=>s+v/(1+rate)**i,0)};}
export const titles=['Fundas textiles peruanas','Resumen ejecutivo','Oportunidad de negocio','Producto y ficha técnica','Propuesta de valor','Tendencias y comprador','Mercado y competencia','Validación y demanda','Modelo de negocio','Plan comercial','Cadena de producción','Exportación y costo de llegada','Organización y plan de 90 días','Costos y contribución','Capital y flujo de caja','Resultado y punto de equilibrio','Escenarios y sensibilidad','Riesgos y condiciones de avance','Conclusiones','Referencias'];
