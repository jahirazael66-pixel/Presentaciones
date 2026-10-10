# Procedencia y alcance

## Contenido

Fuente principal: `docs/Info.txt`, investigación proporcionada por el usuario. Instrucciones: `docs/prompt-original.txt`. Se conserva el material original para trazabilidad; los artefactos de extracción (favicons, “+2” y enlaces de imágenes intermediados) no se usan como contenido de diapositivas.

Contraste de la propuesta: Greenbox About Us, artículo NESsT del 28 de enero de 2026 y resultados ProInnóvate de 2021, p. 14. Las referencias Greenbox Certifications, consultas comerciales, LinkedIn y Datos Perú se conservan desde el informe; no se afirma revalidación de certificados ni identidad registral actual. El artículo NESsT es una fuente del financiador, no una auditoría independiente.

La versión actual distingue administración/finanzas y RR.HH. como internos secundarios en la adaptación funcional de Info.txt; esto no se presenta como clasificación universal. Clarkson considera primarios a los empleados, como explica la revisión de contenido. Las entidades comerciales extranjeras se mantienen externas provisionalmente respecto de Greenbox S.A.C. Perú; el perímetro y propiedad no están completamente comprobados. Certificadores y reguladores conservan el criterio del informe, indicando su carácter interpretativo. Los nombres de clientes y proveedores comerciales no se inventan.

## Identidad e imágenes

- Logo Greenbox: PNG original adjunto por el usuario. Se mantiene su proporción y apariencia. Uso en esta presentación académica según la instrucción del usuario; no se declara una licencia pública para otros usos.
- Verde dominante extraído: RGB 42, 211, 134 (`#2AD386`). Complementos: blanco, crema `#F7F3E8`, menta `#E7F7ED`, durazno `#F4DFCF` y verde profundo `#163D2C`.
- Ilustraciones de fruta, personas, caja, hoja, globo y ciclo: SVG conceptuales originales creados para esta presentación. No representan instalaciones ni trabajadores específicos de Greenbox.
- Fotografías documentales y aportadas: procedencia y límites indicados más abajo.

## Dependencias locales de versiones iniciales (historial)

- Reveal.js 5.2.1 — MIT; fuente: https://github.com/hakimel/reveal.js . Distribución obtenida de jsDelivr; licencia en `assets/vendor/reveal-LICENSE`.
- Apache ECharts 5.6.0 — Apache-2.0; fuente: https://github.com/apache/echarts . Licencia y NOTICE en `assets/vendor/`.
- Manrope e Inter — SIL Open Font License 1.1. Archivos obtenidos de Google Fonts. Licencias en `assets/fonts/`.
- No se añade GSAP: Reveal.js gestiona navegación y fragmentos; ECharts anima el gráfico; la Web Animations API del navegador gestiona las entradas secuenciadas y el dibujo de iconos. Esta implementación permite cancelar animaciones y respetar movimiento reducido sin otra dependencia.

No se usan CDNs durante la exposición. Las consultas a fuentes externas requieren internet. Los archivos fuente pueden editarse sin compilación ni gestor de paquetes.

## Investigación de movimiento y exposición · revisión 2

- Reveal.js, Fragments: https://revealjs.com/fragments/ — avance incremental y eventos fragmentshown/fragmenthidden.
- Reveal.js, Transitions: https://revealjs.com/transitions/ — transiciones por diapositiva.
- Reveal.js, Auto-Animate: https://revealjs.com/auto-animate/ — opción investigada; no se utiliza para evitar emparejamientos ambiguos entre escenas diferentes.
- MDN, Element.animate(): https://developer.mozilla.org/en-US/docs/Web/API/Element/animate — animaciones nativas con objetos cancelables.
- GSAP, Timeline y matchMedia: https://gsap.com/docs/v3/GSAP/gsap.timeline() y https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/ — alternativas investigadas; no añadidas como dependencias.

Las cifras animadas siempre terminan en los valores documentados. Los pasos de la cadena, el ciclo de compost y las conexiones visuales son ilustraciones conceptuales. La animación no representa cantidades, tasas o resultados nuevos.

