# Cambios respecto a las originales

Qué se tradujo y qué se cambió en cada skill. Las originales sin cambios están
en los repos que lista [CREDITOS.md](CREDITOS.md).

## En todo el paquete

| Original | Ahora | Por qué |
| --- | --- | --- |
| Cinco skills separadas, cada una con su `SKILL.md` | Una sola skill: un `SKILL.md` de entrada que elige el modo y un `MODO.md` por modo en `modos/` | Que se instale de una vez, y que Claude lea solo el modo que toca (no las cinco a la vez) |
| Comandos `/chief-of-staff`, `/teach`, `/last30days` | `/skills-secretas <modo>` (`jefe`, `anatomia`, `profe`, `psicologia`, `30dias`), o pedirlo en lenguaje natural | Un solo comando sin choques de nombres |
| Instrucciones en inglés | Cada `MODO.md` traducido al español neutro, con tuteo, y la regla de responder en el idioma del usuario (español por defecto) | Que lo use cualquier persona que hable español |
| Archivos `agents/openai.yaml` (metadatos para Codex) | No se incluyen | Sirven para otra herramienta y aquí nadie los lee |
| Rayas largas (U+2014) en textos y código | En el texto, reemplazadas por coma o guion; en el código, por el escape `\u2014`, que da exactamente el mismo valor | Regla de estilo de Aldush Media; se comprobó que el código quedó idéntico (mismo árbol de sintaxis) |
| Licencias en cada repo | Los cinco textos completos en `licencias/` y los autores en `CREDITOS.md` | Lo exige la licencia MIT |

## 1 · Jefe de equipo (Chief of Staff)

| Original | Ahora | Por qué |
| --- | --- | --- |
| Solo se activaba con su comando (`disable-model-invocation`) | Se activa solo si el usuario lo pide de forma explícita, y confirma la meta antes de lanzar el primer agente | La skill combinada no puede apagar la activación de un solo modo; así se conserva la intención del original |
| El wiki va donde se acuerde con el usuario | Igual, y propone una carpeta propia (`wiki-<meta>/`) | Que no se mezcle con los archivos del modo Profe |
| Ejemplos de programación (lint, CODING_STANDARDS, logs) | Se conservan y se suman los equivalentes para contenido (plantillas, guía de voz, métricas) | Que sirva a un creador sin perder el sentido original |
| Marcado como `in-progress` | Marcado como beta en el modo y en `COMO_USAR.md` | Para no prometer más de lo que el autor promete |
| Todo el trabajo va en subagentes, sin plan B | Si el entorno no deja lanzar agentes, hace el trabajo él mismo y lo avisa en una línea | Que no se trabe (salió en la prueba) |
| Los reportes de subagentes se citan, pero no dice dónde quedan | Se guardan tal cual en `fuentes/` dentro del wiki, con fecha; las decisiones del chat van a una página con fecha | Que las citas sigan apuntando a algo después de compactar la conversación |
| Solo dice cómo citar código y métricas | También cómo citar un entregable sin git (archivo y fecha), y que las páginas de reglas van en presente | Para metas de contenido |
| "Propón horarios" | Los propone y solo los crea si el usuario dice que sí, preguntando su zona horaria | Que no programe nada por su cuenta |
| Pensado para sesiones largas | Se ajusta al tamaño de la meta y cierra con qué se entregó y qué sigue | Para metas chicas, como un calendario de una semana |

## 2 · Anatomía (Anatomy)

| Original | Ahora | Por qué |
| --- | --- | --- |
| `SKILL.md` en inglés | `MODO.md` traducido completo | Traducción |
| Referencias técnicas (`references/`) en inglés | Se quedan en inglés | Son instrucciones internas para Claude con firmas y comandos exactos; traducirlas podía romper referencias cruzadas. Todo lo que ve el usuario sale en español |
| Rutas relativas a la raíz del repo (`node examples/...`) | Rutas relativas a la carpeta del modo, con `ANATOMY_DIR` | La skill ahora vive en `modos/2-anatomia/`; los scripts ya encontraban el kit por su propia ruta |
| Publicación en la galería comunitaria del autor (`scripts/publish.mjs`, `scripts/session.mjs`, `scripts/fingerprint.mjs`, `references/publish.md`) | No se incluye | Lee tus conversaciones de Claude Code y sube tu prompt a un pull request público en el repo del autor; además cambia tu configuración global de git |
| Páginas y PDFs de ejemplo ya generados (unos 25 MB) | No se incluyen; se regeneran con `node examples/<nombre>/build.mjs` | El paquete pasa de 27 MB a 1.9 MB y los ejemplos se rehacen en segundos |
| Tests, evals y archivos de GitHub del repo | No se incluyen | Son para desarrollar la skill, no para usarla |
| Títulos fijos de las hojas para imprimir en inglés ("How it works", "Parts", "Specification", "Not to scale", "Assemblies") | En español ("Cómo funciona", "Piezas", "Especificaciones", "Sin escala", "Conjuntos"), y el pie dice "Anatomía" | Son textos que ve quien recibe el PDF |
| Páginas con `lang="en"` fijo y botón "Open the printable PDF" | `lang="es"` por defecto, con la opción `lang` en `pageHtml` para otro idioma, y "Abrir el PDF para imprimir" | Lo mismo, y ayuda a la accesibilidad |
| Las figuras importan el kit desde la carpeta de la skill | El `MODO.md` pide copiar `kit/` y `scripts/` a la carpeta de la figura, y construir los ejemplos en una copia | Que la figura sea del usuario y no se escriba dentro de la skill instalada (salió en la prueba) |
| "Vienen ocho ejemplos" (hay nueve) | Nombra los nueve, y aclara que los ejemplos están en inglés y son de consulta | Salió en la prueba |
| Mensajes de los scripts en inglés | Se quedan en inglés; Claude se los cuenta al usuario en español | Las instrucciones dependen de esos textos exactos (`audit passed`, `line ends: 0`) |

