# Notas de Elisabeth para la app HOME

Aquí se apunta todo lo que Elisabeth pide o comenta sobre la app, para no perder el hilo.

## 2026-10-24

- La app está en `iCloud Drive/Antigravity/HOME`.
- En iPhone, el botón de la parte inferior de la pantalla principal (CASAS) no se veía. Hay que hacerlo visible. → Hecho en V1.
- Leer siempre los `.md` de la carpeta antes de cambiar nada, y apuntar aquí lo que ella vaya diciendo.
- El inicio de «Mi casa» era un lío. Tiene que haber:
  - **Zona**, **Subzona** y **Ubicación**.
  - Que sea **sencillo poner un ítem en la ubicación**.
  - Que se vea **enseguida dónde está** la ubicación: dentro de su subzona, y la subzona dentro de su zona.
  - Que sea fácil **editar, crear, borrar**, etc. → Hecho en V1.
- Al terminar, poner **V1** (versión 1) al lado de «Home» en la pantalla principal. → Hecho.
- Comentó que había archivos que no eran de HOME:
  - `icon.png` es el logo de **Labores** (bastidor de bordar), no de HOME. El manifest ya no lo usa; se puede borrar de la carpeta.
  - `logo_elibi.jpg` sí es de HOME (firma EliBi en el logo y la calculadora).
  - `hogar-copia-2026-06-28.json` y `1_hogar-copia-2026-06-28.json` son **copias de datos**, no parte de la app. Mejor guardarlas en una subcarpeta `copias/`. La de `1_` tiene otras casas (STA JULITA, FABARA).
- Para qué sirve la app: ir apuntando lo que tiene en casa, cada cosa en su sitio, para que al buscar algo («llaves bici») la app le diga dónde lo puso, con la ruta completa. El buscador tiene que estar **arriba del todo** y buscar en **toda la casa**. → Hecho en V1 (buscador «¿Dónde está?»).
- Le parecía todo «lioso y confuso». Quiere algo **simple y sencillo**: poder poner todos los sitios y, dentro de los sitios, sus cosas.
- La **página principal sigue siendo la agenda** (le va bien tener agenda). Abajo tiene que **verse el botón para ir a las casas**. Al pulsarlo ve sus casas y escoge una.
- Pidió rehacerlo todo con **colores pastel**, bonito, sencillo, fácil e intuitivo, **con el buscador**. → Hecho en V1 (rediseño «sitios y cosas»).
- Su captura del iPhone aún mostraba **V12**: todavía no había sustituido `index.html` por la versión nueva.
- La app se publica con **GitHub Pages** en el repositorio `elialtarriba/Casa`. Hay que borrar de allí `.DS_Store`, `icon.png` y las copias `.json` (contienen datos personales).
- La app se usa sobre todo en su **iPhone** (también tiene que funcionar en Android).

### Peticiones para la V2
1. Un botón de **configuración** bonito: cambiar los colores de la agenda, del botón CASAS y de la letra. → Hecho (⚙️ Ajustes).
2. Al cambiar el color de una casa no se cambiaba (después de mucho probar sí). Revisar que todas las configuraciones funcionen. → Arreglado y probado.
3. «Exportar copia», «Copyright» e «Importar copia» en una sola línea, que se vea pero pase desapercibido. El copyright, solo «© Copy». → Hecho.
4. No se creaba otra casa. → Arreglado.
5. Poder cambiar el color de los botones «＋ Sitio», «＋ Cosa» y de todos los botones. → Hecho en Ajustes.
6. Más iconos: faltaban cómoda, armario, mesita de noche… → Hecho (24 iconos de muebles dibujados).
7. Poner **V2** y decirle qué archivos subir a GitHub. → Hecho.

### Peticiones para la V3
- Le gustan mucho los iconos dibujados. Pidió más: estantería de pared, estantería de IKEA, sofá dos plazas, sillón, cama de matrimonio, cama individual, cama con mueble, ventana, armario empotrado y sin empotrar, mueble comedor, cama individual con dos cajones debajo, armario grande de tres puertas correderas. → Hecho.
- Más colores, sobre todo **tonos de marrón** (que se distingan bien entre sí), amarillos y naranjas. Le gustaría todo **«marronoso» pastel**. → Hecho (tema «Marrón pastel» y paletas).
- Poder cambiar el **color de fondo**: el lila no le gusta. → Hecho.
- Poder cambiar el color del **botón de configuración**. → Hecho.
- Tener los **tonos del logo** para ponerlo todo de esos colores. → Hecho (tema y paleta «Tonos del logo»).
- El botón CASAS estaba demasiado cerca de la línea marrón del pie. → Más espacio y pie sin franja.
- Con la app en la pantalla de inicio **no se veía la versión**. Quiere que sea bonito y se vea todo. → Versión dentro del pie.

