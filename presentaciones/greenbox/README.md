# Greenbox — recorrido vertical interactivo

Presentación académica de 15 capítulos y 51 estados de explicación. El contenido se recorre con desplazamiento vertical normal; los controles de exposición permiten avanzar subtema por subtema. Se conservan los temas, fuentes, imágenes y cinco gráficos de la versión anterior.

## Abrir
https://jahirazael66-pixel.github.io/Presentaciones/presentaciones/greenbox/?v=horizontal1

Puede abrirse directamente o servirse con `python -m http.server 8000`. No requiere compilación, cuenta, conexión a fuentes tipográficas externas ni extensiones.

## Navegar y exponer
- Desplazar la página con ratón, rueda o gesto táctil; el índice lateral indica el capítulo actual.
- Encabezados, índice lateral e índice de Opciones: saltar a un capítulo.
- Flechas anterior/siguiente, izquierda/derecha y PageUp/PageDown: recorrer subtemas y capítulos. Las flechas arriba/abajo conservan el desplazamiento normal.
- Pestañas y elementos del gráfico: elegir un foco directamente.
- Vista completa: restaurar cámara, explicación y estado general. Cada aspecto, incluido el primero, tiene un acercamiento independiente.
- Opciones: índice, animación, repetición, pantalla completa, notas y retorno al lobby.
- Animación: respeta inicialmente la preferencia de movimiento reducido del sistema. Una elección explícita permanece en el navegador cuando el almacenamiento local está disponible.
- En móvil, la página se apila para lectura vertical; también admite orientación horizontal.

## Explorar gráficos
Cinco SVG locales: flujo de cadena de valor, barras de empleo, circular de grupos, dispersión de stakeholders y matriz de evidencia de estándares. Agricultores y ambiente añaden diagramas con perspectivas.

Usar +/− para acercar. Arrastrar después del acercamiento para desplazar; Alt + rueda permite zoom en escritorio. La rueda normal sigue desplazando la página. Los elementos seleccionables admiten Tab y Enter o espacio. Las explicaciones permanecen fuera del área móvil del gráfico y no abren globos.

## Diseño y recursos
DM Sans y DM Serif Display, fuentes locales. Paleta verde, crema y menta con acentos de terracota, azul y ámbar. Cada capítulo tiene composición propia: portada fotográfica, galería de productos, panorama de cadena, cifras protagonistas, bandas ODS, mapa de relaciones y síntesis tipográfica. La información de empresa aparece una vez en su capítulo.

`journey.css` y `journey.js` definen el recorrido nativo; `learning.js` controla gráficos y cámaras; `stakeholders.js` conserva la clasificación y referencias. GSAP local coordina animación. Reveal.js, plugins adicionales, ECharts y estilos anteriores se conservan como recursos de versiones previas, pero la página actual no los carga.

## Contenido y límites
Se mantienen datos documentados, declaraciones empresariales e inferencias señaladas. Las cifras de empleo 40 y 240 corresponden a momentos reportados, no a una serie anual actual. +200 y +500% son cálculos derivados. El circular cuenta grupos (3/2/4/4), no personas ni peso económico. La dispersión es cualitativa alto/bajo y no atribuye puntuaciones.

Los 13 stakeholders siguen disponibles. Administración/finanzas y RR. HH. se distinguen como internos secundarios en la adaptación funcional de Info.txt, con el límite explicado en `docs/revision-de-contenido-y-stakeholders.md`: Clarkson considera primarios a los empleados. Primario/secundario no equivale a influencia/interés.

Las menciones y logos de estándares no prueban certificación vigente. Las fotografías aportadas y documentales conservan sus créditos y límites en `CREDITS.md`.

## Documentación
- `VALIDACION.md`: verificaciones funcionales y visuales.
- `docs/estandar-visual-en-desarrollo.md`: preferencias expresas, aún en calibración.
- `docs/retroalimentacion-de-implementacion.md`: aprendizajes de implementación.

La reforma solo afecta `presentaciones/greenbox/`; conserva el lobby y las demás presentaciones.

## Encuadre de exposición
En escritorio, cada capítulo se ajusta al espacio disponible bajo el encabezado. Flechas, índice y pestañas alinean la sección completa con una transición de 0,7 segundos cuando las animaciones están activadas. El encuadre se recalcula tras cambiar subtema, tamaño de ventana, fuentes o imágenes. La rueda y los gestos conservan el recorrido vertical normal; en móvil se mantiene lectura natural sin reducir todo a una pantalla.

ISO contiene un solo estado dedicado al proyecto de gestión ambiental documentado en 2021. Se retiraron del contenido proyectado las aclaraciones de verificación pendiente, manteniendo citas, pies de gráficos y documentación para la explicación oral. No se convierte una mención o un proyecto en afirmación de certificado obtenido.

## Gráficos y filtros combinables
El circular de stakeholders se presenta junto a la explicación en escritorio, con leyenda seleccionable de tamaño legible. En móvil se apila. Se retiró la fotografía de agricultores para priorizar las perspectivas del diagrama.

En la Matriz de Valor, los filtros se combinan en dos dimensiones: ubicación (internos/externos) y tipo (primarios/secundarios). Dentro de una dimensión se suman las opciones; entre dimensiones se cruzan. Ejemplos: internos + primarios = 3 grupos; internos + secundarios = 2; externos + primarios = 4; externos + secundarios = 4. Seleccionar ambos tipos muestra primarios y secundarios, limitado por la ubicación si está seleccionada. Una dimensión sin selección incluye todas sus opciones.

Cada botón permite seleccionar y deseleccionar. La combinación permanece al avanzar por cuadrantes y restablecer cámara; Todos limpia los filtros. El indicador muestra las opciones y el total de grupos visibles.

## Zoom de lectura directo
El control flotante Zoom permanece visible en el lateral derecho, separado de Opciones. +/− cambian en 10 puntos; el deslizador gradúa entre 100% y 200% en pasos de 5. El porcentaje es relativo al encuadre completo del capítulo. Ajustar o Escape vuelven a 100%.

Con zoom activo, arrastrar texto o fondo mueve la vista ampliada; enlaces, botones y gráficos mantienen su propia interacción. El zoom usa transición de 0,42 segundos con movimiento activo. El nivel de zoom se conserva al cambiar capítulo, subtema o tamaño de ventana; solo se restablece mediante Ajustar o Escape. Se conserva el zoom de cámaras de gráficos, que funciona independientemente.

Los pies, fuentes y aclaraciones de gráficos tienen un tamaño base ligeramente mayor. El ajuste automático de encuadre mide el diseño antes de su transformación para no anular el zoom elegido.

## Comparación en paralelo
Empleo y Matriz de Valor colocan gráfico y explicación en columnas en escritorio, con párrafos más grandes y sin apilar todo en el centro. El subtema Mujeres también sitúa ilustración y texto en paralelo. En móvil se conserva lectura vertical. La cadena mantiene su vista panorámica; el zoom elegido continúa al navegar.
