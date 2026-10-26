# Registro de Cambios y Tareas (Changelog)

Este archivo mantiene un registro de todas las modificaciones y tareas pendientes de la aplicación, para asegurar que no se rompe nada y mantener el hilo del desarrollo.

## Tareas Pendientes (Planificadas)

- Ninguna tarea pendiente en este momento.

## Cambios Realizados

- **(2026-10-26) [V15] Arreglos y novedades de la prueba:**
  - **PDF (búsqueda por colores y demás PDF):** la vista previa enseña cada página **entera en la pantalla**, sin moverse arriba y abajo. Si hay varias páginas, se pasan deslizando, una a una («1 / 2»). Imprimir y Guardar siguen igual.
  - **Logo en el PDF:** junto a la firma EliBi salía un cuadrado gris porque la imagen del logo guardada en la app estaba estropeada. Ahora sale el logo de la casita.
  - **Cambiar la nota de día:** el recuadro de la fecha ya no se sale de la ventana; queda alineado.
  - **Título «Home» y versión:** centrados entre los dos logos.
  - **El color del título «Home» no se veía:** un fondo decorativo de la pantalla de inicio quedaba por encima del título y lo aclaraba. Corregido: ahora el color elegido se ve tal cual. Se han revisado uno a uno todos los ajustes de color (fondo, agenda, Listas, Sitios, ⚙️, letra, título, ＋ Sitio, ＋ Cosa, Guardar, otros botones, versión y letra de los botones) y todos funcionan.
  - **Todos los colores con desplegable**, como en las notas: en ⚙️ Ajustes (los temas rápidos siguen arriba), en el editor de casa (color de la casa, botón ＋ Sitio y botón ＋ Cosa, debajo de «Tema rápido»), en el editor de lista (color de la lista, del fondo y de la letra) y en el color del día. Se toca la línea, se despliega la lista con nombres y grupos, se elige y se pliega sola. Al final hay «Elegir otro color…».
  - **Fotos de la agenda:** el botón 📷 (con el número de fotos) abre una ventana con todas las fotos del mes (o del año en vista anual). Tocando una foto vas a su día y se abre su nota. «Cerrar» para salir sin ir a ningún sitio.
  - **🎤 Dictar dentro de la nota:** botón «🎤 Dictar». Hablas y se va escribiendo en la nota; otro toque para parar. Luego se puede corregir.
  - **🎤 Nota por voz en la agenda:** botón 🎤 al lado de «Día · Mes · Año». Dices la fecha y después la nota («2 de abril de 2026, dentista a las cinco»). Al volver a tocar el micrófono se crea la nota en esa fecha. Entiende «2 de abril de 2026», «2 abril», «15/11/2026», «hoy», «mañana», «pasado mañana», «el lunes…» y también en catalán («demà», «3 de gener»…). Antes de crearla enseña en qué fecha se guardará, y se puede escribir o corregir a mano.
  - El dictado usa el reconocimiento de voz del iPhone. Si en la app instalada no está disponible, avisa y se puede usar el micrófono 🎤 del teclado.
  - Versión **V15**. `sw.js`: caché `home-cache-v15-2026-10-26`.

- **(2026-10-25) [V14] Ir a la Agenda o a las Listas desde cualquier sitio:**
  - En todas las pantallas de dentro de una casa (la casa y cada sitio, a cualquier nivel) hay arriba, encima del título, dos botones pequeños y discretos: **📅 Agenda** (izquierda) y **📝 Listas** (derecha).
  - Ya no hace falta volver atrás hasta «Mis sitios» para ir a la agenda o a las listas.
  - Si se ha elegido un color en «Letra de los botones», también se aplica a estos dos.
  - Versión **V14**. `sw.js`: caché `home-cache-v14-2026-10-25`.

