# Validación · Candela v1

## Comprobado

- Compilación de producción de React con Vite y recursos locales.
- Montaje en DOM sin errores capturados. No es una prueba visual de navegador.
- Diecisiete capítulos y sus controles; navegación directa, índice y avance entre focos.
- Vista general independiente y acercamiento del primer símbolo del flujograma.
- Zoom de lectura conservado al cambiar de capítulo y subtema; ajuste explícito a 100 %.
- Ficha real en NV sin puntaje; ejercicio separado. Pesos suman 100.
- Todos los criterios críticos bloquean aprobación cuando son parciales, incumplidos o no verificados.
- Dieciséis combinaciones de la barrera de liberación: únicamente las cuatro condiciones completas habilitan.
- Indicador correcto y N/A sin liberaciones; rechazo de valores incoherentes.
- Flujograma con decisiones Sí/No, rutas de retención diferenciadas, responsables y registros. Stock recibe autorización únicamente desde Calidad.
- Recursos HTML, imágenes y fuentes locales presentes en la publicación.
- Imágenes de chocolate excluidas del producto del caso. Procedencia fotográfica no atribuida a Candela.

## Límite de esta ejecución

No está disponible la herramienta admitida de revisión visual de navegador en este entorno. No se ha certificado visualmente el encuadre por resolución, la pantalla completa, las transiciones reales ni los gestos táctiles. La adaptación responsive está implementada y la lógica se probó en DOM. La revisión visual del usuario permitirá detectar ajustes de composición en su pantalla.

## Comandos

`npm run build`, `npm run check`, `node tests/ui.test.mjs` desde el proyecto fuente.

## Comprobaciones de la revisión A–D

- Orden: estudio de caso y cadena, matriz completa, A, B, C, D, conclusiones y fuentes.
- Sin etiquetas de bloques A–D ni numeración de cláusulas en los capítulos iniciales de desarrollo del caso.
- Cinco preguntas de porqués con sus cinco respuestas visibles y seis ramas de Ishikawa con dos causas concretas por rama.
- Cláusulas respaldadas por el PDF ISO proporcionado: 4.1, 4.2, 4.4, 6.1, 6.2, 8.1, 8.4–8.7, 9.1, 10.2 y 10.3. Aplicaciones al caso separadas del resumen normativo.
- Selección interactiva de cláusulas actualiza etapas relacionadas y permite abrir la misma cadena de procesos.

## Ajuste final de presentación

- Calculadora retirada; indicador estático compacto con fórmula, meta, responsable y frecuencia.
- Sin avisos destacados de estudio académico ni referencias a archivos proporcionados por el usuario en el contenido proyectado.
- Referencias externas y notas breves de fuentes conservadas. La redacción mantiene la diferencia entre escenario, hipótesis y propuesta sin agregar banners.

## Revisión 4: índice literal y distribución del explorador ISO
- 22 títulos (apartados y subapartados) cotejados con el índice de la traducción oficial ISO 9001:2015. Títulos entre comillas angulares; las aplicaciones mantienen redacción propia.
- Matriz con acceso directo al apartado seleccionado, selector lateral persistente y traza de ocho etapas numeradas con recorrido de ida y vuelta.
- Retirada definitiva de la ficha visual del indicador mensual. Se mantiene la explicación de seguimiento del bloque D.
- Párrafo de introducción de la matriz centrado.
- En pantallas bajas se eliminan introducciones repetidas para liberar altura, sin reducir el texto explicativo. En móvil el selector se mantiene como banda horizontal desplazable.
- Verificación visual real en navegador de los bloques A y C, incluidos los títulos largos 4.2 y 8.4, a 1363 × 936 y zoom de lectura 100 %. Selector, cadena y detalle principal visibles simultáneamente. No equivale a comprobar todas las resoluciones ni todos los niveles de zoom.
- Pruebas DOM de selección de los 13 apartados, resaltado de etapas, acceso directo de la matriz, zoom persistente y retirada del indicador, junto con compilación de producción y reglas del proceso.
