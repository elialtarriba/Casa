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
