<img src="../assets/readme/divider.svg" alt="" width="100%">

# Instalación y configuración

[Volver al README](../README.md)

## Windows

### Opción 1: instalador gráfico

1. Descargar Git desde [git-scm.com/download/win](https://git-scm.com/download/win).
2. Ejecutar el instalador. Las opciones por defecto sirven; conviene revisar dos pantallas:
   - **Default editor**: elegir *Visual Studio Code* si ya está instalado.
   - **Initial branch name**: elegir *Override* y escribir `main`.
3. Al terminar quedan disponibles **Git Bash** (terminal tipo Linux) y el comando `git` en PowerShell.

### Opción 2: winget (PowerShell)

```powershell
winget install --id Git.Git -e --source winget
winget install --id GitHub.cli -e
winget install --id GitHub.GitHubDesktop -e      # opcional
winget install --id Microsoft.VisualStudioCode -e   # opcional
```

Cerrar y volver a abrir la terminal, y comprobar:

```powershell
git --version
gh --version
```

### Terminales en Windows

| Terminal | Cuándo usarla |
|---|---|
| **PowerShell** | La terminal de Windows; acepta `git` y `gh` sin problema |
| **Git Bash** | Si se siguen tutoriales escritos para Linux (`ls`, `touch`, `cat`...) |
| **Windows Terminal** | Contenedor con pestañas para PowerShell, Git Bash y WSL |
| **WSL** | Linux completo dentro de Windows; útil para proyectos que se desplegarán en servidores |

## Linux

```bash
# Debian, Ubuntu, Linux Mint, Pop!_OS
sudo apt update
sudo apt install git gh

# Fedora
sudo dnf install git gh

# Arch, Manjaro
sudo pacman -S git github-cli
```

Si la versión de `gh` de la distribución es antigua, en [cli.github.com](https://cli.github.com/) están los repositorios
oficiales para tener la última.

```bash
git --version
gh --version
```

## macOS (referencia)

```bash
xcode-select --install     # instala git
brew install git gh        # con Homebrew
```

## Configuración inicial (todos los sistemas)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@unal.edu.co"
git config --global init.defaultBranch main
```

El correo debe ser uno de los registrados en la cuenta de GitHub para que los commits aparezcan en el perfil. Si se prefiere
no mostrarlo, GitHub ofrece uno privado en **Settings → Emails** (del tipo `ID+usuario@users.noreply.github.com`).

Los scripts [`../scripts/configurar_git.ps1`](../scripts/configurar_git.ps1) y
[`../scripts/configurar_git.sh`](../scripts/configurar_git.sh) hacen esta configuración preguntando nombre y correo.

## Autenticación: cómo GitHub sabe que eres tú

Desde agosto de 2021 GitHub no acepta la contraseña de la cuenta para operaciones de Git. Hay cuatro caminos; basta con uno.

### A. GitHub CLI (el más simple)

```bash
gh auth login
# GitHub.com → HTTPS → Yes (autenticar Git) → Login with a web browser
```

Muestra un código, abre el navegador y listo: `git push` funciona sin pedir nada más.

### B. Git Credential Manager (Windows)

Viene con Git para Windows. La primera vez que se hace `git push` abre una ventana para iniciar sesión en el navegador
y guarda la credencial en el sistema.

### C. Token personal (PAT)

1. **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
2. Elegir repositorios y permisos (*Contents: Read and write*), y una fecha de vencimiento.
3. Cuando Git pida contraseña, pegar el token.

### D. Llave SSH

```bash
ssh-keygen -t ed25519 -C "tu_correo@unal.edu.co"   # Enter a todo, o poner frase de paso
cat ~/.ssh/id_ed25519.pub                          # Linux y Git Bash
type $env:USERPROFILE\.ssh\id_ed25519.pub          # PowerShell
```

Copiar la línea completa en **Settings → SSH and GPG keys → New SSH key** y probar:

```bash
ssh -T git@github.com
```

Con SSH, las URL de clonado son del tipo `git@github.com:USUARIO/REPO.git`.

[Volver al README](../README.md)
