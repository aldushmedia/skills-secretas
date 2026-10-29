# Modo 2 · Anatomía

Este modo construye figuras SVG isométricas, interactivas y muy detalladas, que
explican una idea técnica como un objeto físico real (un banco de pruebas, un
reloj comparador, una cajonera, un plotter, una cerradura). Tienen muchas
piezas sólidas, pequeñas y precisas, sombreado en cuatro tonos, el orden de
pintado correcto, una tarjeta con título, pista y lectura en vivo, y un
movimiento suave y tranquilo. Funciona sin framework (TypeScript o JS que
escribe SVG y HTML) y en React o Next.js. Puede agregar shaders WebGL
realistas (fuego, escape de un motor, agua, cáusticas, luz de lámpara) que
viven dentro del dibujo, con la misma perspectiva isométrica. También imprime
una figura como PDF A4 (póster, plano u hoja de repaso).

**Úsalo** cuando alguien quiera una ilustración isométrica, un diagrama o una
figura que explique algo para documentación, un blog, una página de venta o un
artículo, un dibujo técnico "premium", un explicador interactivo, o un SVG que
muestre cómo funciona un sistema, un algoritmo o un componente, aunque nunca
diga "isométrico".

**Necesitas:** Node.js 20.10 o más reciente, y Chrome o Chromium para las
revisiones. No hay que instalar paquetes: el kit solo usa módulos de Node. Si
Chrome está en un lugar poco común, define `CHROME_PATH`.

**Idioma.** Escribe en el idioma del usuario, en español por defecto, todo lo
que se ve en la figura (título, pista, lectura en vivo, leyenda, pie y textos
de accesibilidad) y en las hojas para imprimir. Habla con el usuario en ese
mismo idioma. Los nombres de funciones del kit y los comandos se quedan como
están. `pageHtml` marca la página como `lang="es"`; si la figura está en otro
idioma, pásale `lang` (por ejemplo, `lang: "en"`). Los mensajes de los scripts
(`audit passed`, `line ends: 0`) están en inglés: cuando le cuentes al usuario
cómo va, díselo en español.

## Rutas de este modo

`kit/`, `scripts/`, `examples/` y `references/` están dentro de la carpeta de
este modo (`modos/2-anatomia/`), que aquí llamamos `ANATOMY_DIR`. Toma su ruta
absoluta una vez y úsala en todos los comandos, por ejemplo
`node "$ANATOMY_DIR/scripts/capture.mjs" ...`. Los scripts encuentran el kit
por su propia ruta, así que funcionan desde cualquier carpeta.

Las figuras del usuario van en su proyecto (por ejemplo `anatomia-<nombre>/`),
no dentro de la carpeta del modo. Copia ahí `kit/` y `scripts/` desde
`ANATOMY_DIR` y escribe el `build.mjs` de la figura junto a ellos, en una
subcarpeta (por ejemplo `anatomia-<nombre>/figura/build.mjs`), para importar el
kit con rutas relativas como hacen los ejemplos (`../kit/iso-kit.mjs`). Así la
figura queda con su propio kit y no depende de dónde esté instalada la skill.
Las capturas de las revisiones se guardan en la carpeta desde la que corres el
comando. Cuando una referencia diga `node scripts/...` o
`node examples/...`, esas rutas son relativas a `ANATOMY_DIR`.

Las referencias de `references/` están en inglés técnico, con las firmas
exactas del kit. Léelas igual; lo que le muestres al usuario va en su idioma.

---

Este modo hace figuras como un instrumento pequeño sobre una mesa de trabajo:
una base pesada sobre patas, rieles con reglas graduadas, un carro sobre
bujes, perillas moleteadas, resortes, un reloj comparador cuya aguja se mueve,
tornillos como puntitos. El lector entiende la idea porque reconoce la
máquina. Cada número que muestra la figura sale del mismo modelo que mueve sus
piezas.

Con el modo vienen nueve ejemplos completos: los ocho de abajo y
`examples/push-button/`, la referencia del botón de PDF. Abre el más parecido
antes de empezar. Cada ejemplo sin framework se construye con `node build.mjs`,
que escribe una página HTML independiente junto al script; agrega `--light` para
el tema claro. Las páginas ya construidas no vienen en el paquete para que pese
menos. Para verlas, no las construyas dentro de la skill: copia `kit/`,
`scripts/` y `examples/<nombre>/` a una carpeta temporal, con el mismo árbol, y
corre ahí `node examples/<nombre>/build.mjs` (tarda segundos). Los ejemplos
están en inglés: son material de consulta para ti, no se los entregues al
usuario como resultado.

- `examples/dial-indicator/` es el más chico: un reloj comparador en su base,
  unas 300 líneas en total.
- `examples/desk-computer/` es SVG sin framework: una computadora de escritorio
  con un teclado en el que puedes escribir. La línea escrita aparece en una
  pantalla CRT dibujada en el plano del frente del gabinete, y la imagen se
  reduce a una línea y un punto cuando la apagas. Tiene unos 85 sólidos y 850
  trazos.
- `examples/arcade-cabinet/` es una máquina de arcade vertical sin el panel
  lateral, un Héroe de unos 240 sólidos y 15 cables. Una moneda vuela a la
  ranura, rueda por el canal a la velocidad que alcanza un disco que rueda por
  una pendiente de 30°, activa el alambre del interruptor de monedas y cae en
  la caja; el pulso del interruptor corre tramo a tramo por su cable hasta la
  placa, y el CRT se calienta, se autoprueba y corre un modo de demostración
  dibujado en el plano del monitor inclinado. La palanca se inclina y cierra un
  microinterruptor bajo el panel. Muestra cómo ubicar una cámara para que el
  mecanismo de un corte se mantenga a la vista, una placa cóncava dibujada como
  prisma a lo largo de cualquier eje, piezas móviles reconstruidas en la página
  con el mismo módulo que usa la construcción, y monedas y un cable en vivo
  dibujados en espacios reservados del orden ya asentado.
  `node build.mjs --audit` prueba la geometría.