### Peticiones para la V4
- La ventana de editar casa (51 colores y 70 iconos a la vez) le parece **demasiado «tocha»**: abruma. Quiere en **todos los sitios** un diseño más claro, que no agobie. → Hecho: editor corto, e iconos y colores por pestañas.
- Pero **con más iconos y más colores**, como se había hablado (marrones, amarillos, naranjas, tonos del logo). → Hecho.

### Peticiones para la V5
- La calculadora le gusta mucho, pero al pulsar Descuento, Aumento o Precio sin IVA no se veían los botones de abajo. Quiere que quede bien con el panel abierto. → Hecho: el teclado se adapta y cabe todo.

### Peticiones para la V6
- Le han gustado mucho los **temas rápidos** de Ajustes y poder cambiar también color a color.
- Quiere lo mismo en **cada casa**: su propio tema rápido (marrones, anaranjados, amarillos, verdes o azules). → Hecho.
- Poder cambiar el color del **cuadro y la letra de la versión**, para que no sea siempre lila. → Hecho.

### Peticiones para la V7
- En modo año, al ir bajando no sabía a qué año pertenecía cada mes. Poner el **año al lado de cada mes**. → Hecho.
- En modo año, al pulsar **Fecha actual** estando abajo, que vaya directamente a la fecha actual y se vea. → Hecho.
- Poner **V7**. → Hecho.

### Peticiones para la V8
- Además de la vista mensual y la anual, quiere un **botoncito para la vista del día** que quiera ver. → Hecho (selector Día · Mes · Año; en la vista de día se puede elegir cualquier fecha).

### Peticiones para la V9
- No podía hacer más de una nota en un día. Tiene que poder hacer **tantas notas como quiera en un día**. → Hecho.
- Al pulsar un día debe preguntar: **añadir una nota, editar una nota existente o seleccionar solo el día**. Con un **popup bonito, redondeado y del tema**. → Hecho.

### Peticiones para la V10 (2026-10-25)
1. En la agenda, al añadir una nota, poder poner un **aviso a la hora y el día** que quiera, con un **popup bonito** con lo que pone la nota, que salga **aunque la app no esté activa** y que se pueda cerrar una vez leído. → Hecho: ventana de aviso dentro de la app, más la opción de añadirlo al Calendario del iPhone para que avise con la app cerrada. Una web no puede avisar sola con la app cerrada; se lo he explicado.
2. En «Mis casas», a la derecha, un botón **Listas** que lleve a otra página donde añadir listas, cada una con su color de lista, color de fondo y color de letra. Al pulsar el cuadradito, el ítem se tacha y baja al final. Listas una debajo de otra, como las casas, con «＋ Nueva lista». → Hecho.
3. **Exportar e importar todo**: agenda, casas y listas. → Hecho (también ajustes y calculadora).
4. Que con el acceso directo en el móvil se vea todo y funcione **sin internet ni ninguna conexión**. → Hecho (hay que abrirla una vez con internet después de subir la versión).

### Peticiones para la V11
- Poner las **listas antes que las casas**: debajo del calendario, tres botones: **configuración, listas y sitios**. → Hecho.
- Las casas ya no se llaman «Mis casas», sino **«Mis Sitios»**. → Hecho (dentro siguen siendo casas: «＋ Nueva casa»).
- En **Listas**: a la izquierda, botón para ir a la **Agenda**; a la derecha, botón para ir a **Mis Sitios**. → Hecho.
- En **Mis Sitios**: arriba a la izquierda, botón para ir a la **Agenda**; arriba a la derecha, botón para ir a **Mis Listas**. → Hecho.

### Peticiones para la V12
1. En las listas, la casilla de añadir se escondía debajo del teclado. Ponerla **arriba, debajo del título y los botones**, encima del primer ítem. → Hecho.
2. Poder cambiar el **color de las palabras de los botones** (Agenda, Sitios, Listas). → Hecho (Ajustes → «Letra de los botones»).
3. En la agenda, **cambiar el día de una nota** desde dentro de la nota, si se ha equivocado. → Hecho.
4. El **color de la nota en una lista desplegable**, para que no se vea tanta cosa, con estos colores: azul celeste, azul, verde claro, verde oscuro, amarillo, naranja, rosa, rojo, marrón claro, marrón oscuro y caqui. Al editar una nota se tiene que **ver más espacio de la nota**. → Hecho.
5. Al crear una lista nueva, **quitar el ejemplo** (Mi lista / Leche / Pan). → Hecho.

### Peticiones para la V13
- Dentro de un sitio, el **título no se veía** (quedaba cortado por el lápiz). Arreglarlo. → Hecho (título en dos líneas y «Deshacer» solo con la flecha ↩).

