# Cómo usar skills-secretas

Cinco skills en una, en español. Le hablas a Claude normal y él elige el modo.
Si quieres elegirlo tú, escribe el comando seguido del modo: `jefe`,
`anatomia`, `profe`, `psicologia` o `30dias`.

## Instálala en 1 minuto

En Claude Code:

```
/plugin marketplace add aldushmedia/skills-secretas
/plugin install skills-secretas@skills-secretas
```

Instalada como plugin, el comando es `/skills-secretas:skills-secretas`. Si
prefieres el comando corto `/skills-secretas`, copia la carpeta a mano:

```bash
git clone https://github.com/aldushmedia/skills-secretas.git
cp -r skills-secretas/skills/skills-secretas ~/.claude/skills/
```

Si la skill no aparece, reinicia Claude Code.

## ¿Qué modo uso?

| Quieres... | Modo | Dile algo como |
| --- | --- | --- |
| que Claude persiga una meta grande con varios agentes | 1 · Jefe de equipo (beta) | «Encárgate de esta meta: ...» |
| entender algo técnico con una figura que puedas mover | 2 · Anatomía | «Explícame cómo funciona ..., interactivo» |
| aprender algo paso a paso, en varias sesiones | 3 · Profe | «Enséñame a ...» |
| vender mejor con psicología | 4 · Psicología de marketing | «Aplica psicología de marketing a ...» |
| saber qué se dijo de un tema este mes | 5 · Últimos 30 días | «¿Qué se dijo de ... en el último mes?» |

---

## 1 · Jefe de equipo (beta)

**Qué hace.** Toma una meta grande y la persigue con agentes en segundo plano,
mientras te sigue hablando y guarda lo aprendido en un wiki.

**Cuándo usarlo.** Para armar el calendario de contenido del mes o preparar un
lanzamiento con varias piezas (guiones, captions, DMs).

**Cómo pedirlo.**
- «Encárgate de esta meta: armar un calendario de 7 reels sobre IA para creadores»
- «Modo jefe de equipo: prepara el lanzamiento de mi comunidad de pago»
- «Encárgate de esta meta: investigar a mis 5 competidores y proponer 10 ideas de reels»

**Qué necesitas antes.** Nada que instalar. Solo se activa si lo pides de forma
explícita, y antes de lanzar agentes te confirma la meta y dónde guardar el
wiki.

**Qué te entrega.** El trabajo hecho por los agentes, un wiki en su propia
carpeta (`wiki-<meta>/`) y propuestas de horarios recurrentes.

**Límites y cuidados.** Está en beta en el original. Gasta bastantes tokens
porque trabaja con varios agentes. Revisa lo que hacen antes de publicar nada.

---

## 2 · Anatomía

**Qué hace.** Explica algo técnico con una figura isométrica interactiva: una
máquina real cuyas piezas se mueven como funciona la idea.

**Cuándo usarlo.** Para un post o un carrusel que explique cómo funciona el
algoritmo, una herramienta de IA o tu método, o para una página de venta que se
vea premium.

**Cómo pedirlo.**
- «Explícame cómo funciona el algoritmo de reels, interactivo»
- «Hazme una figura interactiva de cómo un DM con palabra clave se vuelve venta»
- «Explícame cómo funciona un reel viral, interactivo, y sácalo en PDF»

