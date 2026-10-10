# Greenbox — presentación visual narrativa

Presentación HTML de 15 escenas para exposición académica. Conserva la información de la versión anterior y reorganiza su desarrollo mediante diagramas, ilustraciones SVG, texto integrado y secuencias de movimiento.

## Abrir
https://jahirazael66-pixel.github.io/Presentaciones/presentaciones/greenbox/

También se puede servir esta carpeta con `python -m http.server 8000` y abrir `http://localhost:8000`. No requiere proceso de compilación, cuenta adicional ni extensiones del navegador para exponer.

## Navegar
- Flechas del teclado o del menú: avanzar y retroceder por subtemas y escenas.
- Encabezados de sección: saltar a empresa, cadena de valor, responsabilidad social, certificaciones, stakeholders o cierre.
- Subtemas: elegir el foco actual.
- Índice: seleccionar cualquiera de las 15 escenas.
- Repetir: volver a ejecutar la secuencia del punto actual.
- Animación: activar o desactivar; la elección se conserva en este navegador cuando el almacenamiento local está disponible.
- Pantalla completa y notas del expositor: controles auxiliares.
- En teléfonos, usar orientación horizontal para mejorar la lectura. La presentación conserva el modo diapositivas al redimensionar.

## Diseño y recursos
DM Sans para contenido y navegación; DM Serif Display para contraste editorial. Verde del logo, blanco, crema, verde oscuro y tonos suaves. Fuentes, logo, ilustraciones y bibliotecas necesarias se sirven desde el proyecto.

Reveal.js mantiene la navegación por escenas y subtemas. GSAP 3.15.0, MotionPath, DrawSVG y MorphSVG coordinan recorridos, dibujo de conexiones y transformación de ilustraciones. Los cinco gráficos son SVG locales: barras de empleo, circular de grupos, dispersión cualitativa de stakeholders, flujo de cadena de valor y matriz de evidencia de estándares. `learning.js` controla selección, filtros y cámaras; `learning.css` define jerarquía y acentos. No se requieren nuevas bibliotecas ni servicios externos. Los recursos de versiones anteriores se conservan pero no son dependencias de la nueva página.

## Contenido y rigor
No se investigaron ni agregaron nuevos datos empresariales en esta reforma. Las referencias y límites se conservan: datos documentados, declaraciones empresariales e inferencias. La vigencia de certificaciones sigue sin comprobarse. Los 13 stakeholders y sus posiciones en la matriz son los de la versión publicada anterior. Primario/secundario no equivale a influencia/interés.

El contenido esencial no abre globos ni ventanas emergentes. Índice y notas son utilidades independientes de la explicación. Las fuentes siguen accesibles mediante enlaces.

## Documentación reutilizable
- `docs/estandar-visual-en-desarrollo.md`: preferencias expresas y criterios de futuras presentaciones.
- `docs/retroalimentacion-de-implementacion.md`: decisiones, dificultades y mejoras observadas.
- `VALIDACION.md`: resumen de verificaciones.

El estándar visual sigue sujeto a la evaluación estética del usuario. Las pruebas funcionales no sustituyen esa aprobación.

## Explorar los gráficos
- Cadena de valor: elegir una etapa o subtema, acercar con +/−, arrastrar al acercarse y volver con «Vista completa».
- Empleo: seleccionar una barra o «Comparar». Son 40 y 240 trabajadores en dos momentos reportados; +200 y +500% son cálculos derivados, no nuevos datos de campo.
- Stakeholders: seleccionar un sector circular y un grupo. El gráfico cuenta 5 internos primarios, 4 externos primarios y 4 externos secundarios.
- Matriz de Valor: filtrar internos/externos y primarios/secundarios, seleccionar un cuadrante o punto, acercar, desplazar y regresar. La separación entre puntos no representa puntuaciones.
- Certificaciones: seleccionar una fila para leer propósito, respaldo y límite de verificación. No se afirma vigencia de certificados sin evidencia.

Todos los elementos seleccionables admiten Tab y Enter o espacio. El zoom tiene botones y rueda; el desplazamiento admite arrastre con ratón o puntero táctil. Las explicaciones permanecen en pantalla, separadas del área móvil del gráfico.
