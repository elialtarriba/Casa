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
