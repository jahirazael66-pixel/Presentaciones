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

## Corrección de encuadre y contenido proyectado
- 15 capítulos y 51 estados: ISO pasa de tres estados a un único proyecto documentado.
- 153 estados completos comprobados al avanzar con el botón real en 1366×768, 1440×900 y 1024×768. Títulos, textos, imágenes, controles de subtemas, gráficos, notas y fuentes quedan dentro del área visible bajo el encabezado; sin fallas detectadas.
- 150 transiciones inversas con el botón anterior: alineación final comprobada.
- Transición suave de 0,7 segundos a un capítulo lejano y avance de subtema: mantiene el destino seleccionado y llega al margen correcto.
- Teclado izquierda/derecha funciona también con foco en los botones de navegación. Entrada y salida de pantalla completa comprobadas.
- Móvil 390×844: conserva lectura vertical y no presenta desbordamiento horizontal en el capítulo comprobado.
- Recorrido completo de contenido visible: retirados avisos de verificación pendiente. Citas y pies de gráficos conservados. ISO no afirma obtención de un certificado.
- Sin errores JavaScript durante estas pruebas.

## Circular horizontal y matriz con filtros combinables
- Las 16 combinaciones posibles de los cuatro filtros se comprobaron contra los 13 grupos. Resultados por categoría: internos primarios 3, internos secundarios 2, externos primarios 4, externos secundarios 4; primarios 7, secundarios 6.
- Selección y deselección mediante botones reales; estados aria-pressed, persistencia entre cuadrantes y flechas, retorno de cámara y limpieza con Todos: comprobados.
- Los 14 estados de agricultores, circular y matriz en 1366×768, 1440×900 y 1024×768: encuadre completo sin desbordamientos detectados.
- Circular: cuatro botones de leyenda seleccionables y sincronizados con explicación. Foto de agricultores retirada del capítulo.
- Móvil 390×844 y 844×390: capítulos afectados sin desbordamiento horizontal; filtros externos + secundarios muestran cuatro grupos.
- Sin errores JavaScript durante estas pruebas; revisión visual de capturas del circular y agricultores.

## Zoom de lectura visible
- +/−, deslizador 100–200% con pasos de 5, porcentaje y texto accesible: comprobados.
- El tamaño real de una cabecera aumenta proporcionalmente; la transición presenta escala intermedia y llega a 180% tras 0,42 segundos.
- Arrastre en párrafo desplaza la vista; Ajustar y Escape vuelven a 100%. Teclado del deslizador comprobado.
- Avanzar de subtema restablece el encuadre completo. Los filtros siguen operativos y el ajuste automático no reduce el zoom elegido.
- 153 estados en 1366×768, 1440×900 y 1024×768 al tamaño normal, sin cortes o desbordamientos detectados.
- Móvil 390×844 y 844×390: control dentro de pantalla, ampliación y retorno operativos; sin desbordamiento horizontal del documento.
- Sin errores JavaScript; revisión visual de vista normal y ampliada.

## Corrección: mantener zoom al navegar
La regla anterior de restablecer automáticamente al avanzar queda sustituida. Se conserva el nivel de zoom al cambiar capítulo o subtema, avanzar animaciones, retroceder y redimensionar. Comprobadas 14 flechas consecutivas, saltos de capítulo, pestañas, transición suave, tamaños de escritorio y móvil; 150% permanece aplicado al contenido y al indicador. Ajustar y Escape vuelven a 100%. Sin errores JavaScript en estas pruebas.
