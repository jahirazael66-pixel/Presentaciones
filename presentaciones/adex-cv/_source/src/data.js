export const slides=[
{title:'Revisión de CV con IA',chapter:'Contexto del problema',speaker:'María Fernanda',time:'00–02 min',theme:'cover'},
{title:'Revisión y registro manual',chapter:'Contexto del problema',speaker:'María Fernanda',time:'00–02 min',theme:'problem'},
{title:'El proceso automatizado',chapter:'Solución propuesta',speaker:'Miguel',time:'02–05 min',theme:'flow'},
{title:'Sistema y revisión humana',chapter:'Solución propuesta',speaker:'Miguel',time:'02–05 min',theme:'roles'},
{title:'Demostración en vivo',chapter:'Puesta en marcha',speaker:'Jahir',time:'05–09 min',theme:'demo'},
{title:'Tiempo, costo y capacidad',chapter:'Comparación de resultados',speaker:'Jostin',time:'09–11 min',theme:'comparison'},
{title:'Resultados y siguientes pasos',chapter:'Comparación de resultados',speaker:'Jostin',time:'09–11 min',theme:'results'},
{title:'Referencias y evidencia',chapter:'Consulta',speaker:'Equipo',time:'Respaldo',theme:'references'}];
export const team=['Maria Fernanda Ruiz Luna','Jahir Azael Castillo Paucas','Miguel Peralta Llontop','Jostin Alexander Chavez Estela'];
export const links={form:'https://docs.google.com/forms/d/e/1FAIpQLScT8o5Z7pdbROeTS73ZMBhrA1GA0dCDYHz17GZwUMJDhfrGbw/viewform',sheet:'https://docs.google.com/spreadsheets/d/1oVh6cfAQzYTXScPoIbC0EUou_gNIEtUdqWL44LXDXFg/edit?gid=202#gid=202'};
export const flow=[
{title:'Google Forms',short:'Recibe la postulación',detail:'Nombre, correo, vacante y PDF de la plantilla. El formulario admite un archivo de hasta 1 MB.',owner:'Postulante',icon:'form'},
{title:'Google Drive',short:'Conserva el PDF',detail:'El documento original se guarda como fuente para comprobar los datos y revisar cualquier diferencia.',owner:'Cuenta del piloto',icon:'drive'},
{title:'Make',short:'Extrae y valida el texto',detail:'La ejecución por evento comprueba marcador, etiquetas, orden y campos; cruza nombre, correo y vacante con Forms.',owner:'Reglas de validación',icon:'make'},
{title:'¿Plantilla válida?',short:'Decisión documental',detail:'Una estructura incorrecta se registra en Rechazados y recibe un motivo. El documento puede corregirse y volver a enviarse.',owner:'Reglas previas a GPT',icon:'decision'},
{title:'GPT-5 nano',short:'Organiza la evidencia',detail:'Prepara información sobre estudios, Excel, mercados, comercio exterior, informes, inglés y disponibilidad. Las fuentes se copian sin IA.',owner:'Asistente de análisis',icon:'ai'},
{title:'Google Sheets',short:'Registra la ficha',detail:'Admitidos reúne las fichas. Rechazados conserva nombre, correo, motivo, código, enlace y fecha del envío.',owner:'Registro trazable',icon:'sheet'},
{title:'Recursos Humanos',short:'Verifica y decide',detail:'Compara la ficha con el PDF y evalúa requisitos y competencias. El sistema no contrata ni descarta personas por su cuenta.',owner:'Responsabilidad humana',icon:'human'}];
export const trials=[{name:'Sofía · con plantilla',state:'Admitido',seconds:59.47,credits:10.14},{name:'Diego · con plantilla',state:'Admitido',seconds:57.03,credits:10.36},{name:'Sofía · sin marcador',state:'Rechazado sin GPT',seconds:5.01,credits:6},{name:'Sofía · reenvío final',state:'Admitido',seconds:69.36,credits:10.66}];
export const sources=[['Informe inicial del proyecto','Diagnóstico y diseño conceptual · 22/10/2026'],['Informe final del equipo','Pruebas, costos, supuestos y KPIs · 03/11/2026'],['Google · Activadores instalables','https://developers.google.com/apps-script/guides/triggers/installable'],['Make · Créditos','https://help.make.com/credits'],['Make · Precios','https://www.make.com/en/pricing']];