- `examples/raptor-engine/` es un motor de cohete colgado en un banco de
  pruebas. Sus piezas redondas salen de `kit/lathe.mjs` y sus tubos y su arnés,
  de `kit/tube.mjs`. Se desarma en 11 conjuntos con resortes escalonados y
  reordenamiento de profundidad en cada cuadro. Cada pieza registra su forma
  real, y `node build.mjs --audit` (`kit/audit.mjs`) prueba, en reposo,
  desarmado y en cada cuadro repetido de la explosión, que nada atraviesa nada,
  que cada extremo se apoya en un soporte real, que ninguna curva se pellizca,
  se dobla o cae sobre otra línea, que la pendiente de ningún perfil curvo
  tiembla, y que cada superposición se dibuja en orden de profundidad. Un
  penacho, una onda de choque, salpicaduras y vapor en WebGL se dibujan entre
  el SVG de atrás y el de adelante. Es la referencia para tuberías densas,
  sombreado suave y desvanecidos.
- `examples/ripple-tank/` es una cubeta de ondas escolar sobre patas altas, con
  una pantalla de papel debajo, vista desde 44° de altura. Dos capas WebGL (la
  luz de la lámpara, las sombras y las cáusticas sobre el papel, y los reflejos
  del agua y el vidrio) están alineadas con los planos isométricos y las mueve
  un modelo puro de dispersión y óptica (`model.mjs`); un cambio de frecuencia
  viaja desde los vibradores a través de una textura de historial.
- `examples/test-rig/` es una figura de producción de un sitio real
  (React/Next): un botón de vidrio sobre un carro montado en resortes, una sonda
  en un riel que presiona y jala, y un reloj comparador que mide la
  inclinación. Tiene 53 sólidos y unos 470 trazos.
- `examples/spot-plate/` es otra figura de producción del mismo sitio: seis
  pares de gotas de vidrio sobre una placa de toque, cada par dibujado a partir
  de un solo campo de distancia, así que un par más cerca que `merge` se junta
  en una sola pieza de vidrio. Un abanico de galgas de espesor fija `merge`,
  una hoja por cada separación. Es la referencia para formas que se transforman
  una en otra y para un control que mueve muchas piezas.
- `examples/turning-dial/` es el modo 3D opcional: un dial de combinación que
  gira en 3D real con una pequeña mano robótica encima. Tiene unas 90 piezas en
  vivo con materiales metálicos, un segundo grupo que gira, una bisagra, un dedo
  de tres bisagras que se levanta y una cápsula que se desprende como cuerpo
  libre. Un LED en WebGL, su charco de luz y unas chispas siguen a las piezas
  que se mueven. `stress.mjs`, a su lado, es una mano densa de unas 380 piezas
  en un taller lleno de cosas, que se usa para medir el rendimiento.

El banco de pruebas (test rig) es la vara de calidad del dibujo. El Raptor es
la vara del trabajo con shaders: un efecto WebGL tiene que llegar a su estándar
de render en el espacio del mundo, sin saltos y sin costuras.

## La única idea que importa

**El objeto es la explicación.** No dibujes cajas, flechas y etiquetas. Inventa
una cosa física real y bien hecha cuyo funcionamiento _sea_ el concepto. Así se
tradujeron figuras anteriores:

| Concepto | Objeto |
|---|---|
| Un solo contexto de GPU compartido que atiende muchos lienzos | Un plotter de pórtico: un cabezal que visita 16 pocillos |
| Una clave de caché que se salta el trabajo cuando nada cambió | Una cerradura de pines: cuando todos los pines coinciden, el cilindro gira y no se vuelve a dibujar nada |
| Siete destinos de render con distintos bytes por texel | Una cómoda de siete cajones, cada uno tan hondo como sus bytes |
| Un desenfoque separable (49 × 49 muestras contra 49 + 49) | Un sello de cama de clavos junto a dos peines sobre rieles |
| Un resorte que presiona y se inclina | Un banco de pruebas con resortes, una sonda y un reloj comparador |
| Un perfil de alturas | Un calibre de perfiles presionado contra el borde |
| Una luz que depende de hacia dónde mira la superficie | Un pequeño estudio de foto: lámpara principal y de relleno alrededor de una base giratoria |

Hay dos formas de fallar, las dos vistas en la práctica:

- **Demasiado abstracta.** Placas apiladas, losas flotando o cajas con
  etiquetas no se leen como nada.
- **Demasiado plana y sosa.** Una sola losa grande con un par de líneas no tiene
  volumen, ni piezas, ni nada que descubrir.

La solución para las dos es la misma: una máquina reconocible, hecha de muchas
piezas pequeñas, precisas y con un propósito.

**Toda creación es muy detallada.** Esto vale para cada figura, por pequeña que
sea la idea o el pedido: un explicador rápido sigue siendo una máquina densa y
real, nunca un par de losas. Lo que cambia con el tamaño (paso 1 del flujo) es
hasta dónde lo llevas: una Figura recibe el barrido a 4× sobre su tema y su
mecanismo; un Héroe o una Épica, sobre todo el dibujo.

- **Estudia la cosa real.** Constrúyela como se construye el objeto real: cada
  tornillo, junta, bisel, buje, placa de identificación, cable con su conector,
  escala con sus marcas, y las piezas que sostienen a las piezas.
