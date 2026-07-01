# Registro de Cambios y Tareas (Changelog)

Este archivo mantiene un registro de todas las modificaciones y tareas pendientes de la aplicación, para asegurar que no se rompe nada y mantener el hilo del desarrollo.

## Tareas Pendientes (Planificadas)

- Ninguna tarea pendiente en este momento.

## Cambios Realizados

- **(2026-07-01) [V11] Soporte Offline:**
  - Se ha creado el archivo `manifest.json` y `sw.js` para habilitar el uso de la aplicación HOME sin conexión a internet.
  - Implementada estrategia *Network First* para garantizar que siempre se obtiene la versión más reciente al haber internet, o usar la memoria en modo avión.
  - Actualizada la versión a V11.

- **(2026-06-29) [V10] Ajustes Visuales Drag & Drop:**
  - Ajustado el globo visual al arrastrar una línea del calendario. Cuando se arrastra dentro de su mismo día, el globo se mantiene cerca del dedo; al salir hacia un día diferente, el globo salta por encima del dedo para no tapar la visión del día de destino.
  - Actualizada la versión a V10.

- **(2026-06-29) [V9] Mejoras de UI Calendario y Deshacer/Rehacer:**
  - Añadidas flechas (`‹` y `›`) en la vista anual para navegar de 1969 a 2060.
  - Añadido botón "Fecha actual" (Hoy) en la esquina inferior izquierda.
  - Movido el botón "🔎 Colores" a la esquina inferior derecha.
  - Añadida propiedad `user-select: none` para prevenir sombreado azul al arrastrar en el calendario.
  - Implementado sistema de historial (Deshacer/Rehacer) con botones `↶` y `↷`. Se guarda el estado automáticamente al mover, editar o borrar líneas de calendario. El límite es de 5 acciones hacia atrás/adelante.
  - Actualizada la versión inferior derecha a "V9".

- **(2026-06-28) [V2-V7] Mejoras UX/UI Calculadora:**
  - Calculadora a pantalla completa nativa sin márgenes de popup.
  - Reemplazado título y botón 'X' por un botón 'Salir' minimalista, moviendo el teclado hacia arriba.
  - El interior de la calculadora ahora hace scroll, permitiendo pulsar el '0' al abrir los paneles de Descuento/Aumento.
- **(2026-06-28) [V2-V7] Mejoras Drag & Drop del Calendario:**
  - El globo flotante ahora se sitúa 25px por debajo del dedo para no tapar la visión.
  - El objetivo de destino (día) se calcula 45px por encima del dedo, permitiendo ver qué día se va a seleccionar.
  - Implementado Auto-Scroll: arrastrar hacia los bordes superior/inferior hace scroll continuo (ideal para vista anual).
- **(2026-06-28) [V2-V7] Arreglos de Layout del Calendario:**
  - Reparado bug de Safari: las cuadrículas (días) ahora se estiran uniformemente para rellenar todo el espacio (`grid-template-rows: repeat(6, 1fr)`).
  - Altura mínima de los días reducida a 28px para que la cuadrícula se comprima correctamente en pantallas pequeñas y no oculte el botón inferior de la cámara (fotos).
  - El modo Pantalla Completa (`⛶`) usa ahora `100dvh` y salva la safe-area de iOS, arreglando el colapso visual y superposiciones.
- **(2026-06-28) Frases Motivadoras:** Añadidas "Lo hice porque nadie me dijo que era imposible" y "Quien la sigue la consigue" en ambas versiones de la app.
- **(2026-06-28) Calculadora Independiente:** Se extrajo la lógica JS, HTML y CSS de la calculadora hacia `calculadora/calculadora.html`.
- **(2026-06-28) Calculadora a Pantalla Completa:** La calculadora ahora ocupa 100vw y 100vh.
- **(2026-06-28) Historial de la Calculadora:** Se añadió un desplegable al pulsar el resultado, mostrando un historial tipo ticket con botones de borrar historial y cerrar.
- **(2026-06-28) Rediseño de Home:** El calendario ahora es el elemento principal del `#s-home`.
- **(2026-06-28) Pantalla CASAS:** Se cambió el FAB a "CASAS" y enlaza a la nueva pantalla `#s-houses-list` donde está el grid de casas, Exportar, Importar y "+ Nueva casa".
- **(2026-06-28) Pantalla Completa Calendario:** Se añadió el botón `⛶` para expandir el calendario a toda la pantalla.
- **(2026-06-28) Integración Calculadora:** Se actualizó el botón de calculadora en `index.html` para abrir `calculadora/calculadora.html`.
- *2026-06-28:* Creación del archivo de registro inicial.
