#!/usr/bin/env bash
# Configuración inicial de Git en Linux, macOS o Git Bash (Windows).
# Uso:  bash scripts/configurar_git.sh

set -euo pipefail

if ! command -v git >/dev/null 2>&1; then
  echo "Git no está instalado."
  echo "  Debian/Ubuntu:  sudo apt install git"
  echo "  Fedora:         sudo dnf install git"
  echo "  Arch:           sudo pacman -S git"
  exit 1
fi

echo "Git encontrado: $(git --version)"
echo

nombre_actual=$(git config --global user.name || true)
correo_actual=$(git config --global user.email || true)

read -r -p "Nombre completo [${nombre_actual}]: " nombre
read -r -p "Correo registrado en GitHub [${correo_actual}]: " correo
nombre=${nombre:-$nombre_actual}
correo=${correo:-$correo_actual}

if [[ -z "$nombre" || -z "$correo" ]]; then
  echo "Nombre y correo son obligatorios."
  exit 1
fi

git config --global user.name "$nombre"
git config --global user.email "$correo"
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global core.autocrlf input
git config --global color.ui auto

echo
echo "Configuración guardada:"
git config --global --list | grep -E "^(user|init|pull|core.autocrlf)"

echo
if command -v gh >/dev/null 2>&1; then
  if gh auth status >/dev/null 2>&1; then
    echo "GitHub CLI ya tiene una sesión activa."
  else
    read -r -p "¿Iniciar sesión en GitHub ahora con 'gh auth login'? [s/N]: " r
    [[ "${r,,}" == "s" ]] && gh auth login
  fi
else
  echo "Sugerencia: instala GitHub CLI (gh) para autenticarte fácilmente: https://cli.github.com/"
fi