- **Dos miradas.** A 1× se lee como una máquina clara. A 4×, cada zona todavía
  tiene algo verdadero que encontrar; una cara pelada o una esquina vacía es
  trabajo sin terminar, no calma.
- **Con propósito, nunca ruido.** El detalle viene de piezas que pertenecen al
  mecanismo. Cada una se apoya en otra pieza, termina en un borde y se
  desvanece en lugar de cortarse.
- **Revísalo al final.** Antes de terminar, acerca a 4× (sobre el tema y el
  mecanismo en una Figura, sobre todo el dibujo en un Héroe o una Épica) y
  agrega las piezas reales que falten donde una zona se vea vacía.

## Flujo de trabajo

Trabaja en este orden. Escribe el concepto y la lista de piezas antes de
cualquier geometría. Ahí se decide la mayor parte de la calidad.

1. **Mide el tamaño antes de empezar.** Di el tamaño antes que cualquier otra
   cosa, y dile al usuario más o menos cuánto va a tardar cuando el nivel lo
   pida.
   - **Figura**: un mecanismo, 40 a 80 piezas, SVG con una capa WebGL como
     máximo. Di el tamaño y constrúyela sin preguntar. No le des un tiempo al
     usuario, porque una Figura muchas veces se termina en bastante menos de una
     hora. Para las revisiones de avance de abajo, calcula hasta una hora.
   - **Héroe**: un objeto denso, varias capas WebGL o un tema en 3D, 80 a 150
     piezas. Unas 2 a 4 horas. Dilo y constrúyelo, salvo que el usuario haya
     pedido algo rápido.
   - **Épica**: un vehículo, un edificio o una planta completa con muchos
     sistemas en movimiento, o el modo 3D en más de un tema. 6 horas o más. No
     la empieces. Da la estimación, propón una versión Héroe que conserve el
     núcleo de la idea y di qué agregaría la versión completa. Construye la
     Épica solo si el usuario la elige.
   - Sea cual sea el tamaño, ten una página que funcione y se abra en el
     navegador dentro de la primera hora, y profundiza a partir de ahí. Corre
     `date` al empezar y en cada paso, y cuando un paso pase del doble de su
     parte de la estimación, dile al usuario cómo va y qué falta.
2. **Primero la verdad.** Junta los números y el comportamiento reales de lo
   que se explica: tamaños, cantidades, umbrales, curvas. La lectura, el
   movimiento y el pie de la figura tienen que ser ciertos. Si puedes, escribe
   el modelo como un módulo puro y pequeño, como `rig.ts` en el ejemplo del
   banco de pruebas, y mueve todo desde ahí.
3. **Inventa el objeto.** Elige una máquina, herramienta, instrumento o mueble
   cuyo mecanismo corresponda uno a uno con el concepto. Di en una oración qué
   se mueve y qué significa ese movimiento. Nunca copies una imagen de
   referencia: toma su acabado, no su objeto.
4. **Lista de piezas.** Escribe al menos 40 piezas (40 a 80 para una Figura, 80
   a 150 para un Héroe, más para una Épica), agrupadas: base (placa, patas,
   ranura, tornillos de esquina, placa de identificación, regla), estructura
   (postes, rieles, barras del marco, topes), mecanismo (carro, bujes,
   resortes, émbolo, aguja), controles (perilla moleteada, tornillo de
   mariposa, corona) y el tema mismo, que es la única pieza iluminada. Cada
   pieza se apoya en otra. `references/craft.md` tiene un vocabulario de piezas
   con recetas.
5. **Planea el mundo.** Usa unidades de mundo de más o menos 1 px del objeto
   real: x e y en el piso, z hacia arriba. Traza los planos como rectángulos
   redondeados `{x, y, w, d, r}` y círculos. Elige la cámara: azimut de 45° por
   defecto, de 35° a 60° para mostrar el lado largo, elevación de 30° (más alta,
   como los 44° de la cubeta de ondas, para mirar dentro de algo abierto).
   Luego ajusta con `fitProjection(points, width, height, { pad, azimuth })`.
6. **Construye la geometría una sola vez.** Precalcula cada trazo estático en un
   módulo de geometría con el kit: `slabOf`, `cylinder`, `extrude`,
   `planOutline`, `topTicks`, `knurl`, `coil`, `radialTicks` y demás. Las
   piezas redondas en cualquier eje (campanas, bridas, válvulas, actuadores)
   salen de `kit/lathe.mjs`, y los tubos y cables, de `kit/tube.mjs`. Las piezas
   móviles se construyen una vez en su posición de reposo y se mueven con
   `translateAlong`. Solo se reconstruyen en cada cuadro las piezas cuya forma
   cambia.
7. **Pinta de atrás hacia adelante y de abajo hacia arriba.** Ordena las piezas
   repetidas con `depthOf`. Parte en una mitad de atrás y otra de adelante todo
   lo que envuelva a otra pieza: los resortes alrededor de una varilla, las
   barras de un marco alrededor de un carro. Una pieza móvil se dibuja en el
   lugar donde está físicamente. Ver "Painter's order" en
   `references/craft.md`. Cuando una figura ya tiene tubos, cables y piezas
   redondas, deja de ajustar las claves a ojo: registra la forma de cada
   elemento al ponerlo en `A.recorder(P, { order, spring })`, deja que
   `A.settle(R, P)` mida la profundidad real donde dos elementos se superponen
   y fije las claves, y termina la construcción con `A.auditOrExit(R, P)`.
   Traza el recorrido de los tubos antes de dibujarlos: puertos reales en los
   dos extremos, tramos a lo largo de la estructura, cruces en las rectas,
   collarines que interrumpen el tubo (`references/craft.md`, sección 8).
   Registra la forma real de lo que dibujas: una forma sustituta que calle a la
   auditoría es un error, y la auditoría la hace fallar. Una varilla que sale
   de un prensaestopas es una sola varilla de `G.rodOut`, registrada con
   `A.slide`.
