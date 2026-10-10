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

## Iteración de foco visual y exploración — 10 octubre 2026
**Retroalimentación recibida:** la tipografía, paleta y animaciones anteriores fueron valoradas positivamente; la presentación aún repetía composiciones y no dirigía suficientemente la atención. Se pidió aprender sin depender del discurso y explorar cinco gráficos.

**Respuesta de diseño:** se conservan los quince temas. El empleo compara dos momentos con base cero; el circular cuenta los trece grupos; la dispersión usa niveles cualitativos; la cadena conecta etapas con actores; la matriz separa propósito y respaldo de estándares. Todas tienen explicación y conclusión dentro de la escena. Los títulos laterales y una escena oscura aportan variación sin cambiar las familias tipográficas.

**Lecciones observadas:**
- Una prueba que revisa solo párrafos y títulos puede omitir leyendas SVG. Revisar también la caja del gráfico, leyenda, conclusión y pie.
- Los SVG con alto al 100% pueden expandir una fila de CSS Grid por tamaño intrínseco. Usar una fila `minmax(0,1fr)`, hijos con `min-height:0` y SVG anclado a su contenedor.
- Las etiquetas de puntos necesitan espacio dentro de cada cuadrante; no basta con ubicar bien el centro del círculo.
- Mantener fuentes y límites al seleccionar un elemento evita que una exploración aparente más certeza que la documentación.
- Reutilizar SVG y bibliotecas locales existentes evita instalar nuevas dependencias para una interacción que el navegador ya resuelve.
- La cámara mueve solo el gráfico: controles, explicación y conclusión conservan posición y legibilidad. El modo sin animaciones también permite filtrar, seleccionar, acercar y regresar.

Esta bitácora describe decisiones y comprobaciones del proyecto; no implica reentrenamiento ni memoria permanente del modelo.

## Revisión de precisión y perspectiva
La cadena de valor fue validada por el usuario como referencia de atención focalizada. Se extendió la cámara a agricultores, ambiente y filas de estándares, manteniendo otras composiciones.

La revisión detectó una diferencia entre el marco clásico de Clarkson y la adaptación funcional ya explícita en Info.txt. La versión anterior había eliminado internos secundarios sin conservar aquella adaptación. Se restauran administración/finanzas y RR. HH. como soporte en el criterio del documento, con su límite teórico visible. El CFO documentado permite distinguir función secundaria e influencia alta estimada.

Para mejorar rapidez y rigor: leer primero el criterio del documento base; registrar hecho, inferencia y clasificación por separado; calcular filtros y gráficos desde una única fuente de datos; probar todos los miembros al modificar textos, no solo la vista general. Consultar las FAQ actuales evitó tratar Bio Suisse y JAS como menciones únicamente históricas; HACCP permanece sin revalidación actual.


## Edición fotográfica

- Inspeccionar transparencia real, no interpretar el fondo negro de una previsualización como píxeles negros.
- Conservar texto y geometría de marcas; adaptar el soporte visual en CSS/SVG.
- Separar la vista general del primer foco, con estados de navegación explícitos.
- Al reiniciar una cámara, restaurar también explicación y pestaña.
- Etiquetar fruta fresca y fotografías ilustrativas para no confundirlas con productos finales.

## Reforma vertical — 10 octubre 2026
- Una plantilla uniforme seguía haciendo repetitivas las escenas pese a cambiar ilustraciones. Se sustituyó el marco de slides por capítulos nativos y composiciones elegidas según cada relación.
- Mantener la misma API de gráficos permite conservar contenido, categorías y cámaras sin rehacer datos. Los 53 estados y enlaces directos se mantienen.
- La rueda de gráficos competía con la lectura vertical: reservar el zoom de rueda a Alt y ofrecer botones. Permitir arrastre solo al acercar y conservar gesto vertical normal.
- Los controles flotantes inferiores tapaban texto centrado. Se trasladaron al encabezado; las utilidades quedan agrupadas en Opciones.
- Completar antes de cancelar la animación evita residuos de opacidad cuando se cambia rápido de estado.
- La prueba de rueda debe recalcular el rectángulo del gráfico después de desplazar: una coordenada anterior puede quedar fuera del SVG y producir una falsa falla.
- Revisar fotografías además de cajas: una imagen puede caber perfectamente pero cortar el rostro. El agricultor se presenta completo mediante ajuste de contención.
- No cargar recursos heredados que la versión actual no usa; conservarlos sin referencias mantiene historial sin añadir coste de carga.
- La rapidez proviene de reutilizar datos y contratos probados, mientras se rediseña la estructura visual; documentar resultados de pruebas reales, no supuestos.

