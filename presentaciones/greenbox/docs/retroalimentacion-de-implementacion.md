# Retroalimentación de implementación — reforma visual Greenbox

## Objetivo
Mejorar efectividad, rapidez y calidad en futuras presentaciones mediante decisiones observables y pruebas reproducibles. Esta documentación registra el proceso y sus resultados; no afirma que exista memoria permanente del modelo.

## Decisiones reutilizables
1. **Separar contenido de puesta en escena.** Recuperar textos, notas y referencias de la versión publicada antes de modificar la composición. Mantener los datos de stakeholders en un archivo independiente permite transformar la red en matriz sin cambiar sus grupos.
2. **Diseñar por relación.** Una cadena pide recorrido; una relación social pide intercambios; certificaciones piden familias y evidencia; una matriz pide ejes, clasificación y razones. No partir siempre del mismo conjunto de tarjetas.
3. **Una navegación, un estado.** El número de fragmentos visibles determina el subtema activo. Pestañas, flechas, regreso y enlaces del índice usan ese mismo estado.
4. **Cancelar antes de animar otra escena.** Revertir el contexto GSAP evita acumulación de estilos y secuencias que continúen fuera de pantalla. Comprobar también cambios rápidos y retroceso.
5. **Elección de movimiento explícita.** El movimiento reducido define el estado inicial, pero el botón puede activarlo y guarda la elección local. La versión anterior demostró que un bloqueo incondicional del sistema impedía el control manual.
6. **No depender de servicios externos en la exposición.** Fuentes, SVG y bibliotecas se guardan junto al HTML. Versionar URLs CSS/JS evita servir una mezcla de archivos nuevos y anteriores en caché.
7. **Verificar el entorno al inicio.** Un archivo local o paquete de una sesión anterior no garantiza que sus dependencias ni el navegador temporal continúen disponibles. En esta ejecución se reinstaló BeautifulSoup y se recuperó Chromium con descompresión directa, evitando un problema de extracción de permisos.
8. **Licencias y procedencia junto a los recursos.** Registrar familias tipográficas y versión de GSAP. No usar fotos de procedencia desconocida para representar la empresa.

## Revisión de calidad
Las capturas y resultados del recorrido se guardan durante la revisión. Los resultados finales de navegación, límites de texto y preferencias de animación se resumen en VALIDACION.md al completar las pruebas. Corregir hallazgos antes de publicar; evitar registrar como exitoso algo aún no probado.

## Hallazgos de la revisión final
- La activación automática de la vista de desplazamiento de Reveal.js en pantallas estrechas cambiaba la escena al redimensionar. Se desactivó `scrollActivationWidth` para conservar el modo de exposición.
- Etiquetas de stakeholders más completas requerían seis píxeles adicionales en las agrupaciones. Se aumentó el espacio de los cuadrantes y se volvió a comprobar el ajuste interno.
- La prueba de repetición debe esperar un primer fotograma antes de medir actividad: un tween recién creado aún puede no figurar como activo antes del render.

## Mejora siguiente
Recoger la valoración del usuario después de exponer. Medir qué transiciones ayudan a comprender y cuáles distraen, si el tamaño de texto funciona proyectado y si las escenas permiten entender el material sin narración adicional. Ajustar el estándar a esa retroalimentación, sin confundir una prueba funcional con aprobación estética.