8. **Enmárcala.** Pon la figura en una tarjeta: `Fig n` arriba a la izquierda,
   un título corto arriba a la derecha, la pista de interacción abajo a la
   izquierda y la lectura en vivo abajo a la derecha. Las claves de la leyenda y
   un pie de figura verdadero van debajo de la tarjeta, y las palabras quedan
   fuera del dibujo, salvo como mucho una etiqueta grabada diminuta.
9. **Dale vida.** Usa un movimiento tranquilo basado en el tiempo: seguimiento
   exponencial o resortes reales. Un recorrido automático se repite cuando nadie
   la toca. La figura responde al puntero y al teclado, se detiene cuando sale
   de la pantalla y se queda quieta con movimiento reducido. Escribe atributos
   sobre referencias y no vuelvas a renderizar en cada cuadro. Ver
   `references/motion.md`.
10. **Revisa como un crítico.** El dueño encuentra fallas acercando la imagen,
    así que acércala tú primero. Lee cada PNG que generes.
    - Captura escritorio, teléfono (390 de ancho), hover y varios momentos del
      movimiento con `scripts/capture.mjs`; usa `scripts/drive.mjs` para
      secuencias, la pose desarmada y la versión sin WebGL (`--no-webgl`).
    - **Corre la auditoría hasta cero.** Vale la pena en cualquier figura, y con
      tubos, cables o piezas redondas es obligatoria: `node build.mjs --audit`
      tiene que terminar en `audit passed`, con cada
      línea de falla en 0: separación en reposo, desarmado y a medio vuelo,
      terminales, extremos sueltos, dobleces, superposición consigo mismo,
      amontonamiento (también contra sólidos delgados), formas sustitutas,
      soporte, temblor, sillas y orden de profundidad. Arregla un
      entrelazamiento en la geometría, nunca con un sesgo de clave.
    - **Corre la revisión de líneas hasta cero.** La auditoría nunca ve el
      marcado de las líneas.
      `node "$ANATOMY_DIR/scripts/lines.mjs" page.html --out shots/lines.png`
      (también en la página `-light`, y en cada pose de reposo con la acción
      `["lines"]` de `drive.mjs`) tiene que imprimir `line ends: 0`: cada
      junta, raya, nervio, marca y aguja termina en un trazo, un punto o un
      contorno. Lee el PNG con los anillos.
    - **Acercamientos a 4× de cada unión en los dos temas** (construye también
      con `--light`), armado y desarmado: cada brida, T, codo, abrazadera,
      válvula, fuelle, banda, silla, rótula y cruce; cada cuerpo curvo (sin
      escalones de tono); cada lugar donde termina una textura (en un borde o
      desvaneciéndose); las caras planas de las cajas con sus juntas; cada
      manguera con textura en una unión de tramos; cada varilla que se desliza,
      en reposo y en su carrera completa; y cada ventana con texto o shader
      dentro.
    - **Shaders:** una hoja de contactos en cámara lenta con `["slow", 0.05]` a
      lo largo de cada transición; nada salta, no hay cambios bruscos de color,
      los bordes dan 0. En el tema claro, registra también la tinta de cada
      cuadro en cada transición (tiene que seguir a la luz de forma monótona) y
      recorta donde la tinta toca los trazos, a 8× a 16× (`references/verify.md`,
      "Light-theme shaders").
    - Pon tu PNG junto a los ejemplos y pregúntate: ¿es al instante un objeto
      real, lleno de piezas pequeñas con volumen, con cada línea terminando en
      algo? ¿Está muy detallado a 1× y sigue premiando la vista a 4×, sin caras
      peladas ni esquinas vacías? Repite hasta que la respuesta sea sí. Lista de
      revisión: `references/verify.md`.

## Preparación

El kit está en `kit/`:

