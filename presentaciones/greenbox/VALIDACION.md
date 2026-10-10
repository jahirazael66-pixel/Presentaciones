# Validación — recorrido vertical Greenbox

Iteración del 10 octubre 2026. Alcance: únicamente `presentaciones/greenbox/`; otras presentaciones y lobby se conservan.

## Verificaciones en Chromium / Playwright
- 15 capítulos y 53 estados en escritorio 1440×960: sin errores JavaScript, solicitudes fallidas ni desbordamientos horizontales detectados.
- Los mismos 53 estados en 1024×768, 390×844 y 844×390: 159 estados adicionales sin desbordamientos de títulos, párrafos, imágenes, pestañas o gráficos detectados.
- Selección por pestañas y SVG, flechas anterior/siguiente, navegación con teclado, índice completo y detección del capítulo al desplazar la página.
- Cadena, agricultores y ambiente: vista general independiente, primer acercamiento y siguientes, retorno simultáneo de cámara, texto y pestaña.
- Circular: categorías 3/2/4/4 sincronizadas con la explicación.
- Matriz de Valor: los 13 stakeholders seleccionables; filtros 5 internos, 8 externos, 7 primarios y 6 secundarios; selección y restablecimiento.
- Evidencia de estándares: ocho filas seleccionables, acercamiento por fila y retorno general.
- Zoom por botones y Alt + rueda; rueda normal desplaza la página. Arrastre después del acercamiento comprobado.
- Movimiento activado, repetición, persistencia tras recargar y enlace directo al estado elegido.
- Índice en los tres tamaños; los controles superiores no cubren el contenido centrado.
- Revisión de capturas: portada, productos, cadena, agricultores, ambiente, ODS, ISO, circular, dispersión y certificaciones. Corregidos recorte de fotografía agrícola, superposición de pestañas y ubicación de controles.

Estas comprobaciones no constituyen una auditoría de accesibilidad ni garantizan todos los dispositivos y navegadores. La valoración estética sigue correspondiendo al usuario.

## Rigor
No se añadieron cifras o certificados para justificar nuevos gráficos. La matriz sigue siendo cualitativa; el circular cuenta grupos. Se mantienen fuentes, interpretaciones y límites de certificaciones. Fotografías ilustrativas aportadas se distinguen de imágenes documentales NESsT.

## Publicación
Cambios limitados a Greenbox, basados en el último árbol del repositorio y actualización de rama con comprobación del commit esperado. La entrega se verifica contra GitHub Pages tras completar el despliegue.