- **(2026-10-25) [V13] El título de la casa o del sitio se ve entero:**
  - El título quedaba cortado («Comoda 3 cal…») porque el lápiz ✏️ y el botón «↩ Deshacer» ocupaban mucho sitio.
  - Ahora «Deshacer» es solo la flecha ↩ (más pequeño, en el mismo sitio) y el título puede ocupar **dos líneas**, con un tamaño de letra que se adapta a la pantalla.
  - Los nombres normales se leen enteros. Si un nombre es larguísimo y no cabe en dos líneas, termina en «…», pero se ve completo en la ruta de debajo del buscador.
  - Probado en iPhone pequeño (SE) y normal.
  - Versión **V13**. `sw.js`: caché `home-cache-v13-2026-10-25`.

- **(2026-10-25) [V12] Arreglos en listas y notas:**
  - **Listas:** la casilla «Añadir a…» está ahora arriba, debajo del título, y no la tapa el teclado. Se queda fija al hacer scroll y lo último que añades aparece justo debajo. Al desmarcar un tachado, vuelve arriba.
  - **Nueva lista:** se quita el ejemplo (Mi lista / Leche / Pan) de la ventana de crear o editar lista.
  - **Letra de los botones:** nueva línea en ⚙️ Ajustes, «Letra de los botones», que cambia el color de las palabras de los botones (Agenda, Listas, Sitios, Fecha actual, ＋ Sitio, ＋ Cosa…). Con «Automática» se queda como antes, con la letra a juego con cada botón.
  - **Notas: cambiar de día.** Tocando la fecha de arriba de la nota (▾) eliges otro día y la nota se mueve allí, con su color, fotos y aviso. Deshacer (↶) la devuelve en un solo paso.
  - **Notas: más espacio para leer.** El texto ocupa casi toda la ventana. El color, el aviso, las fotos y «Hecha» van en botoncitos pequeños debajo, que se despliegan solo al tocarlos.
  - **Colores de nota en una lista desplegable,** con nombre: Sin color, Azul celeste, Azul, Verde claro, Verde oscuro, Amarillo, Naranja, Rosa, Rojo, Marrón claro, Marrón oscuro y Caqui. Los mismos colores salen en «Color del día». Las notas antiguas con otros colores los conservan.
  - Versión **V12**. `sw.js`: caché `home-cache-v12-2026-10-25`.

- **(2026-10-25) [V11] Listas antes que sitios y navegación entre las tres partes:**
  - Debajo de la agenda hay ahora **tres botones**: **⚙️ Ajustes**, **📝 LISTAS** y **🏡 SITIOS** (antes «CASAS»).
  - «Mis casas» pasa a llamarse **«Mis sitios»**. Arriba a la izquierda está «‹ Agenda» y arriba a la derecha «📝 Listas».
  - **«Mis listas»**: arriba a la izquierda «‹ Agenda» y arriba a la derecha «🏡 Sitios». Dentro de una lista, «‹ Listas» sigue volviendo a todas las listas.
  - Cada botón tiene el color de su parte: el de Listas, el mismo en la agenda y en Mis sitios; el de Sitios, el mismo en la agenda y en Mis listas.
  - En ⚙️ Ajustes hay una línea nueva, **«Botón LISTAS»**, y «Botón CASAS» pasa a llamarse **«Botón SITIOS»**. Los temas rápidos también cambian el botón de Listas.
  - Comprobado que los tres botones caben en una sola línea, también en el iPhone pequeño (SE).
  - Versión **V11**. `sw.js`: caché `home-cache-v11-2026-10-25`.

- **(2026-10-24) [V9] Varias notas por día y ventana para elegir:**
  - **Puedes poner tantas notas como quieras en un mismo día.** Cada nota tiene su texto, su color, sus fotos y puede marcarse como hecha.
  - **Al tocar un día** (en la vista de mes o de año) sale una ventana redondeada con los colores de la agenda, que pregunta qué quieres hacer:
    - **＋ Añadir una nota**
    - **✏️ Editar una nota** (dice cuántas hay; si hay varias, eliges cuál)
    - **📅 Solo seleccionar el día** (lo marca sin escribir nada y queda listo para la vista «Día»)
    - Abajo, el **color del día**, que se cambia con un toque.
  - **Ventana de nota:** texto grande, color de la nota, fotos (añadir y quitar), «Marcar como hecha» y un botón 🗑️ para borrar solo esa nota (con confirmación). Cancelar no guarda nada, tampoco las fotos añadidas.
  - **Vista de día:** el botón «＋ Añadir nota» y el botón «⋯» con las opciones del día. Tocar una nota la abre para editarla.
  - La búsqueda por colores y tocar una línea dentro de un día también abren la ventana del día.
  - Deshacer (↶) y rehacer (↷) de la agenda siguen funcionando con las notas.
  - Versión **V9**. `sw.js`: caché `home-cache-v9-2026-10-24`.

