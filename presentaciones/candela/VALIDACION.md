# Validación · Candela v1

## Comprobado

- Compilación de producción de React con Vite y recursos locales.
- Montaje en DOM sin errores capturados. No es una prueba visual de navegador.
- Catorce capítulos y sus controles; navegación directa, índice y avance entre focos.
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
