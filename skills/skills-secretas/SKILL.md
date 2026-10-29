---
name: skills-secretas
description: >-
  Cinco skills en una, en español. Jefe de equipo (beta): coordina agentes en
  segundo plano para una meta grande; solo si lo piden: «encárgate de esta
  meta», «modo jefe de equipo», «chief of staff». Anatomía: explica algo
  técnico con una figura interactiva: «explícame cómo funciona... interactivo»,
  «hazme una figura isométrica», «interactive explainer», «isometric
  illustration». Profe: tutor con lecciones, hojas de repaso y memoria de dónde
  te quedaste: «enséñame...», «quiero aprender...», «teach me». Psicología de
  marketing: aplica sesgos y modelos mentales a tu oferta o tu contenido:
  «aplica psicología a mi oferta», «por qué la gente compra», «psychology»,
  «persuasion», «cognitive bias», «social proof», «anchoring», «scarcity».
  Últimos 30 días: qué se dijo de un tema este mes en Reddit, X, YouTube,
  TikTok, Hacker News y la web: «qué se dijo de... este mes», «qué opina la
  gente de...», «last30days», «what are people saying about...».
---

# Skills secretas

Cinco modos en una sola skill. Elige **un** modo, lee **solo** su `MODO.md`
completo y síguelo. No leas los otros modos: cada uno carga sus propios
archivos cuando los necesita.

| Modo | Úsalo cuando el usuario... | Lee |
| --- | --- | --- |
| 1 · Jefe de equipo (beta) | te entrega una meta grande para que la persigas con agentes en segundo plano. Solo si lo pide de forma explícita. | [modos/1-jefe-de-equipo/MODO.md](modos/1-jefe-de-equipo/MODO.md) |
| 2 · Anatomía | quiere entender algo técnico o un sistema con una figura interactiva en lugar de texto. | [modos/2-anatomia/MODO.md](modos/2-anatomia/MODO.md) |
| 3 · Profe | quiere aprender algo a lo largo de varias sesiones, con lecciones y hojas de repaso. | [modos/3-profe/MODO.md](modos/3-profe/MODO.md) |
| 4 · Psicología de marketing | quiere aplicar psicología, sesgos o modelos mentales a su oferta, su contenido o su precio. | [modos/4-psicologia-marketing/MODO.md](modos/4-psicologia-marketing/MODO.md) |
| 5 · Últimos 30 días | quiere saber qué se dijo de un tema en el último mes en redes y en la web. | [modos/5-ultimos-30-dias/MODO.md](modos/5-ultimos-30-dias/MODO.md) |

## Cómo elegir

- Si el usuario usó el comando (`/skills-secretas`, o
  `/skills-secretas:skills-secretas` si está instalada como plugin), la primera
  palabra después del comando es el modo: `jefe`, `anatomia`, `profe`,
  `psicologia` o `30dias` (o el número del 1 al 5). El resto es su pedido.
- Si no, elige por lo que pide, con la tabla de arriba.
- Si el pedido mezcla dos modos (por ejemplo, "enséñame con una figura
  interactiva"), haz uno a la vez y pregunta por el orden solo si no es obvio.
- Si no queda claro cuál quiere, pregúntale con una línea por modo.
- El modo Jefe de equipo pone agentes a trabajar mucho rato: entra a él solo
  cuando el usuario lo pide, y confirma la meta antes de lanzar el primero.

## Rutas

Cada `MODO.md` habla de sus archivos con rutas relativas a su propia carpeta
(por ejemplo, `scripts/` o `references/` dentro de `modos/2-anatomia/`). Cuando
ejecutes un comando, usa la ruta absoluta de esa carpeta.

## Idioma

Responde en el idioma del usuario, en español por defecto. Los comandos, flags,
rutas y nombres de archivo se quedan como están.

---

Adaptación al español: Aldush ([@aldushmedia](https://github.com/aldushmedia)).
Basada en el trabajo de: [Matt Pocock](https://github.com/mattpocock/skills)
(Chief of Staff y Teach), [Ryan](https://github.com/wheresryan22/anatomy)
(Anatomy), [Corey Haines](https://github.com/coreyhaines31/marketingskills)
(Marketing Psychology) y [Matt Van Horn](https://github.com/mvanhorn/last30days-skill)
(Last 30 Days). Ver [CREDITOS.md](CREDITOS.md).
