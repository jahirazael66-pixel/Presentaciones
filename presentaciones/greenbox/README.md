# Greenbox · Del campo al mundo

Presentación HTML académica completa: 15 diapositivas, cadena de valor progresiva, gráfico interactivo, 8 fichas de estándares, matriz de 13 stakeholders, fuentes y notas del expositor.

## Abrir y presentar

1. Extrae el ZIP completo. Conserva la estructura de carpetas.
2. Abre `index.html` en un navegador moderno. No requiere instalar paquetes ni conexión a internet para presentar; los enlaces a fuentes sí necesitan internet.
3. Usa las flechas o los botones de navegación. La diapositiva de cadena de valor revela sus etapas en cada avance.
4. Usa **Índice** para saltar de diapositiva, **Notas** para consultar el guion y **Pantalla completa** para exponer. Escape cierra los diálogos; Escape fuera de un diálogo abre la vista general de Reveal.js. F11 es una alternativa para pantalla completa.
5. En la matriz, elige un filtro y después un grupo. Las tarjetas de certificaciones abren su detalle.

Para servirlo localmente, desde esta carpeta: `python -m http.server 8000`. Abre `http://localhost:8000`.

## Publicar en GitHub Pages

Destino sugerido: repositorio `jahirazael66-pixel/Presentaciones`.

1. En el repositorio, crea una carpeta `presentaciones/greenbox` y sube **todo el contenido** de esta carpeta, incluidos `index.html` y `assets/`. No subas solamente el ZIP.
2. En Settings → Pages, selecciona Deploy from a branch, rama `main`, carpeta `/ (root)` y Save. Si Pages ya está configurado, conserva su configuración actual.
3. Espera que termine el despliegue. La ruta esperada será `https://jahirazael66-pixel.github.io/Presentaciones/presentaciones/greenbox/`.

La presentación está preparada para publicar; esta entrega no modifica ni publica automáticamente el repositorio.

## Archivos

- `index.html`: contenido y notas de las 15 diapositivas.
- `assets/css/`: identidad, retícula, tipografías y movimiento reducido.
- `assets/js/main.js`: navegación, diálogos, certificaciones y filtros.
- `assets/js/charts.js`: gráfico ECharts con alternativa legible.
- `assets/js/stakeholders.js`: 13 registros y referencias.
- `assets/vendor/`: Reveal.js 5.2.1 y ECharts 5.6.0, con sus licencias.
- `assets/fonts/`: Manrope e Inter locales.
- `assets/images/`: logo original y SVG conceptual para favicon.
- `docs/`: investigación y prompt originales; notas del expositor en Markdown.
- `CREDITS.md`: fuentes, procedencia y límites de evidencia.
- `VALIDACION.md`: comprobaciones ejecutadas.

## Edición y rigor

Edita el contenido en `index.html` y la matriz en `assets/js/stakeholders.js`. No se presentan las certificaciones como vigentes para todas las sedes y productos. ISO 14001 se muestra como proyecto documentado, no como certificado obtenido. El gráfico laboral compara cifras históricas publicadas, sin inventar fechas de inicio y fin. La asignación a los ODS es interpretativa.

El diseño usa 16:9. En pantallas pequeñas se escala para conservar el formato de exposición; las notas y detalles tienen desplazamiento. Todos los controles interactivos admiten teclado. El texto de las fuentes ocupa una jerarquía secundaria y las referencias completas están al final.
