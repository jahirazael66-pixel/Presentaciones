# Greenbox · Del origen al impacto

Rediseño completo en React de la presentación Greenbox. Programa B2B propuesto de piña deshidratada para Alemania, con triple impacto, 2027. Se conservan literalmente los seis nombres de capítulos de la monografía y se distribuyen en 18 escenas con títulos simples. Los seis KPIs se resumen en tres dimensiones.

## Uso

Flechas / PageUp / PageDown: cambiar de sección. Índice, animaciones, pantalla completa y PDF en opciones. Zoom graduable visible y persistente entre secciones; Encajar vuelve al 100%. Al entrar en pantalla completa se aplica el encuadre de exposición. En móvil o lectura ampliada se permite desplazamiento natural. No hay ventanas flotantes con información esencial.

## Interacciones

- Matriz: filtros combinables interno/externo y primario/secundario. OR dentro de cada grupo y AND entre grupos. Los actores de nivel medio se sitúan en medianas; posiciones cualitativas, sin falsa puntuación numérica. No se inventan actores de bajo poder para llenar cuadrantes.
- Cadena: nueve etapas, vista general, primer acercamiento y todos los demás, zoom, arrastre y selección por teclado. El rombo representa liberación de calidad; rutas de corrección y aprovechamiento separadas.
- Empaque: capas con textos visibles; esquema propuesto, no envase oficial existente.
- Balance: 1.000 / 5.000 kg frescos con conservación de masa, producto, residuos y agua. El agua no se cuenta como residuo valorizado.
- Logística: planta superior real de diez cajas por nivel, vista frontal, embarque o total anual. No se afirma ocupación de un contenedor desde el cubicaje.
- KPIs: todas las seis metas visibles; la selección profundiza en dos comprobaciones a la vez.
- Margen: precio modificable, base y caída del 10%. Contribución no equivale a utilidad neta.

## Desarrollo y reproducción

Node 20.19+ o 22.12+. En `_source`: `npm ci`, `npm run dev`, `npm run build`. `prepare.mjs` recupera imágenes y PDF desde los directorios publicados contiguos. Vite usa rutas relativas, sin CDN ni claves. Tipografías locales Plus Jakarta Sans y Fraunces (OFL); GSAP y React.

`npm test` valida cálculos, balance, cubicaje y lógica de filtros. `npm run test:ui` comprueba montaje, estado persistente, filtros, índice y controles en JSDOM. JSDOM no verifica diseño real: la revisión visual se realiza en navegador. Ajuste de exposición por ResizeObserver, fuentes listas y cambio de tamaño; lectura normal en pantallas pequeñas.

PDF A4 horizontal: `python scripts/build_pdf.py` con reportlab, fonttools y pillow. `scripts/pdf-data.json` contiene las constantes exportadas desde `src/data.js`; actualizarlo al cambiar actores, capítulos o metas. El PDF contiene las 18 escenas en orden y los datos esenciales de todas las interacciones. No usa impresión del navegador. El enlace lleva versión para evitar reutilizar una descarga antigua.

## Procedencia y límites

Base: monografía Greenbox ADEX EC3 facilitada por el usuario. Fuentes externas de empresa, NESsT, UE, ISO, ZSVR, BRCGS, SGS e ICC enlazadas en `src/data.js`. Se verificaron durante la implementación la ficha ISO 14001:2026, el reporte NESsT de enero de 2026 y la aplicación escalonada del reglamento de envases. No se afirma certificación ISO propia de Greenbox, proveedor contratado ni comprador confirmado.

Se corrige a agricultores y envases como externos. NESsT y auditor independiente se separan. Primarios/secundarios son clasificación analítica de la relación con este programa. No se extrapolan los agricultores y empleos reportados por NESsT como impacto nuevo del programa de 20 t.

Fotografías y logo recuperados sin modificación de los recursos de la presentación anterior. `CREDITS.md` histórico conserva su procedencia. Los esquemas SVG/CSS son propios; fotografías de actividad no identifican un lote concreto ni prueban certificados.

## Publicación

Ruta `presentaciones/greenbox/`; la tarjeta del lobby se actualiza para el programa. Se conservan todos los archivos fuera de Greenbox y el historial de la versión previa. Recursos históricos permanecen para trazabilidad y caché; ya no se cargan las antiguas hojas de estilo ni librerías de diapositivas.