## Corrección de encuadre — 10 octubre 2026
- Revisar cajas dentro del capítulo no bastaba: las pruebas anteriores no comprobaban que el capítulo completo entrara en el viewport tras pulsar las flechas.
- `scroll-padding-top` y `scroll-margin-top` aplicaban dos veces el espacio del encabezado. Se usa una sola referencia a su altura efectiva.
- Escenas con altura natural mayor que el área disponible necesitan ajuste de exposición en escritorio. Medir cada estado y comprobar el encuadre final después de hacer zoom de diseño; conservar lectura vertical en móvil.
- El desplazamiento suave nativo con un temporizador fijo podía liberar demasiado pronto la detección del capítulo. La transición actual conoce su finalización, conserva el destino elegido y admite interrupción manual.
- Comprobar recorrido hacia adelante y hacia atrás, navegación con el foco en las flechas, cambios de tamaño y pantalla completa.
- Retirar avisos pendientes del contenido proyectado según preferencia del usuario; conservar respaldo documental y límites para intervención oral. ISO explica el proyecto registrado, sin sugerir obtención de un certificado.

## Tamaño de gráficos y filtros combinados
- El ajuste de una escena completa puede reducir demasiado los gráficos si se apilan gráfico y texto. Para el circular se utiliza composición horizontal en escritorio, con leyenda HTML separada del SVG; así sus controles conservan legibilidad.
- La fotografía de agricultores competía con la información principal. Se retiró de ese capítulo, conservando el archivo original y los créditos.
- Los filtros exclusivos impedían explicar categorías cruzadas. Se implementan selecciones independientes por ubicación y tipo: unión dentro de cada dimensión, intersección entre dimensiones.
- Cambiar el foco de cámara no debe borrar una combinación seleccionada. Vista completa conserva los filtros y Todos los limpia.

## Zoom de lectura sin menú
- Un encuadre completo puede hacer pequeños algunos textos. Añadir una cámara de lectura sobre el capítulo vivo permite ampliarlo sin duplicar gráficos ni perder eventos.
- El control queda en el margen lateral, con botones, deslizador vertical, porcentaje y retorno Ajustar. El nivel va de 100% a 200%; arrastre en texto/fondo mueve el contenido ampliado.
- El ajuste automático no debe medir la caja transformada por el zoom del usuario: usar altura de diseño y escala de encuadre evita que lo compense reduciéndolo.
- Excluir controles, enlaces y SVG del arrastre global conserva los filtros y las cámaras de gráficos. Restablecer al cambiar de subtema evita arrastrar un encuadre parcial a la explicación siguiente.

## Corrección de persistencia del zoom
La preferencia del usuario es conservar el zoom al navegar, incluso entre capítulos. Se retira el restablecimiento automático: mantener nivel y desplazamiento, limitándolo al contenido nuevo. El origen de transformación del nuevo capítulo se calcula en sus coordenadas locales para no depender de su posición antes del desplazamiento suave. Ajustar y Escape siguen restaurando 100%.

## Empleo y matriz en paralelo
El apilamiento centrado seguía reduciendo texto de empleo. Se distribuyen barras y explicación en columnas, con párrafos de 19 px antes del ajuste de encuadre. La Matriz de Valor utiliza también columnas para explicar cuadrantes y grupos sin una larga pila vertical. El subtema Mujeres sitúa ilustración y texto lado a lado. Móvil conserva el apilamiento; cadena mantiene panorama.