- **(2026-10-24) [V8] Vista de día en la agenda:**
  - Nuevo selector **Día · Mes · Año** arriba de la agenda (sustituye los botones «Año» y «Mes»).
  - **Vista de día:**
    - Arriba, el día en grande («Sábado, 24 de octubre», año y «Hoy»), con flechas ‹ › para pasar al día anterior o siguiente.
    - Tocando la fecha se abre el selector del iPhone para **ir a cualquier día**.
    - Una tira con la semana (L a D): el día elegido resaltado, hoy con borde y un puntito en los días que tienen algo apuntado.
    - Debajo, todo lo apuntado ese día en grande, con su color, tachado si está hecho y con las fotos. Tocar una línea o el botón «✏️ Editar este día» abre la nota del día de siempre.
  - «Fecha actual» también funciona en la vista de día.
  - Al cambiar entre Día, Mes y Año se mantiene el mes que estabas mirando.
  - Versión **V8**. `sw.js`: caché `home-cache-v8-2026-10-24`.

- **(2026-10-24) [V7] Agenda en modo año más clara:**
  - Cada mes muestra su año al lado («Enero 2026»), así se sabe a qué año pertenece aunque bajes mucho. El mes actual sale resaltado.
  - En modo año, la cabecera («‹ Año 2026 › ⛶ Mes») y los botones de abajo («Fecha actual», ↶ ↷, «🔎 Colores») se quedan fijos. Solo se desplazan los meses.
  - **«Fecha actual» en modo año** te lleva directamente al mes actual (aunque estés al final del año o en otro año), lo deja visible y el día de hoy parpadea un momento.
  - Al pasar de mes a año con el botón «Año», se abre directamente en el mes que estabas mirando.
  - Versión **V7**. `sw.js`: caché `home-cache-v7-2026-10-24`.

- **(2026-10-24) [V6] Temas rápidos para cada casa y color de la versión:**
  - **Cada casa tiene su tema rápido** (en ✏️ dentro de la casa o en ⋯ → «Nombre, color e icono»): Marrones, Anaranjados, Amarillos, Verdes, Azules, Tonos del logo, Rosas y Lilas. Un toque cambia el fondo de la casa y sus botones «＋ Sitio» y «＋ Cosa».
  - **Y por colores, si quieres:** «Color de la casa» y «Botones» (＋ Sitio y ＋ Cosa) se pueden retocar uno a uno. Al retocar, el tema pasa a «A tu gusto». Cada botón tiene la opción «Como en Ajustes» para usar el color general.
  - La vista previa del editor muestra los dos botones con sus colores.
  - Cada casa puede tener colores distintos; las casas sin botones propios usan los de Ajustes.
  - **Nuevos grupos de color:** Verdes (de verde niebla a eucalipto) y Azules (de azul niebla a vaquero), también en Ajustes.
  - **Cuadro de la versión:** nueva opción en Ajustes para cambiar su color (el del lado de «Home» y el del pie). La letra se adapta sola. Los temas rápidos generales también lo cambian.
  - Las casas nuevas empiezan con el tema Marrones.
  - Probado todo de nuevo, sin errores. Versión **V6**. `sw.js`: caché `home-cache-v6-2026-10-24`.

- **(2026-10-24) [V5] Calculadora: todo cabe en pantalla:**
  - Al pulsar «- % Descuento», «+ % Aumento» o «Precio sin IVA», el panel empujaba el teclado hacia abajo y la última fila (0 , ⌫ =) quedaba fuera de la pantalla.
  - Ahora el teclado ocupa siempre el espacio que queda y se encoge un poco cuando el panel está abierto. La pantalla del número y los botones de arriba también se compactan. Todo queda visible sin hacer scroll.
  - Al cerrar el panel, la calculadora vuelve a su tamaño grande.
  - Probado en tres tamaños de iPhone (SE, normal y Max), con el cálculo de descuento/IVA funcionando.
  - Versión **V5**. `sw.js`: caché `home-cache-v5-2026-10-24`.

