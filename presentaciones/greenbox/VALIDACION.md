# Validación ejecutada

Pruebas realizadas el 9 de octubre de 2026 en Chromium sin interfaz mediante Playwright, abriendo `index.html` como archivo local.

- 15 diapositivas detectadas.
- Sin errores JavaScript registrados ni solicitudes fallidas de recursos.
- Referencias locales del HTML existentes; tipografías y bibliotecas incluidas.
- Navegación anterior/siguiente y navegación mediante flecha derecha comprobadas.
- Cadena de valor: primera etapa revelada al avanzar; etapas restantes implementadas como fragmentos Reveal.js.
- Índice: selección de una diapositiva y cierre comprobados.
- Notas: contenido correspondiente a la diapositiva y cierre con Escape comprobados.
- Certificaciones: apertura y cierre de ficha comprobados.
- Filtros de matriz: Todos 13; internos primarios 5; internos secundarios 0; externos primarios 4; externos secundarios 4.
- Selección de NESsT y actualización de relación/justificación comprobadas.
- Gráfico laboral ECharts renderizado como SVG.
- Preferencia de movimiento reducido: transición configurada en `none`.
- Vista móvil de 390 × 844: ancho del documento igual al ancho de la ventana, sin desbordamiento horizontal.
- Las 15 diapositivas medidas a 1440 × 900: el contenido principal no invade el pie de fuentes. Se revisaron capturas de portada, identidad, agricultores, trabajadores, ambiente, certificaciones, ISO, matriz, relaciones, conclusiones y fuentes.
- Sintaxis de los tres archivos JavaScript comprobada con `node --check`.

Alcance: no se probó un despliegue real de GitHub Pages, otros navegadores ni la apertura de cada enlace externo. Las fichas con contenido extenso permiten desplazamiento interno. La vista móvil conserva el formato de exposición 16:9, por lo que conviene usar orientación horizontal. La función de pantalla completa está implementada con la API del navegador y ofrece F11 como alternativa si el navegador la bloquea.
