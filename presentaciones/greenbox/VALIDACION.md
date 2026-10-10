# Validación — exploración visual de Greenbox

Iteración del 10 octubre 2026. Alcance: exclusivamente `presentaciones/greenbox/`; las otras presentaciones y el lobby se conservan.

## Comprobaciones realizadas en Chromium / Playwright
- Recorrido de las 15 escenas y sus 50 estados: errores JavaScript y encuadre de contenido, gráficos, leyendas, títulos y conclusiones respecto del pie.
- Filtros de dispersión: 5 internos, 8 externos, 7 primarios y 6 secundarios; los 13 grupos permanecen disponibles al restablecer la vista.
- Selección de los 13 stakeholders: nombre, justificación y respaldo dentro de la escena, con encuadre comprobado.
- Cámara: acercamiento, desplazamiento por arrastre y restablecimiento de la vista; selección por cuadrante y punto.
- Circular: 3/2/4/4 grupos, selección de categorías y exploración de miembros.
- Barras: selección de ambos momentos y comparación; 40 → 240, escala común con base cero.
- Cadena de valor: cuatro etapas con explicación y actores relacionados.
- Matriz de evidencia: selección de las ocho filas, con propósito, límite de verificación y cámara por fila.
- Movimiento reducido por defecto, activación explícita persistente y repetición con animaciones activas.
- Navegación mediante índice y teclado, selección SVG por Enter y estabilidad de la diapositiva al redimensionar a formatos móviles; apertura del índice en orientación vertical.
- Revisión visual de capturas de cadena, barras, clasificación, dispersión y evidencia. Ajustadas dimensiones intrínsecas SVG, leyendas y márgenes de cuadrantes.

No se afirma una auditoría de accesibilidad ni pruebas en todos los navegadores o dispositivos. En móvil se recomienda orientación horizontal para leer el formato de exposición. El estándar estético continúa sujeto a la evaluación del usuario.

## Rigor del contenido
Se revisaron fuentes actuales y se precisaron afirmaciones empresariales, sin inventar métricas de influencia/interés. +200 trabajadores, seis veces y +500% son cálculos derivados de 40 y 240. El circular cuenta grupos, no personas ni participación económica. La dispersión solo clasifica alto/bajo; las posiciones dentro del cuadrante no representan puntajes. El flujo no representa volumen. Las referencias de estándares no equivalen a certificados vigentes.

## Publicación
El commit contiene solo archivos de Greenbox. La verificación del despliegue comprueba GitHub Pages y el contenido público frente a los archivos publicados.

## Nueva revisión
Se revisan las perspectivas de agricultores y ambiente, los cuatro segmentos del circular y la categoría interna secundaria en filtros y detalles. La dirección financiera pasa a influencia alta estimada a partir del CFO documentado; su condición de soporte es independiente. La matriz sigue siendo cualitativa. Las referencias y límites se documentan en `docs/revision-de-contenido-y-stakeholders.md`.


## Edición fotográfica · 10 octubre 2026

- 15 diapositivas, 53 estados revisados en Chromium: sin errores JavaScript ni desbordamientos de contenido detectados.
- 19 imágenes aportadas decodificadas y cargadas correctamente; sin solicitudes fallidas.
- General → primer acercamiento → siguientes: cadena, agricultores y ambiente.
- Selección directa, flechas anterior/siguiente, retorno de cámara/texto/pestaña a general y familias de estándares: comprobados.
- Animaciones, repetición y persistencia tras recargar: comprobadas.
- Pantallas móviles 844×390 y 390×844: navegación e índice comprobados.