| Archivo | Para qué sirve |
|---|---|
| `kit/iso-kit.ts` | Todo el núcleo en un archivo: cámara, sólidos, una biblioteca de piezas, un renderizador de SVG a texto, constructores de tarjeta y de página, y el CSS (`ISO_CSS`). Cópialo en un proyecto de TypeScript. |
| `kit/iso-kit.mjs` | El mismo núcleo compilado a ESM simple, para scripts de Node. Impórtalo directo. |
| `kit/iso.css` | `ISO_CSS` escrito en un archivo. Impórtalo una vez y pon `class="iso"` (más `data-theme="light"` para el tema claro) en un contenedor o en `<body>`. |
| `kit/react/draw.tsx` | Componentes de React seguros para el servidor: `Solid`, `Line`, `Wire`, `Dots`, `FaceText`, `IsoFigure`, `Plate`. |
| `kit/react/live.tsx` | Hooks `"use client"`: `useReadout`, `useLoop`, `useEased`, `useInView`, `useStillness`, más `spring` y `follow`. |
| `kit/lathe.mjs` | Piezas redondas en cualquier eje: `frameAlong`, `lathe` (el sombreado suave se activa solo en cualquier perfil con un nudo suave), `solidOf`, `disc`, `ringBand`, `sphereOf`, `saddleOf`, `bandsOf` (un cuerpo curvo cortado en bandas que se ordenan por profundidad y comparten una superficie, con un solo contorno de `sidesOf`), arcos visibles, nervios y círculos de pernos sobre superficies redondas (`ribsOf` y `dotsOf` aceptan `fade`, `ribsOf` acepta `seams`), `rodOut` para una varilla que sale de un prensaestopas, y `fillet` para recorridos de tubos. |
| `kit/tube.mjs` | `tubePieces` parte un tubo o cable 3D en tramos que se ordenan por profundidad (con `breaks`, `gaps` bajo collarines y abrazaderas, tapas elípticas en los extremos, y `rings` para una malla, un corrugado o un forro que sigue la sección a través de cada unión), y `tubeSvg` dibuja uno; `crossingsOf` encuentra dónde un recorrido pasa por una abrazadera, `runsOf` los tramos dibujados. Sus rellenos `.tb-*` están en `ISO_CSS`. |
| `kit/audit.mjs` | Prueba la geometría. `recorder(P, { order, spring })` junta los elementos, las formas (cuerpos torneados, losas, prismas, cajas, esferas, tubos, almohadillas cortadas por su pieza) y los recorridos a medida que los helpers los dibujan; `settle(R, P)` lanza rayos por cada par que se superpone para obtener la profundidad real, en reposo, desarmado y en la explosión repetida, y fija las claves de pintado (`overlapsOf`, `orderKeys`); `auditOrExit(R, P)` es el gancho de `--audit` que corre todas las revisiones (`clearances`, `solidClearances`, `terminals`, `looseEnds`, `supports`, `folds`, `selfOverlaps`, `crowding` con sólidos delgados como líneas, `coverage` para formas sustitutas, `wobble`, `seats`, `depthOrder`) y sale con error ante cualquier problema. `A.slide` registra una varilla que sale de un prensaestopas. `references/kit.md`, sección 12. |
| `kit/gl.mjs` | La capa WebGL para shaders dentro del dibujo: `GLSL_ISO` (la cámara en GLSL, con `rayOf` y `pixelOf`), `glCamera(P)`, `glLayer(...)`, y las envolventes de JS `smooth`, `burst` y `settle`. Para figuras 3D, `GLSL_TURN` y `glslPose(name)` llevan puntos del mundo a un grupo en movimiento y enmascaran un lienzo delantero con `coverOf`. |
| `kit/turn.mjs`, `kit/turn-build.mjs`, `kit/turn-audit.mjs` | El modo 3D opcional. `turn-build.mjs` tiene `turning(P, { recorder })`: grupos (giro, deslizamiento, bisagra, libre), capas en vivo, piezas convexas con materiales, y `T.build`. `turn.mjs` es el motor en ejecución: `TURN.mount`, el controlador, `TURN.cover`, `TURN.poseUniforms` y `TURN_CSS`. `turn-audit.mjs` tiene `orbitOrExit`, la auditoría de órbita en cada ángulo de giro y en cada clip de movimiento. `references/3d.md`. |
| `scripts/capture.mjs` | Capturas con Chrome sin ventana, acercamientos y revisiones de la consola, con WebGL encendido. Se corre con `node`. |
| `scripts/drive.mjs` | Chrome sin ventana con guion y WebGL: mover, hacer clic, teclas, cámara lenta, esperar hasta, evaluar, capturas y hojas de contactos que detectan saltos; `--no-webgl` y `--preload`. |
| `scripts/lines.mjs` | La revisión de extremos de línea sobre una página construida, en Chrome sin ventana: cada línea de textura tiene que terminar en un trazo, un punto o un contorno. Marca las fallas con anillos con `--out`; sale con 1 si hay alguna. |
| `scripts/inline-kit.mjs` | `kitScript()`, `glScript()` y `turnScript()` devuelven el kit, la capa WebGL y el motor 3D como código fuente para meterlo en una página independiente. |
| `scripts/turn-check.mjs`, `scripts/turn-bench.mjs` | Figuras 3D: fidelidad contra los constructores del kit, revisión del orden con búfer z, saltos de píxeles, extremos de línea en 24 ángulos y tiempos por cuadro en el navegador; tiempo de CPU en Node por tipo de pieza. |
| `scripts/print.mjs`, `scripts/print-sheet.mjs` | Hojas para imprimir: congelan poses de una página construida como imágenes vectoriales y las acomodan en un PDF A4 o Carta en tres formatos (póster, plano, detallado). `references/print.md`. |

Elige el camino que le queda al proyecto:

- **HTML independiente, un SVG estático, un post de blog o cualquier sitio que
  no use React.** Escribe un script de construcción de Node como
  `examples/dial-indicator/build.mjs`. Importa `kit/iso-kit.mjs`, arma textos
  con `solidSvg`, `lineSvg`, `dotsSvg`, `wireSvg` y `faceTextSvg`, los envuelve
  con `figureSvg` y `plateHtml`, y escribe la página con
  `pageHtml({ script: kitScript() + live })`, o `kitScript() + glScript() +
  live` cuando tiene un shader. Para un archivo `.svg` suelto usa
  `figureSvg({ standalone: "dark" | "light" })`, que incluye los estilos.
- **React o Next.js.** Copia `kit/` en el proyecto (por ejemplo en
  `components/iso/`). Deja la geometría en módulos `.ts` simples, construye el
  arte estático en un componente de servidor con los componentes de
  `draw.tsx`, y pásalo como props de elementos a un solo componente
  `"use client"` en vivo que mueve las cosas. `references/react.md` explica la
  división y una trampa con páginas grandes.

## Reglas de oficio (versión corta)

Estas son las reglas que separan una figura bien hecha de un diagrama.
`references/craft.md` tiene el razonamiento completo y las recetas.