- **(2026-10-24) [V4] Ventanas más claras, sin agobiar, con más iconos y colores:**
  - **Nuevo editor sencillo** para crear o editar casas y sitios, en una sola ventana corta: arriba una vista previa (icono y nombre), debajo el nombre, la línea **Icono ›**, la línea **Color ›** (solo en casas) y los botones Cancelar y Crear/Guardar. Sustituye a las ventanas antiguas, que mostraban 51 colores y 70 iconos de golpe.
  - **Iconos por pestañas**, con un grupo cada vez y buscador:
    - Para casas: Casas, Casa, Objetos, Exterior y Mi imagen.
    - Para sitios: Muebles, Casa, Objetos, Exterior, Comida y Mi imagen.
    - Al tocar un icono se elige y vuelves al editor.
  - **11 iconos de casa dibujados** (casa, casa con jardín, piso, ático, casa de campo, cabaña, casa de playa, adosado, caravana, oficina, trastero) y una lista de emojis de casa limpia (sin pizzas ni vino).
  - **Más de 60 emojis nuevos** para guardar cosas: balón, puzzle, juegos de mesa, lana, costura, Navidad, pilas, cables, botiquín, medicinas, gafas, joyas, bolsos, abrigos, bañadores, facturas, documentos, sartenes, tarros, etc.
  - El icono se sigue poniendo solo según el nombre, también en casas («playa», «piso», «masía», «cabaña»…). En «Mi imagen» puedes usar una foto o pegar un emoji.
  - **Colores de casa por pestañas:** Marrones, Amarillos, Naranjas, Tonos del logo, Pastel e Intensos (los de antes). Cada color tiene su nombre. Los nuevos colores pastel generan automáticamente los tonos de toda la casa (fondo, iconos, rutas).
  - **Ajustes:** cada color también se elige por pestañas, con nombre.
  - Corregido: el botón principal de las ventanas tenía el texto descentrado, y las pestañas se aplastaban en pantallas pequeñas.
  - Probado todo de nuevo, sin errores. `sw.js`: caché `home-cache-v4-2026-10-24`.

- **(2026-10-24) [V3] Fondo, marrones, tonos del logo y más muebles:**
  - **Ajustes renovados:** arriba, 4 **temas rápidos** que cambian todo de un toque: «Tonos del logo», «Marrón pastel», «Miel y naranja» y «Lavanda (original)». Debajo, cada color por separado: al tocar una línea se abre la paleta.
  - **Muchos más colores**, agrupados: 10 marrones (de crema a tostado), 6 amarillos, 6 naranjas, 6 tonos del logo (amarillo del fondo, terracota del sillón y verde oliva) y pastel. Para la letra hay marrones oscuros (chocolate, café, nogal, cuero, canela, terracota) y otros tonos. Sigue el círculo para elegir cualquier color.
  - **Nuevo: color de fondo de la app.** Se quitan los tonos lilas del fondo, que ahora toma el color elegido (también arriba, en la zona de la hora, y en la lista de casas).
  - **Nuevo: color del botón ⚙️ Ajustes.**
  - **Versión siempre visible:** «V3» va dentro del pie, junto al copyright, y se ve también con la app instalada en la pantalla de inicio. El pie tiene el mismo color que el fondo (sin franja), y el botón CASAS tiene más espacio por debajo.
  - **13 iconos de muebles nuevos:** estantería de pared, estantería IKEA (cubos), sofá dos plazas, sillón, cama de matrimonio, cama individual, cama con cajones, cama con mueble, ventana, armario empotrado, armario sin empotrar, mueble comedor y armario de 3 puertas correderas (37 en total). Al escribir el nombre gana la coincidencia más precisa («Armario empotrado» pone el empotrado, no el armario normal).
  - Probado todo de nuevo, sin errores. `sw.js`: caché `home-cache-v3-2026-10-24`.

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
