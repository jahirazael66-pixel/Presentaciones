export const ec3Chapters=[
 ['eco-carton','Cartón exterior: declaración Tipo II'],['eco-organico','Logotipo ecológico de la UE'],
 ['riesgo-contexto','Contexto del próximo embarque'],['riesgo-proceso','Riesgos a lo largo del proceso'],
 ['riesgo-criterios','Criterios comunes de evaluación'],['riesgo-matriz','Matriz de riesgos del pedido'],
 ['riesgo-mapa','Mapa de calor y prioridad'],['riesgo-control','Cómo evitar la liberación prematura']
];
export const ec3Sources=[
 ['R14','ISO 14021:2026','Autodeclaraciones ambientales de producto o envase','https://www.iso.org/standard/14021'],
 ['R15','Reglamento (UE) 2025/40','Envases y declaraciones ambientales, artículo 14','https://eur-lex.europa.eu/eli/reg/2025/40/oj'],
 ['R16','Comisión Europea · Logotipo ecológico','Condiciones de uso y datos junto al sello','https://agriculture.ec.europa.eu/farming/organic-farming/organic-logo_en'],
 ['R17','Comisión Europea · Comercio orgánico','Importación, certificado de inspección y TRACES','https://agriculture.ec.europa.eu/farming/organic-farming/trade_en'],
 ['R18','BÖLW · Mercado bio alemán','Ventas de alimentos y bebidas bio en 2025','https://www.boelw.de/themen/zahlen-fakten/handel/artikel/umsatz-absatz-importe-2026/']
];
export const probability=[
 ['Raro','Solo sería esperable en circunstancias excepcionales.'],
 ['Improbable','Puede ocurrir, pero existe una revisión previa que lo reduce.'],
 ['Posible','Hay condiciones o puntos de transferencia que permiten el evento.'],
 ['Probable','El escenario deja abierta una vía directa para que ocurra.'],
 ['Casi seguro','Es esperable en este embarque si no se corrige la condición presente.']
];
export const impact=[
 ['Insignificante','Ajuste interno sin afectar conformidad, cantidad ni entrega.'],
 ['Menor','Reproceso acotado que no compromete el pedido.'],
 ['Moderado','Demora recuperable o costo adicional sin reemplazar el lote.'],
 ['Mayor','Rechazo parcial, reposición o compromiso de la fecha pactada.'],
 ['Crítico','Rechazo total, riesgo grave para la salud o interrupción del envío.']
];
export function riskLevel(score){return score<=4?'Bajo':score<=10?'Medio':score<=15?'Alto':'Crítico';}
export const riskData=[
 ['R1','Liberación','Liberación sin evidencia del lote','Se acepta un certificado genérico.','Se habilita el stock sin evidencia propia.','Un lote no conforme podría llegar al despacho.',4,5,'El escenario permite habilitar sin barrera obligatoria.','Si el lote escapa al bloqueo final, puede salir producto no apto.','sign','lock'],
 ['R2','Acopio','Aflatoxinas fuera de límite','Secado o conservación deficientes.','Las aflatoxinas superan el máximo.','Bloqueo y posible sustitución del lote.',3,5,'La exposición a humedad es una condición plausible.','El lote completo puede quedar fuera del pedido.',null,'drop'],
 ['R3','Muestreo','Evidencia analítica no válida','Plan o identificación deficientes.','La muestra no representa el lote o el informe no se vincula con él.','Se invalida la evidencia y se repite el análisis.',3,4,'Hay transferencias entre almacén y laboratorio.','Repetir el análisis puede comprometer la fecha pactada.','sample','lab'],
 ['R4','Etiquetado','Omisión del alérgeno','Se utiliza un arte sin validar para Alemania.','La etiqueta omite la identificación del alérgeno.','Riesgo grave para el consumidor alérgico.',2,5,'Se supone una revisión previa del arte.','La omisión puede afectar gravemente a un consumidor alérgico.',null,'tag'],
 ['R5','Transporte','Deterioro de parte de la carga','Sellado deficiente o exposición a humedad.','Parte del producto se deteriora durante el traslado.','Rechazo parcial o reposición.',3,4,'No se ha verificado la protección en la ruta del escenario.','Puede perderse parte del pedido.',null,'truck'],
 ['R6','Documentación','Inconsistencia del código de lote','Varios responsables preparan registros sin un cotejo final.','Los códigos difieren entre producto, informe y expediente.','Observación del importador y demora recuperable.',3,3,'Varios responsables preparan los documentos.','Se supone que el error se corrige sin sustituir el lote.',null,'file']
].map(([id,stage,title,cause,event,effect,p,i,whyP,whyI,node,icon])=>({id,stage,title,cause,event,effect,p,i,whyP,whyI,node,icon,score:p*i,level:riskLevel(p*i)}));