- **Sólidos, no estructuras de alambre.** Cada pieza se rellena del color del
  papel y se pinta en orden, así que lo de adelante tapa lo de atrás. Nada de
  aristas que se transparentan ni líneas ocultas punteadas.
- **Deja que el kit sombree.** `extrude` devuelve cuatro tonos de costado según
  hacia dónde miran, más una cara superior más clara. Úsalo para todo lo que
  tenga altura, y usa `flat` solo para pisos e incrustaciones de menos de 1
  unidad de grosor.
- **Jerarquía de tonos.** La base y las patas son `lo`, la estructura es `mid` y
  el tema es `hi`. Exactamente un acento es `lit` (blanco en el tema oscuro,
  negro en el claro): la pieza que el lector debe mirar. Las ranuras son
  `faint`, las marcas menores `lo`, las mayores `mid` y la marca del cero `hi`.
  Usa color solo cuando el color es el tema, como los canales rojo, verde y
  azul.
- **Detalle pequeño y preciso, nunca ruido.** Usa biseles de 0.4 a 1.6, ranuras
  a 3 a 5 de un borde, tornillos como puntos de 0.4 a 0.55 con un anillo en las
  esquinas de las placas, moleteado en las perillas, marcas de regla cada 4 a 5
  unidades con una mayor cada 5, y una placa de identificación con tres líneas.
  Cada detalle pertenece a una pieza.
- **Las líneas se resuelven.** Cada línea termina en algo: una cara, otra línea
  o un punto terminal. Los conectores son `Wire` cuyos puntos terminales caen
  sobre objetos. No hay líneas de referencia, globos, flechas de cota ni
  etiquetas flotando en el aire.
- **Ningún tubo ni cable atraviesa nada.** Ni otro tubo, cable o sólido, en
  reposo, desarmado ni en ningún cuadro de la explosión. Deja unos 1.5 radios de
  separación con todo, salvo con la conexión propia de la línea; lleva las
  líneas junto a la estructura en lugar de cruzar la cara del tema; e
  interrumpe el tubo donde lo envuelva una brida, banda, fuelle, abrazadera o
  válvula. Las piezas se tocan al ras, tangentes o con el borde sobre la
  superficie, nunca hundidas: la cara trasera de una brida se apoya en su
  puerto (sobre una almohadilla de silla, `G.saddleOf`, cuando el puerto es
  curvo), una derivación sale de una T con rótula, y cada extremo, también
  desarmado, termina en una brida, un acople, la carcasa de un conector o un
  punto terminal.
- **Cada cruce se dibuja en su orden real de profundidad.** Donde dos elementos
  se superponen en pantalla, el más cercano va encima, y eso lo prueban
  `A.settle` y la auditoría, no el ojo. Las líneas se cruzan en las rectas, bien
  separadas en profundidad: una curva, un extremo o una abrazadera que cae
  sobre el contorno de otra línea se lee como una unión (una varilla, un
  tirante, un poste o un riel cuentan como línea: el último tramo de un tubo
  nunca corre a lo largo de uno en pantalla), un tramo que apunta hacia quien
  mira y luego gira se pellizca en una V (sal de ese puerto con un codo de
  rótula), y un recorrido nunca regresa sobre sí mismo en pantalla. Un par que
  no se puede ordenar está entrelazado, y la solución es un corte o un contacto
  tangente, nunca un sesgo.
- **Las superficies curvas se sombrean suave, nunca en escalones.** Marca como
  suaves los nudos curvos (`[s, r, 1]`) y `lathe` los sombrea con una sola curva
  monótona que también dibuja el contorno; dale a cualquier cuerpo curvo más
  grande que una conexión un perfil analítico con `smooth: { slope }`, corta los
  cuerpos largos con `G.bandsOf` y usa `G.sphereOf` para las esferas. Las
  bandas de tono se afinan hasta desaparecer en lugar de terminar en un corte
  recto, y las juntas van bajo el contorno (`inner`).
- **Una textura termina en un borde real o se desvanece.** Nervios, círculos de
  pernos, líneas, juntas y ranuras nunca se detienen a mitad de una superficie,
  plana o curva: `ribsOf` y `dotsOf` aceptan `fade` (dibuja los nervios
  desvanecidos con `fadedSvg`), una fila de nervios termina en sus juntas
  (`ribsOf(…, { seams: true })`), una junta o soldadura en una caja da la vuelta
  a sus esquinas (`k.sideSeam`, como `inner` de la losa), una línea en una cara
  va de borde a borde, las rejillas son ranuras cerradas, las marcas cuelgan del
  borde de una regla, una línea suelta que tiene que detenerse se desvanece con
  `fadeLineSvg`, y una fila cuyas piezas miran hacia arriba (agujeros sobre un
  anillo) se ve completa (`all: true`). Una textura en un tubo (malla,
  corrugado, forro) sigue su sección y atraviesa cada unión de tramos:
  `tubePieces(…, { rings })`, nunca un trazo punteado por la línea central. El
  brillo y la sombra de un tubo siguen sobre sus tapas y a través de cada unión.
  Solo las líneas que representan texto impreso, la cola de una aguja y la punta
  de un puntero pueden detenerse sobre una cara pelada, marcadas como `free`.
- **Los shaders nunca saltan ni se cortan.** Cada uniforme sigue una envolvente
  con ataque y caída, los cambios de fase son fundidos que mueve la cantidad
  física, cada término llega a cero antes de cualquier límite o borde del
  lienzo, y el efecto vive en el espacio del mundo con la cámara de la propia
  figura (ver abajo).
- **Lo que va en las caras les queda.** El texto que muestra una máquina cabe
  en su ventana con la cadena más ancha y se recorta a ella; lo que se ve por
  una abertura se recorta con la abertura y con su propio plano, y se dibujan
  las paredes del hueco.
