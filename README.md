# skills-secretas

Cinco skills para Claude Code en una sola, en español. Le hablas a Claude normal
y él elige el modo:

| Modo | Qué hace | Pídelo así |
| --- | --- | --- |
| 1 · Jefe de equipo (beta) | Persigue una meta grande con agentes en segundo plano y guarda lo aprendido en un wiki | «Encárgate de esta meta: armar un calendario de 7 reels sobre IA» |
| 2 · Anatomía | Explica algo técnico con una figura isométrica interactiva, y la imprime en PDF | «Explícame cómo funciona el algoritmo de reels, interactivo» |
| 3 · Profe | Tutor personal: lecciones cortas, hojas de repaso y memoria de dónde te quedaste | «Enséñame a escribir ganchos para reels» |
| 4 · Psicología de marketing | 72 principios de psicología aplicados a tu oferta, tu precio y tu contenido | «Aplica psicología de marketing a mi comunidad de $29/mes» |
| 5 · Últimos 30 días | Qué se dijo de un tema el último mes en Reddit, X, YouTube, TikTok, Hacker News y la web, resumido en español | «¿Qué se dijo de Claude Code en el último mes?» |

## Instalación

En Claude Code, como plugin:

```
/plugin marketplace add aldushmedia/skills-secretas
/plugin install skills-secretas@skills-secretas
```

El comando queda como `/skills-secretas:skills-secretas`. Si prefieres el
comando corto `/skills-secretas`, copia la carpeta:

```bash
git clone https://github.com/aldushmedia/skills-secretas.git
cp -r skills-secretas/skills/skills-secretas ~/.claude/skills/
```

Pruébala: escribe «explícame cómo funciona un reel viral, interactivo».

Las instrucciones de cada modo, con frases de ejemplo y lo que necesitas antes,
están en [COMO_USAR.md](skills/skills-secretas/COMO_USAR.md).

## Requisitos

- **Anatomía:** Node.js 20 o más reciente, y Chrome o Chromium para las
  revisiones automáticas.
- **Últimos 30 días:** Python 3.12 o más reciente. Sin API keys ya busca en
  Reddit, Hacker News, Polymarket, GitHub y la web; YouTube, TikTok, Instagram y
  X necesitan herramientas o keys opcionales.
- Los demás modos no necesitan nada.

## Seguridad

Las skills ejecutan código en tu equipo: revísalo antes de usarlo. En esta
versión:

- Últimos 30 días no lee las cookies de tu navegador ni entra a X con tu
  cuenta, no instala nada sin que digas que sí y no publica nada sin que lo
  pidas.
- Anatomía no trae la publicación en la galería del proyecto original.
- Las API keys van como variables de entorno, nunca dentro de la skill.

Todos los cambios respecto a las originales están en
[CAMBIOS.md](skills/skills-secretas/CAMBIOS.md).

## Archivos

```
skills/skills-secretas/SKILL.md      la entrada: elige el modo y carga solo su archivo
skills/skills-secretas/COMO_USAR.md  cómo usar cada modo
skills/skills-secretas/INSTALAR.md   instalación en dos comandos
skills/skills-secretas/CREDITOS.md   autores, repos, versión y licencia de cada original
skills/skills-secretas/CAMBIOS.md    qué se tradujo y qué se cambió
skills/skills-secretas/licencias/    el texto de la licencia de cada original
skills/skills-secretas/modos/        un MODO.md por modo, con sus scripts y referencias
tests/                               pruebas del paquete
```

Para correr las pruebas: `python3 -m unittest discover -s tests -v`.

## Créditos

Adaptación al español: Aldush ([@aldushmedia](https://github.com/aldushmedia)).
Basada en el trabajo de Matt Pocock (Chief of Staff y Teach), Ryan (Anatomy),
Corey Haines (Marketing Psychology) y Matt Van Horn (last30days). Los autores,
los repos originales y la versión exacta de cada uno están en
[CREDITOS.md](skills/skills-secretas/CREDITOS.md).

## Licencia

MIT. Se conservan los avisos de copyright de los cuatro autores originales. Ver
`LICENSE` y `skills/skills-secretas/licencias/`.
