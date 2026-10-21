# Candela · La decisión de liberar un lote

Presentación web interactiva de 14 capítulos para el caso académico de calidad de nueces amazónicas peladas destinadas a Alemania. Mantiene la lógica del PowerPoint EA1 y los bloques A–D de ISO 9001:2015.

## Uso

Abrir la URL publicada mediante GitHub Pages. Navegar con botones, temas, índice, flechas izquierda/derecha o PageUp/PageDown. El contenido también se recorre con desplazamiento vertical libre. Opciones contiene animaciones, repetición, pantalla completa y notas del expositor.

El zoom de lectura está en el margen derecho. Conserva el nivel elegido entre capítulos y subtemas. Ajustar o Escape lo restablece. El zoom del flujograma es independiente.

En Cadena y flujograma: explorar la cadena completa, entrar al proceso evaluado, seleccionar símbolos o avanzar por todos los focos. Arrastrar el fondo mueve la vista; Vista general restablece su cámara.

## Desarrollo

Fuente: React 19, Vite 7, GSAP 3, Manrope y Literata locales.

Desde la carpeta del proyecto fuente:

```sh
npm ci
npm run build
npm run check
node tests/ui.test.mjs
```

`dist/` contiene el sitio estático. Los archivos compilados no requieren un servidor de aplicaciones ni instalar dependencias en el equipo del público. Para desarrollar: `npm run dev`.

En el repositorio publicado, `_source/` conserva el proyecto reproducible. Tras una actualización, copiar el contenido de `_source/dist/` a `presentaciones/candela/`, conservando README, documentos, licencias y fuente.

## Alcance del contenido

El incidente, la posible causa raíz, el flujo de control y las metas son académicos. No describen un incidente real ni un procedimiento auditado de Candela. Se distingue cadena general de referencia del proceso evaluado de recepción, cuarentena y liberación.

La ficha del proveedor no asigna puntaje real: conserva NV. El ejercicio interactivo y el calculador del indicador están identificados como demostraciones. El indicador devuelve N/A sin liberaciones y rechaza numerador superior al total. Las brechas críticas impiden aprobar un proveedor, cualquiera sea el puntaje.

## Imágenes

Imágenes aportadas por el usuario. Se usan como referencias, sin atribuir instalaciones, personas ni laboratorio a Candela. Se conserva el logo aportado. La imagen de chocolate con quinua fue excluida porque el caso trata de nueces peladas.

## Verificación

Ver `VALIDACION.md`. Compilación y pruebas funcionales en DOM. Esta ejecución no dispone de revisión visual en navegador automatizado; no se certifican mediante esas pruebas el encuadre real, el gesto táctil ni el comportamiento de pantalla completa.