- **Volumen.** Dales grosor real a las cosas, haz que se apoyen en otras cosas, y
  pon un halo suave bajo la base y bajo todo lo que esté levantado.
- **Composición.** Centra la figura y deja que llene más o menos del 55% al 65%
  de la tarjeta. Mantén la misma escala en un conjunto de figuras y asegúrate de
  que se siga leyendo a 390 px de ancho.

## WebGL dentro del dibujo

Usa un shader solo para lo que las líneas no pueden dibujar: fuego y escape,
agua y cáusticas, luz real de lámpara, brillo, vapor. Las piezas siguen siendo
SVG. Las reglas básicas vienen de la primera figura con shader, cuyo cambio de
color entre fases se veía cortado en lugar de fundido:

- **Tres capas.** Un SVG de atrás tiene lo que el efecto cubre, el lienzo tiene
  el efecto (`pointer-events: none`) y un SVG de adelante tiene lo que lo cubre.
  Divide una pieza, o el efecto, cuando está de los dos lados.
- **Espacio del mundo, la misma cámara.** Construye cada punto del shader con
  `onFloor`, `onWallX` y `onWallY`, o recorre el rayo del píxel
  `rayOf(vb) + t·towardViewer()`. Dimensiona todo en unidades del mundo por
  `uK`. Todo lo que está sobre un plano coincide exactamente con las líneas SVG
  de ese plano.
- **Nada salta.** Cada uniforme sigue una envolvente con ataque y caída (`burst`
  del kit para eventos, `settle` para niveles). Los cambios de fase son fundidos
  en los que el color cambia de forma continua con la cantidad física, y un
  desvanecido de salida solo se oscurece.
- **Sin cortes duros.** Cada término llega a cero antes de cualquier `if`,
  límite o borde del lienzo, y antes de cualquier borde de celda de un ruido
  celular.
- **Visto por una abertura, enmascarado dos veces.** Lo que está detrás de una
  ventana o un hueco se enmascara en su propio plano y con la abertura en el
  plano de la cara, multiplicado (`references/webgl.md`, sección 5).
- **Mezcla.** Usa `tonemap()` y tramado. En el tema oscuro, un lienzo que solo
  suma luz usa salida premultiplicada con `mix-blend-mode: screen`, y uno que
  también tiene que oscurecer (el agua de la cubeta de ondas) se queda con la
  mezcla normal.
- **El tema claro también se entrega, y sus shaders se diseñan para el papel.**
  Usa alfa premultiplicada normal, nunca `screen`. Escribe el color que debe
  mostrar el papel y despeja la tinta. Un brillo es un cuerpo saturado con un
  centro pálido, un borde de color y un piso de alfa, nunca un color del tema
  oscuro oscurecido: eso le dio al Raptor su "humo de tinta roja".
  - Lo que recibe la luz toma un tinte, y la cavidad que la contiene recibe un
    fondo físico más oscuro (hollín, refractario, profundidad del agua).
  - Los cuerpos calientes siguen una sola tabla de tinta de cuerpo negro,
    compartida con la versión sin WebGL.
  - La tinta solo crece con la luz: desvanece la tinta terminada una sola vez,
    nunca término por término.
  - La tinta termina en el borde interior de cada trazo.
  - Mide la tinta en cada cuadro. `references/webgl.md`, sección 8, tiene las
    recetas y las fallas que encontraron los revisores.
- **Mesura.** Limita la densidad de píxeles a 1.5 y renderiza solo mientras el
  efecto esté activo y en pantalla. Con movimiento reducido se muestra un solo
  cuadro quieto, y el SVG se tiene que leer igual sin WebGL.

Lee `references/webgl.md` antes de escribir cualquier shader.

## 3D: figuras que giran (beta)

El 3D es una opción, como WebGL. Úsalo cuando la idea es una pieza que se
mueve en profundidad: un dial o una base que gira, dedos que se flexionan, una
pieza que se desprende y cae. El resto de la figura sigue siendo arte estático
del kit.

Está en beta: el motor está probado en su ejemplo y en una figura de prueba,
todavía no en una figura de producción. Gira un tema a la vez y deja quietas
las cosas que lo rodean. Una figura chica corre a 60 fps; una mano densa de 380
piezas que se flexiona midió unos 20 fps a 1440 y de 13 a 15 fps en un perfil de
teléfono (390 px, CPU 4 veces más lenta) en una máquina muy cargada.

- **Las piezas en vivo son el mismo dibujo del kit.** En cada cuadro, las
  primitivas convexas del kit (prismas, redondos, domos, esferas con caras
  planas, piezas torneadas, tubos) se vuelven a proyectar y a sombrear con las
  reglas del kit. Un giro de θ es el kit dibujando con azimut `a − θ`.
- **El orden sale de planos separadores.** Los pares del mismo grupo reciben un
  plano fijo en el grupo, los pares en eslabones distintos uno fijo en su marco
  común, y el resto se resuelve en cada cuadro. La auditoría prueba que no hay
  ciclos en ningún ángulo ni en ningún cuadro de clip.
- **Los contactos son al ras, tangentes o de borde sobre plano.** Las
  articulaciones son discos de nudillo coaxiales en el grupo hijo que tocan el
  eslabón del padre; si no, la auditoría declara suelto todo el grupo hijo.
  Ninguna línea en vivo cruza dos grupos que se mueven: un cable pasa una
  articulación con un clip de cada lado, o llega a la base giratoria por un
  anillo colector en el centro.