## 3 · Profe (Teach)

| Original | Ahora | Por qué |
| --- | --- | --- |
| Solo se activaba con `/teach` | Se activa al pedir «enséñame...» o «quiero aprender...» | Lo pide el uso combinado; el modo sigue siendo el mismo |
| Usa siempre el directorio actual como espacio de trabajo | Lo usa si ya es un espacio de este modo o está vacío; si no, propone `profe-<tema>/` | Evitar que choque con un proyecto o con el wiki del Jefe de equipo |
| `GLOSSARY-FORMAT.md` existía pero el `SKILL.md` no listaba `GLOSSARY.md` | Se lista junto con los demás archivos del espacio de trabajo | Que el formato de glosario se use |
| Ejemplos de yoga, Rust y gimnasio | Se conservan y se suman ejemplos de contenido (ganchos, retención, editar reels) | Que sirva a un creador |
| "Abre la lección con un comando" | Indica el comando por sistema (`open`, `xdg-open`, `start`) | Más claro |
| Recursos y comunidades | Prefiere los que están en el idioma del usuario cuando son igual de buenos | Para hispanohablantes, sin bajar la calidad |
| Una lista de principios, sin orden para empezar | Una "Primera sesión, en orden" de seis pasos | Salió en la prueba: sin orden, la primera sesión se adivinaba |
| "Lección autocontenida" y "componentes compartidos en `./assets/`" parecían chocar | Aclara que autocontenida es que no depende de internet ni de compilar; enlazar `./assets/` está bien | Lo mismo |
| Si no puede abrir la lección, no dice qué hacer | Le da al usuario la ruta absoluta | Sesiones sin pantalla o remotas |
| Valores `active` y `superseded by LR-NNNN`, y enlaces `[[MISSION.md]]` | `Estado: vigente` y `Estado: reemplazado por 0007-nombre.md`, y nombres entre comillas invertidas | Traducción, y que coincida con cómo se numeran los archivos |
| Lo que el usuario ya sabe no tenía un lugar claro | Va en un registro de aprendizaje, no en `MISSION.md`; el glosario vive solo en `GLOSSARY.md` | Evitar duplicados |

## 4 · Psicología de marketing (Marketing Psychology)

| Original | Ahora | Por qué |
| --- | --- | --- |
| 72 principios con ejemplos de SaaS y B2B | Los 72 principios, cada uno con su nombre original entre paréntesis y ejemplos para creadores en Instagram (reels, DMs con palabra clave, lead magnets, comunidades de pago) | Lo pidió Aldush; no se quitó ningún principio |
| Si no hay contexto del producto, no dice qué preguntar | Pregunta lo mínimo, en un solo mensaje: qué vendes, a quién, a qué precio, por qué canal y qué prueba tienes; y ofrece guardarlo en `.agents/product-marketing.md` | Respuestas menos genéricas |
| Sin guía de cómo entregar | Elige de 6 a 10 modelos por etapa del recorrido, cada uno con por qué funciona, un texto listo para usar y la nota ética | Respuestas útiles y de largo parejo (salió en la prueba) |
| Precios en "$" | Pide escribir la moneda y adaptar terminaciones y umbrales a la moneda local | En México y Colombia "$" son pesos, y en España se paga en euros |
| Ejemplos que prometen resultados o inflan el "valor total" | Notas de ética: solo números y testimonios reales, sin prometer cifras | Coherencia con el paso de "implementar de forma ética" |
| Remite a otras skills del autor (cro, copywriting, popups, ab-testing) | Remite a los modos de este paquete (Últimos 30 días y Profe) | Esas skills no vienen en el paquete |
| `evals/evals.json` | No se incluye | Es para evaluar la skill, no para usarla |

## 5 · Últimos 30 días (last30days)

