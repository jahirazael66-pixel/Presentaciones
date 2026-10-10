# Greenbox — recorrido vertical interactivo

Presentación académica de 15 capítulos y 53 estados de explicación. El contenido se recorre con desplazamiento vertical normal; los controles de exposición permiten avanzar subtema por subtema. Se conservan los temas, fuentes, imágenes y cinco gráficos de la versión anterior.

## Abrir
https://jahirazael66-pixel.github.io/Presentaciones/presentaciones/greenbox/?v=vertical1

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
