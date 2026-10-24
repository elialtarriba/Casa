# Registro de Cambios y Tareas (Changelog)

Este archivo mantiene un registro de todas las modificaciones y tareas pendientes de la aplicación, para asegurar que no se rompe nada y mantener el hilo del desarrollo.

## Tareas Pendientes (Planificadas)

- Ninguna tarea pendiente en este momento.

## Cambios Realizados

- **(2026-10-24) [V2] Ajustes de colores, iconos de muebles y arreglos:**
  - **⚙️ Ajustes** (botón redondo junto a CASAS, en la agenda). Permite cambiar los colores de la agenda, el botón CASAS, el color de la letra, el título «Home», los botones «＋ Sitio» y «＋ Cosa», los botones Guardar/Añadir y el resto de botones (volver, deshacer, cancelar…). Cada opción tiene 10 colores pastel y un círculo para elegir cualquier otro. El cambio se ve al momento y se guarda. Hay un botón para volver a los colores originales. Los ajustes también van dentro de «Exportar copia».
  - **Arreglado: casa nueva que no aparecía.** Al guardar, la app refrescaba la agenda en lugar de la lista de casas: la casa se creaba pero no se veía. Ahora aparece al momento y sale el aviso «Casa creada».
  - **Arreglado: cambiar el color de una casa.** Era el mismo fallo, el cambio se guardaba pero no se veía. Ahora se ve enseguida, tanto desde la lista (⋯) como desde dentro de la casa.
  - **Nuevo lápiz ✏️ dentro de la casa:** edita lo que estás viendo. En la raíz edita la casa (nombre, color, icono); dentro de un sitio, ese sitio.
  - **Iconos de muebles dibujados** (no existen como emoji): armario, cómoda, mesita de noche, estantería, escritorio, mesa, zapatero, mueble TV, aparador, vitrina, baúl, cajón, balda, altillo, perchero, mueble de baño, despensa, caja, caja de cartón, nevera, lavadora, cama, sofá y trastero. Se ponen solos al escribir el nombre (también en catalán: calaixera, armari, tauleta…). Si el nombre no coincide con ningún icono, se muestran todos para elegir.
  - Máximo de casas ampliado de 5 a 10.
  - **Exportar · © Copy · Importar** en una sola línea, pequeña y discreta.
  - Las ventanas de crear o editar casa y sitio, en pastel.
  - Probado: crear y editar casa, color, iconos, sitios, cosas con foto, buscar, deshacer, nota de la agenda, calculadora, exportar e importar.
  - Versión **V2**. `sw.js`: caché `home-cache-v2-2026-10-24`.

- **(2026-10-24) [V1] Rediseño completo: pastel, sencillo, «sitios y cosas»:**
  - **Colores pastel** en toda la app (rosa, lavanda, menta, mantequilla) y letra redondeada del iPhone. Se oculta el panel de depuración («APP STARTED…»).
  - **Agenda:** se mantiene como página principal, con el mismo funcionamiento y nuevos colores. Debajo, el botón **🏡 CASAS** grande y siempre visible.
  - **Mis casas:** una tarjeta grande por casa con foto o icono y «N sitios · N cosas». Al tocarla entras. El botón **⋯** sirve para nombre, color, icono, foto o borrar. «＋ Nueva casa» al final de la lista. Exportar e importar copia siguen abajo.
  - **Dentro de una casa, solo dos ideas:** **sitios** y **cosas**. Un sitio puede tener dentro otros sitios y cosas, sin límite (Habitación › Armario › Cajón › Caja…). Ya no hay que decidir si algo es zona, subzona o ubicación. Los datos de antes pasan tal cual: las zonas, subzonas y ubicaciones son sitios y sus ítems son cosas.
  - Todas las pantallas son iguales: arriba el buscador, debajo la ruta (tocable para volver atrás) y la lista de sitios y cosas. Abajo, dos botones grandes: **＋ Sitio** y **＋ Cosa** (en la raíz de la casa solo «＋ Sitio»).
  - **＋ Cosa:** una hoja desde abajo donde escribes y pulsas «Añadir». Puedes añadir varias seguidas, también con foto.
  - **Botón ⋯ en cada fila** (menú desde abajo). En un sitio: cambiar nombre o icono, mover a otro sitio, añadir foto del sitio, PDF y borrar. En una cosa: dónde está, sus fotos, cambiar nombre, añadir foto, mover y borrar.
  - **Mover** cosas y también sitios enteros (con todo lo que tienen dentro) a otro sitio de la casa.
  - Se quitan de la vista las funciones de lista de tareas: marcar como hecho, números, colores, 👁, 📎, 🖼️ y anterior/siguiente. Los datos no se borran.
  - **Buscador «¿Dónde está?»** igual que antes: por palabras, con la ruta completa. Al tocar un resultado te lleva al sitio y la cosa se ilumina.
  - Los avisos («Guardado…», «Movido a…») salen arriba para no tapar los botones.
  - La flecha ‹ sube un nivel. En la raíz de la casa vuelve a «Mis casas». «↩ Deshacer» deshace el último cambio.