## Reforma visual narrativa
- DM Sans y DM Serif Display: Google Fonts, archivos locales y licencias OFL incluidas en assets/fonts.
- GSAP 3.15.0 y plugins MotionPath, DrawSVG y MorphSVG: gsap.com / paquete npm gsap. Términos oficiales en assets/vendor/gsap-LICENSE.txt.
- Diagramas e ilustraciones SVG conceptuales realizados para esta presentación. No representan fotografías ni instalaciones verificadas.
- En la reforma vertical se conserva Reveal.js como archivo histórico; no se carga. La navegación actual es nativa y los gráficos son SVG.

Los gráficos interactivos de `learning.js` son SVG originales del proyecto; no añaden dependencias. Los cálculos de empleo y composición se derivan de la información ya documentada.

## Fotografías documentales

Imágenes publicadas en la [ficha de Greenbox de NESsT](https://www.nesst.org/greenbox). Se conservan sin retoque; el encuadre se resuelve en CSS/SVG. No se afirma la fecha de captura ni que una fotografía pruebe certificación, vigencia o situación actual. Los derechos permanecen con sus titulares.

- `greenbox-campo.jpg`: [archivo fuente](https://images.squarespace-cdn.com/content/v1/58d072963e00bea07a2ca2da/263426ef-117d-4e1a-9c64-148bb1d63418/55458116386_30fd1ffdb2_b.jpg?format=750w).
- `greenbox-planta.jpg`: [archivo fuente](https://images.squarespace-cdn.com/content/v1/58d072963e00bea07a2ca2da/1592329915131-ISIKGMFRXACUITFGJHVV/DSC_8591.jpg?format=750w).
- `greenbox-empaque.jpg`: [archivo fuente](https://images.squarespace-cdn.com/content/v1/58d072963e00bea07a2ca2da/1592329914243-5FACYKFWVX4Z25R379KI/DSC_8294.jpg?format=750w).


## Imágenes aportadas por el usuario · 10 octubre 2026

Se incorporan las 19 imágenes sin alterar sus píxeles, textos ni marcas. Se preservan transparencias originales y se adaptan con contenedores blancos, márgenes, `object-fit` y encuadre CSS/SVG. No se aumenta resolución artificialmente. Imágenes de productos: ilustrativas, no prueba de un producto o envase Greenbox. Paisaje e instalaciones: aportadas, sin geolocalización verificada. Distintivos: referencia gráfica, no documentos de certificación ni prueba de vigencia.

- `valle.webp` → `assets/images/aportadas/paisaje-valle.webp`
- `planta greenbox.jpg` → `assets/images/aportadas/instalaciones.jpg`
- `seleecion fruta.jpg` → `assets/images/aportadas/seleccion-fruta.jpg`
- `piña.webp` → `assets/images/aportadas/pina.webp`
- `mango.png` → `assets/images/aportadas/mango.png`
- `Aguaymanto.webp` → `assets/images/aportadas/aguaymanto.webp`
- `bananaa.png` → `assets/images/aportadas/banana.png`
- `nibs.jpg` → `assets/images/aportadas/nibs.jpg`
- `polvo maca.jpg` → `assets/images/aportadas/maca.jpg`
- `polvo.jpg` → `assets/images/aportadas/cacao.jpg`
- `pure mango.jpg` → `assets/images/aportadas/pure-mango.jpg`
- `logo usda.gif` → `assets/images/aportadas/usda.gif`
- `eu organic.jpg` → `assets/images/aportadas/eu-organic.jpg`
- `bio suisse.png` → `assets/images/aportadas/bio-suisse.png`
- `jas organic.jpg` → `assets/images/aportadas/jas.jpg`
- `bgrs logo.webp` → `assets/images/aportadas/brcgs.webp`
- `haccp.webp` → `assets/images/aportadas/haccp.webp`
- `kosher.jpg` → `assets/images/aportadas/kosher.jpg`
- `fairtrade.png` → `assets/images/aportadas/fairtrade.png`

## Dependencias activas en el recorrido vertical
La página actual carga únicamente las fuentes locales DM Sans y DM Serif Display, GSAP local, `stakeholders.js`, `learning.js` y `journey.js`, junto con estilos de fuentes y `journey.css`. Los archivos de bibliotecas anteriores se conservan sin cargarse. No se añade ninguna imagen ni licencia externa en esta reforma.