### Peticiones para la V14
- Al ir entrando en los sitios, para ir a la Agenda o a las Listas había que volver atrás hasta el inicio de Mis Sitios. Poner **dos botones (Agenda y Listas) arriba, encima del título, en cada pantalla de cada sitio**, que no sobresalgan mucho. → Hecho.

### Peticiones para la V15 (2026-10-26)
1. El PDF de la búsqueda por colores no se veía entero en la pantalla: tiene que verse todo, sin moverse arriba y abajo. Al lado de EliBi no se veía el logo. → Hecho.
2. En «Cambiar la nota de día», el recuadro de la fecha sobresalía y no estaba alineado. → Hecho.
3. El título «Home» y la versión no estaban centrados entre los dos logos. → Hecho.
4. El color del título «Home» se cambiaba en Ajustes pero no en la palabra. Revisar que todos los ajustes funcionen. → Hecho (todos revisados).
5. El desplegable de colores de las notas le gusta: ponerlo **en todos los sitios donde se pida color**, debajo de los temas (los temas le encantan y no se deben quitar). → Hecho.
6. En la agenda, al tocar el icono 📷 con el número de fotos, que salga una ventana con todas las fotos, poder tocar una e ir a su nota y su día, y poder cerrar la ventana. → Hecho.
7. En cada nota, un **micrófono**: hablar y que se vaya escribiendo, y poder corregirlo. → Hecho.
8. En la agenda, un **botón de micrófono**: decir primero la fecha («2 abril 2026») y luego la nota, y al volver a pulsar se crea la nota en esa fecha. → Hecho.

### Peticiones para la V16
- En el navegador, al pulsar para pasar de un mes a otro, **a veces se hacía zoom** y no debería. → Hecho.
- En los modos día, mes y año, **deslizar el dedo** para pasar adelante o atrás, **como pasar la hoja de un libro**. **Sin estropear nada de lo que ya hay.** → Hecho, con cuidado de no interferir con arrastrar notas, el scroll de la vista Año ni la ventana del día.

### Peticiones para la V17
- El giro de la V16 no parecía pasar la hoja de un libro. Quiere ver **media página actual y media de la siguiente**, como en la foto que mandó (una hoja que se curva en diagonal). Pidió verlo **antes** en una prueba.
- En la prueba: **más inclinado**, que la hoja **siga el dedo** y que **si se para, la hoja se pare**. Además, más **3D** y quitar una **sombra que no pertenecía a nada**.
- Le ha encantado («¡Perfecto! ¡Qué bonito!»). → Puesto en la agenda en la V17.

### Peticiones para la V18
- En la nota por voz de la agenda, con «avui» funcionaba, pero con **«mañana» y «demà» no se grababa la nota**. Afinarlo o arreglarlo. → Arreglado: se perdía la última frase al parar. Añadida la elección de idioma (castellano / català) y más maneras de decir la fecha.
- Habla en castellano y en catalán.

### Peticiones para la V19
- Que la nota por voz entienda **«el lunes de la semana que viene»**, **«el dilluns de la setmana que ve»**, «el martes», «el miércoles»… → Hecho.

### Peticiones para la V20
1. En las listas, que **solo el recuadro** tache o destache, y un **botón para editar** al lado de la ✕. Así hay más espacio para tachar en la tienda con el móvil. → Hecho.
2. Un sitio para **guardar los tickets** de todas las compras:
   - con un **botón** propio;
   - un **calendario de fotos** en vez de notas;
   - una ventana que pregunta **el día**, y luego la **cámara o Fotos**;
   - **fotos que no pesen**, guardadas en un **archivo aparte**;
   - cada ticket, con o sin **foto de lo que es**;
   - **fácil de encontrar**, bonito, profesional, con **temas** (que no falte el marrón);
   - pasar de mes **como una hoja**.
   → Hecho.
3. **Iconos nuevos** para la casa, la calculadora y el botón de tickets, con las **esquinas redondeadas** y **un poco más luminosos**. → Hecho.
- «Pasar entre sitios como una hoja»: aclarado, no hace falta; los sitios se quedan como están.

### Peticiones para la V21
1. Iconos: **menos amarillo y más marrón claro**. → Hecho.
2. En tickets, al buscar, que el **teclado se esconda solo**. → Hecho.
3. En la línea de Agenda, botones para ir a **Listas y Sitios**, **simétricos y alineados**. → Hecho (barra de iconos igual en todas las pantallas).
4. En esa línea, un botón para **buscar por fechas o por nombre** y hacer un **PDF bonito** con precios y totales, para imprimir, y poder cerrarlo y volver a tickets. → Hecho.
5. **Iconos de Listas y Sitios** al estilo del de tickets, para sustituir todos los botones de Listas y Sitios. Que todo quede **alineado, con diseño y simétrico**. → Hecho (además, iconos de Ajustes, Agenda y Buscar a juego).
