# ADEX · Revisión de CV con IA

Presentación React de ocho pantallas: problema, proceso automatizado, responsabilidades, demostración, comparación, resultados y referencias. Paleta ADEX y visuales originales SVG/CSS; tipografías locales Manrope y Space Grotesk bajo OFL.

## Desarrollo

`npm ci`, `npm run dev`; producción: `npm run build`. La carpeta `dist` se publica directamente en GitHub Pages. `base: ./` permite alojarla en una subcarpeta.

## Presentar

Al 100% cada pantalla encaja. Flechas o rueda navegan; los botones inferiores también. El zoom visible permite ampliar hasta 220%. Al ampliar, arrastrar, usar rueda o flechas desplaza la cámara sin cambiar de pantalla. Los botones de siguiente/anterior conservan zoom y posición. «Encajar» vuelve a 100%. Doble clic alterna encuadre y 150%. En pantallas estrechas se usa lectura vertical con letra grande.

El menú ofrece índice, animaciones, pantalla completa y PDF. Se respeta inicialmente la preferencia de movimiento reducido. El PDF incluye los detalles esenciales del flujo y todos los escenarios y ensayos, sin requerir interacciones.

## Exposición

María Fernanda: contexto (0–2 min). Miguel: solución (2–5). Jahir: demostración en vivo (5–9). Jostin: resultados (9–11). Preguntas: último minuto. Los enlaces del formulario y registro conservan sus permisos originales; la web no procesa CV ni modifica datos.

## Evidencia y modelo

Cuatro envíos, dos perfiles ficticios; tres admisiones documentales y un rechazo previo a GPT. Promedio de Make: 61,95 s en los tres admitidos. No incluye carga ni revisión humana. Los 8 y 3 minutos humanos, la hora de mantenimiento mensual y los ahorros son supuestos del informe; no mediciones de nómina. Core S/45,60 es referencia del modelo (USD12 × S/3,80), no cotización vigente. Para 2.000 CV se requiere cotizar un paquete mayor. RR. HH. verifica evidencia y decide: admisión documental no significa contratación.

## Validación

`npm test` comprueba el modelo económico. `npm run test:ui` comprueba zoom, navegación, cámara, flujo, escenarios, evidencia y menú. Revisión visual en navegador de las ocho pantallas y cámara; PDF de ocho páginas revisado. `scripts/build_pdf.py` genera el PDF con ReportLab y fonttools usando fuentes del proyecto.

Los documentos fuente y CV no se distribuyen con el proyecto. Referencias y enlaces consultables figuran en la última pantalla.