| Original | Ahora | Por qué |
| --- | --- | --- |
| `SKILL.md` en inglés | `MODO.md` traducido completo, con una tabla de equivalencias para los textos de salida ("Lo que aprendí:", "PATRONES CLAVE de la investigación:", la invitación, el pie) | Que el resumen salga en español aunque las fuentes estén en inglés |
| Referencias técnicas en inglés | Se quedan en inglés, con el comando cambiado a `/skills-secretas 30dias` | Mismo motivo que en Anatomía; además, los tests del original revisan su texto exacto |
| Lee las cookies del navegador para entrar a X, con permiso (y en un caso, con el programa `agentcookie`, sin preguntar) | La búsqueda de cookies está apagada en todos los equipos (`scripts/lib/env.py`, `x_policy`). Solo se vuelve a encender si el usuario fija `LAST30DAYS_X_BACKEND=bird` a propósito | Leer cookies de sesión es delicado, y entrar a X con ellas va contra sus reglas y puede costar la cuenta |
| La primera vez corre un asistente que pregunta por cookies e instala yt-dlp con Homebrew y la CLI de Digg con `npx` | La primera vez corre `scripts/setup_basico.py`, que guarda la configuración sin cookies y sin instalar nada, y dice en español qué fuentes ya funcionan | Nada se instala sin que el usuario diga que sí |
| Puede instalar Python con `uv` y programas con `brew` o `npx` por su cuenta | El `MODO.md` prohíbe instalar sin un sí explícito, y `references/runtime.md` ya no instala Python con `uv`: solo usa uno que ya esté | Lo mismo (lo de `uv` salió en la prueba) |
| Avisos del motor que invitan a sacar una key de ScrapeCreators y a iniciar sesión en X desde el navegador (`scripts/lib/quality_nudge.py`, `scripts/lib/ui.py`) | Avisos neutros que solo dicen qué key necesita cada fuente | Sin links de venta ni el camino de las cookies |
| Ofrece en cada primera vez el servicio de pago ScrapeCreators | No lo ofrece; solo lo explica si el usuario pregunta por TikTok o Instagram | Sin links de venta |
| Revisión de "copia vieja" que redirige a la copia del autor en la caché de plugins | Quitada (`references/runtime.md`, paso 0) | Podía cargar la skill original en lugar de esta |
| Frontmatter con `allowed-tools: Bash` | El `SKILL.md` de entrada no aprueba herramientas por adelantado | Claude Code pide permiso antes de correr comandos |
| Insignia `🌐 last30days v...` y versión leída del `plugin.json` | El motor sigue imprimiendo su insignia en inglés, pero Claude escribe en su lugar `🌐 Últimos 30 días · last30days v3.31.0 · fecha`; el motor lee su versión del archivo `VERSION` del modo (`scripts/lib/render.py`) | Dentro de este plugin, el `plugin.json` tiene la versión de skills-secretas |
| El motor solo reconoce las etiquetas en inglés al exportar a HTML o guardar en la biblioteca | Reconoce también las etiquetas en español (`scripts/lib/html_render.py` y `scripts/lib/library.py`), sin quitar las originales | Que el HTML y la biblioteca funcionen con resúmenes en español |
| Textos de la página HTML y de la biblioteca en inglés ("Research library", "Generated ... by", "Re-run for fresh data") | En español | Son páginas para compartir |
| Comando `/last30days` en los mensajes del motor (resumen de tendencias, avisos, HTML, encabezados de progreso) y ruta `skills/last30days/...` en sus sugerencias de reparación | `/skills-secretas 30dias` y la ruta nueva | Que los comandos que ve el usuario funcionen |
| Imágenes y audio de demostración (14 MB), scripts de desarrollo y `box_chrome_login.py` | No se incluyen | No se usan al correr; `box_chrome_login.py` solo sirve para entrar a X con el navegador |
| Mensajes de progreso del motor en inglés | Se quedan en inglés; Claude los resume en español | El motor tiene unas 72 mil líneas; los lee Claude, no el usuario |

**Cómo se comprobó.** De los archivos de Python del motor, 99 quedaron con el
mismo código que el original (mismo árbol de sintaxis). Cambiaron 12: los diez
de esta tabla (`last30days.py`, `env.py`, `render.py`, `html_render.py`,
`library.py`, `pipeline.py`, `doctor.py`, `prescriptions.py`, `ui.py` y
`quality_nudge.py`) y dos expresiones regulares (`amazon.py` y
`topic_shape.py`) donde la raya larga se escribió como `\u2014`, que
encuentra exactamente lo mismo. Y se agregó `setup_basico.py`. Además se corrió
la batería de tests del original (6,927 tests) contra el motor modificado.
Fallan 95: 94 son los que comprueban la lectura de cookies (ahora apagada a
propósito) o esperan los textos en inglés, los avisos y el comando viejo que se
cambiaron, y 1 falla igual en el original por la máquina donde se corrió
(permisos de root). Las pruebas de este paquete (`tests/`) comprueban las
etiquetas en español, que las cookies quedan apagadas y que la versión se lee
bien.

Los cinco modos se probaron con un ejemplo real cada uno, y lo que salió en
esas pruebas está en las filas marcadas "salió en la prueba".