- **Los tubos en vivo se doblan en planos casi horizontales o dentro de las
  conexiones, y nunca apuntan a lo largo de la vista.** Una curva necesita
  R ≥ 2r / sin²(e − θmax), donde θmax incluye el rango de inclinación de cada
  bisagra en la que va montada: 8r es el límite en plano, y en una bisagra de
  ±12° es 21r. Cada recorrido va de una superficie de montaje a otra, con sus
  puertos en `gaps`. Eso se cumple en cada ángulo y en cada pose.
- **Los materiales reasignan la rampa.** Oro, cromo, acero, metal de cañón,
  caucho, latón y cobre tienen cada uno un juego claro y uno oscuro; los tonos
  siguen saliendo de hacia dónde mira la cara.
- **Los grupos libres se desprenden sin saltos.** Las piezas coaxiales son
  imágenes fijas con texturas que giran.
- **Los shaders siguen el movimiento.** Ánclalos a un grupo con
  `controller.anchor` o `toGroup`, tapa un lienzo delantero con `coverOf`, y
  deja los efectos del mundo (humo, chispas que caen, aceite en la mesa) fuera
  del espacio del grupo.
- **Revisa con `--audit`** (`turn audit passed`) y `scripts/turn-check.mjs`
  (`--fidelity`, `--order`, `--pops`, `--lines`, `--perf`). Itera con
  `--quick --only=…`. Solo una corrida completa prueba la figura, y tarda de 15
  a 20 minutos para 30 piezas, así que córrela en segundo plano.

Lee `references/3d.md` primero.

## Hojas para imprimir (A4)

Cuando el usuario quiera la figura en papel (una hoja de repaso, un póster, un
PDF, una hoja A4 o Carta), imprímela desde la figura terminada en lugar de
volver a dibujar. Escribe un `sheet.mjs` junto a la construcción: las poses que
se van a capturar como acciones de `drive.mjs`, las piezas como selectores CSS
sobre el SVG en vivo, y los textos, cada uno fiel al modelo. Luego corre
`node "$ANATOMY_DIR/scripts/print.mjs" sheet.mjs --format all --png` y lee cada
página. Los títulos fijos de las hojas ("Cómo funciona", "Piezas",
"Especificaciones"...) ya salen en español.

- **poster** (el formato por defecto): una página, el nombre en grande, la
  pregunta, números grandes, la figura con pines numerados y cada pieza con una
  línea.
- **drawing**: una página, un plano técnico con lista de piezas,
  especificaciones, un recuadro de detalle y una tira de pasos con las piezas
  que trabajan iluminadas.
- **detailed**: de 2 a 4 páginas, según la máquina: una vista general con pines
  y acercamientos redondos; "Cómo funciona", con cada paso como una imagen
  grande iluminada (seis por página, el porqué en el último espacio); y para
  figuras complejas, una página de "Conjuntos" con hasta cuatro acercamientos
  grandes de grupos de piezas (`assemblies` en la especificación). Una figura
  simple se queda en 2 páginas; `maxPages` pone el tope.

Ofrece los tres cuando el usuario no haya elegido uno. Cuando la página muestre
una figura que tiene PDF, pon un enlace a él en la tarjeta con
`pdfButton(href)` de `kit/pdf-button.mjs` dentro del cuerpo de la placa (ver
`examples/push-button/build.mjs`); primero imprime, luego vuelve a construir la
página. `examples/raptor-engine/sheet.mjs` y `examples/arcade-cabinet/sheet.mjs`
son las referencias. Lee `references/print.md` primero.

## Referencias

Léelas cuando las necesites:

- `references/craft.md`: el estilo a fondo, con el vocabulario de piezas con
  código, tablas de tonos, patrones de orden de pintado, piezas redondas, tubos
  y arneses, vistas explotadas, pantallas en caras, y los errores que hicieron
  que rechazaran figuras. Léelo antes de diseñar.
- `references/kit.md`: la API, con firmas y ejemplos.
- `references/motion.md`: el comportamiento en vivo (ciclos, resortes,
  recorridos, puntero, teclado, accesibilidad, movimiento reducido), más
  envolventes para eventos únicos, vistas explotadas, reordenamiento de
  profundidad y armado, en JS simple y en React.
- `references/react.md`: la división servidor/cliente de React y Next.js, las
  props de elementos y la trampa del aviso de claves con cargas grandes.
- `references/verify.md`: los comandos de `capture.mjs` y `drive.mjs`, la
  lista de revisión (incluidos los shaders) y las fallas comunes.
- `references/webgl.md`: los shaders dentro del dibujo: cuándo vale la pena
  uno, el orden de las capas, el contrato de la cámara, el recorrido de rayos
  en la cámara isométrica, la API completa con una página mínima, las reglas de
  oficio con los errores que las enseñaron, el tema claro (tintas sobre papel,
  recetas por fenómeno, las fallas de los revisores) y cómo revisarlos.
- `references/walkthrough.md`: cómo se diseñó el banco de pruebas, paso a paso,
  del concepto al código.
- `references/3d.md`: el modo 3D opcional: grupos y poses, capas en vivo,
  piezas convexas y sus reglas, materiales, grupos libres, cadenas de bisagras,
  orden de pintado, objetos estáticos alrededor de una base giratoria, shaders
  que siguen el giro, la auditoría de órbita, revisiones en el navegador,
  rendimiento y límites.
- `references/print.md`: hojas A4 o Carta para imprimir a partir de una figura
  construida: los tres formatos, la especificación de `sheet.mjs` (poses,
  piezas como selectores, foco, ocultar, recortes, imágenes para WebGL) y cómo
  revisar el PDF.

La publicación en la galería comunitaria del proyecto original no viene en este
paquete (ver `CAMBIOS.md`).
