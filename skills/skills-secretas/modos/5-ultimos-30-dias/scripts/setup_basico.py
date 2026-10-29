#!/usr/bin/env python3
"""First-run setup for skills-secretas, without installs and without cookies.

The original `last30days.py setup` also installs yt-dlp with Homebrew and the
Digg CLI with npx. This one only marks setup as done (with browser-cookie
consent off) and tells the user, in Spanish, which sources already work and
what each missing one needs.

    "$LAST30DAYS_PYTHON" "$SKILL_DIR/scripts/setup_basico.py"
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import env, setup_wizard  # noqa: E402

# key name -> (source, verb agreeing with it)
KEYS = {
    "SCRAPECREATORS_API_KEY": ("TikTok e Instagram", "necesitan"),
    "XAI_API_KEY": ("X (con la API de xAI)", "necesita"),
    "X_BEARER_TOKEN": ("X (API oficial, junto con LAST30DAYS_X_BACKEND=xapi)", "necesita"),
}


def configured_keys():
    """Names of the keys set in the environment or in the engine's .env. Values are never read out."""
    found = {name for name in KEYS if os.environ.get(name)}
    try:
        with open(env.CONFIG_FILE, encoding="utf-8") as fh:
            for line in fh:
                name, _, value = line.strip().partition("=")
                if name in KEYS and value.strip():
                    found.add(name)
    except OSError:
        pass
    return found


def main():
    if env.CONFIG_FILE is None:
        print("LAST30DAYS_CONFIG_DIR está vacío (modo sin configuración): no hay nada que guardar.")
        return 0
    if not setup_wizard.write_setup_config(env.CONFIG_FILE, browser_consent=False):
        print(f"No pude guardar la configuración en {env.CONFIG_FILE}. Revisa que puedas escribir en esa carpeta.")
        return 1
    print(f"Listo: configuración guardada en {env.CONFIG_FILE} (sin cookies del navegador y sin instalar nada).")
    print("Ya funcionan sin key: Reddit, Hacker News, Polymarket, GitHub y la web.")
    if shutil.which("yt-dlp"):
        print("YouTube: listo (yt-dlp está instalado).")
    else:
        print("YouTube: falta yt-dlp. Se instala con `brew install yt-dlp` (Mac) "
              "o `pipx install yt-dlp` (Linux y Windows).")
    keys = configured_keys()
    for name, (source, verb) in KEYS.items():
        state = "listo" if name in keys else f"{verb} {name}"
        print(f"{source}: {state}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