- **(2026-10-24) [V1] Nueva numeración de versión, botón CASAS visible y Mi Casa reorganizada:**
  - La versión vuelve a empezar en **V1** (antes V12). Se muestra junto al título «Home» y en la esquina inferior derecha.
  - **Botón CASAS visible en iPhone:** antes estaba fijado al borde inferior y quedaba tapado por el pie de copyright. Ahora forma parte de la pantalla, debajo del calendario, más grande y con relieve. El pie de copyright respeta la zona segura inferior del iPhone.
  - **Mi Casa por niveles:** Zona › Subzona › Ubicación. Cada nivel es una lista vertical con su icono, nombre, contenido («2 subzonas · 5 ítems»), botones ✎ editar y ✕ borrar, y botón grande «＋ Nueva …».
  - **Ruta siempre visible:** al entrar en una zona, subzona o ubicación se ven las cajas anidadas Casa › Zona › Subzona › Ubicación. Tocar cualquiera de ellas lleva a ese nivel. La flecha ‹ de arriba sube un nivel.
  - **Ítems en la ubicación:** la casilla para añadir está arriba («Añadir a …»), y los ítems nuevos aparecen los primeros. Se mantienen color, fotos, PDF, marcar y arrastrar.
  - **Buscador «¿Dónde está?»** arriba del todo dentro de cada casa, siempre visible (se queda fijo al hacer scroll). Busca en toda la casa mientras escribes, por palabras sueltas y en cualquier orden («llaves bici» encuentra «Llaves de la bici»). No distingue acentos ni mayúsculas, ignora palabras como «de», «la», «el» y acepta singular o plural. Cada resultado muestra la ruta completa (Zona › Subzona › Ubicación). Al tocarlo te lleva a esa ubicación y el ítem parpadea en amarillo. También encuentra lugares por su nombre y busca por color. El botón 🔎 Buscar de la barra lleva a este buscador.
  - **Mover ítems:** botón ⇄ en cada ítem para pasarlo a otra ubicación de la misma casa.
  - **Borrar:** ya no bloquea si hay cosas dentro; avisa de cuántos lugares e ítems se borrarán y pide confirmación. También se borran las fotos adjuntas de esos lugares.
  - Crear una zona/subzona/ubicación ya no te mete dentro: te quedas en la lista para poder crear varias seguidas.
  - Barra superior simplificada: se quitan ‹ › (anterior/siguiente) y 🗑 (ahora el borrado está en cada fila).
  - Datos antiguos: si había niveles más profundos («Compartimentos») o ítems en zonas/subzonas, siguen visibles y editables.
  - **Archivos:** `manifest.json` usaba `icon.png`, que es el logo de Labores. Ahora usa `logo.png` (la casita). `sw.js`: quitado `icon.png` y renovada la caché (`home-cache-v1-2026-10-24`) para que el iPhone cargue la versión nueva.

- **(2026-07-01) [V12] Mejoras UX/UI Calculadora:**
  - Añadidas las propiedades CSS `touch-action: manipulation` y `user-select: none` a los botones de la calculadora (`.calc-key` y `.calc-mini-key`) para prevenir el zoom automático no deseado al pulsar rápidamente (doble toque) en dispositivos iOS.
  - Actualizada la versión a V12.

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