**Qué necesitas antes.** Node.js 20 o más reciente
([nodejs.org](https://nodejs.org)). Para las revisiones automáticas, Chrome o
Chromium; si está en un lugar raro, define `CHROME_PATH`. No hay paquetes que
instalar.

**Qué te entrega.** Una página HTML con la figura (y su script para
regenerarla), en tema oscuro y claro, capturas para revisarla y, si lo pides, un
PDF A4 en formato póster, plano o detallado.

**Límites y cuidados.** Una figura simple tarda menos de una hora; una grande,
varias. Ejecuta scripts de Node y abre Chrome sin ventana en tu equipo: revisa
antes lo que corre. La publicación en la galería del autor original no viene en
este paquete.

---

## 3 · Profe

**Qué hace.** Es un tutor personal: te arma lecciones cortas, hojas de repaso y
un registro de lo que ya aprendiste, para seguir donde te quedaste.

**Cuándo usarlo.** Para aprender a escribir ganchos, editar en CapCut o
entender métricas, a tu ritmo y en varias sesiones.

**Cómo pedirlo.**
- «Enséñame a escribir ganchos para reels»
- «Quiero aprender a leer las métricas de Instagram»
- «Enséñame a editar reels en CapCut desde cero»

**Qué necesitas antes.** Nada que instalar. Trabaja en una carpeta: si la
carpeta donde estás tiene otras cosas, te propone crear `profe-<tema>/`.

**Qué te entrega.** Una misión (`MISSION.md`), lecciones en HTML
(`lessons/`), hojas de repaso (`reference/`), recursos confiables
(`RESOURCES.md`) y registros de aprendizaje.

**Límites y cuidados.** Primero te va a preguntar para qué quieres aprender el
tema; sin eso las lecciones salen genéricas. Busca recursos en la web y te los
cita.

---

## 4 · Psicología de marketing

**Qué hace.** Aplica 72 principios de psicología y modelos mentales (anclaje,
escasez, prueba social, aversión a la pérdida y más) a tu oferta, tu precio o tu
contenido.

**Cuándo usarlo.** Para ponerle precio a tu comunidad, escribir la página de
venta o mejorar los DMs con palabra clave.

**Cómo pedirlo.**
- «Aplica psicología de marketing a esta oferta: comunidad de $29/mes para crecer en Instagram con IA»
- «¿Por qué la gente no compra mi curso? Te paso la página»
- «Dame 5 formas éticas de crear urgencia en mi lanzamiento»

**Qué necesitas antes.** Nada. Si tienes un archivo `.agents/product-marketing.md`
con tu producto y tu audiencia, lo lee primero.

**Qué te entrega.** Los principios que aplican a tu caso, por qué funcionan y
cómo usarlos en concreto, con ejemplos de reels, DMs y comunidades.

**Límites y cuidados.** Úsalo con ética: la escasez y la urgencia solo cuando
son reales.

---

## 5 · Últimos 30 días

**Qué hace.** Investiga qué dijo la gente de un tema en el último mes en Reddit,
X, YouTube, TikTok, Hacker News, Polymarket, GitHub y la web, y te lo resume en
español con citas.

**Cuándo usarlo.** Para encontrar ideas de contenido con lo que se está
hablando ahora, o para saber qué piensa tu audiencia de una herramienta antes de
hablar de ella.

**Cómo pedirlo.**
- «¿Qué se dijo de Claude Code en el último mes?»
- «¿Qué opina la gente de las herramientas de video con IA este mes?»
- «Compara CapCut contra Premiere según la comunidad»

**Qué necesitas antes.** Python 3.12 o más reciente. La primera vez se configura
solo, sin instalar nada. Sin API keys ya funcionan Reddit, Hacker News,
Polymarket, GitHub y la web. Para sumar más fuentes:
- YouTube: instala `yt-dlp` (`brew install yt-dlp` en Mac, `pipx install yt-dlp`
  en Linux o Windows).
- TikTok e Instagram: una key de ScrapeCreators (`SCRAPECREATORS_API_KEY`), que
  cobra después de sus llamadas gratis.
- X: `XAI_API_KEY`, o `X_BEARER_TOKEN` junto con `LAST30DAYS_X_BACKEND=xapi`.

Las keys van como variables de entorno o en `~/.config/last30days/.env`, nunca
dentro de la skill.

**Qué te entrega.** Un resumen con titulares, patrones clave, comentarios
reales con su autor y un pie con cuántos hilos, videos y publicaciones revisó.
Guarda una copia en `~/Documents/Last30Days` (si no la quieres, define
`LAST30DAYS_MEMORY_DIR` vacío).

**Límites y cuidados.**
- En este paquete no lee las cookies de tu navegador ni entra a X con tu cuenta.
- Si tienes `gh` con sesión, usa tu token solo para consultar GitHub.
- Si tienes una key de OpenAI, Gemini, xAI u OpenRouter en el entorno, la usa
  para ordenar resultados.
- Ejecuta un motor de Python grande en tu equipo: revisa antes lo que corre.
- Las fuentes pueden estar en inglés; el resumen sale en español.
