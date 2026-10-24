# Fundas textiles peruanas · propuesta para Nueva York

Presentación web de 20 secciones en React, Vite y GSAP, sin servicios ni claves externas. Diseño y desarrollo propios; fotografías de referencia AMAHÍ facilitadas por el usuario, identificadas en pantalla. Las fotografías no representan una colección propia ni acreditan materiales o certificaciones.

## Desarrollo

Node 20.19+ o 22.12+. Desde `_source`: `npm ci`, `npm run dev`. `prepare.mjs` copia las fotografías desde `../images` cuando se trabaja con la versión guardada en el repositorio. `npm run build` genera `dist/`, listo para reemplazar la versión publicada. Mantener `base: './'` en Vite.

`npm test`: comprobaciones independientes del modelo financiero. `npm run test:ui`: montaje en JSDOM y controles con estado persistente. La revisión visual real se hace en navegador; JSDOM no demuestra diseño responsive ni animación visual.

## Navegación

Flechas o PageUp/PageDown cambian de sección. Índice y navegación por tema, pantalla completa y animaciones en opciones. Zoom de lectura graduable a la vista; se conserva entre secciones. Cadena completa con vista general, selección de todas las etapas, zoom y arrastre. Tab/Enter permite recorrer sus nodos. Gráficos con cifras visibles e interacciones para comparación. Impresión incluye el contenido visible; para un PDF editorial de tamaño fijo se necesita una revisión específica adicional.

## Modelo y fuentes

Datos y orden derivados del informe facilitado, con 44 referencias externas enlazadas en `src/sources.js`. Supuestos comerciales identificados como propuestos o modelados. No se presentan pedidos, proveedores o certificaciones como confirmados. Las tasas de entrada son escenarios del informe; no verificación legal actual. El simulador no sustituye una cotización ni asesoría tributaria.

Cifras exactas se calculan antes de redondear: utilidad neta 3918.60 USD; IGV 3996; mínimo de caja 1251.20; VAN a 20% 7904.34 con recuperación anual de IGV y -513.16 sin recuperación.

## Recursos y licencias

React MIT; Vite MIT; GSAP según licencia incluida por su paquete. DM Sans y Cormorant Garamond SIL OFL: licencias adjuntas en `licenses/`. Fotografías AMAHÍ: material de terceros de referencia, sin concesión de nuevos derechos de uso; no eliminar atribución ni presentarlas como producto propio. Esquema de funda y diagramas SVG propios, sin fotos sintéticas.

## Publicación

Ruta `presentaciones/fundas/`; tarjeta nueva en el lobby raíz. El despliegue conserva las presentaciones anteriores. No subir node_modules, el informe fuente privado ni temporales de pruebas.
