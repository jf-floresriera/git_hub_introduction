<img src="../assets/readme/divider.svg" alt="" width="100%">

# Trabajar desde el escritorio

Dos opciones para usar Git con botones en lugar de comandos. Por dentro hacen lo mismo que la terminal.

[Volver al README](../README.md)

## GitHub Desktop

| Sistema | Disponibilidad |
|---|---|
| Windows | Oficial: [desktop.github.com](https://desktop.github.com/) o `winget install GitHub.GitHubDesktop` |
| macOS | Oficial |
| Linux | Sin versión oficial; versión comunitaria [shiftkey/desktop](https://github.com/shiftkey/desktop) (.deb, .rpm, AppImage) |

### Flujo básico

| Acción | En GitHub Desktop | Equivale a |
|---|---|---|
| Iniciar sesión | *File → Options → Accounts → Sign in* | `gh auth login` |
| Clonar | *File → Clone repository* | `git clone` |
| Crear repo | *File → New repository* | `git init` |
| Ver cambios | Pestaña *Changes* | `git status` · `git diff` |
| Preparar | Casillas junto a cada archivo | `git add` |
| Confirmar | *Summary* + **Commit to main** | `git commit -m` |
| Subir | **Push origin** | `git push` |
| Traer | **Fetch origin** → **Pull origin** | `git fetch` · `git pull` |
| Rama nueva | *Current branch → New branch* | `git switch -c` |
| Pull request | *Branch → Create pull request* | `gh pr create` |
| Historial | Pestaña *History* | `git log` |

### Ventajas y límites

- Muy claro para empezar: se ve exactamente qué cambió antes de confirmar.
- Resolver conflictos abre el editor elegido.
- No cubre todo Git (por ejemplo `rebase` interactivo o `stash` avanzado); para eso, terminal.

## Visual Studio Code

Disponible oficialmente en **Windows, Linux y macOS**. Necesita tener Git instalado.

1. *File → Open Folder* y abrir la carpeta del proyecto.
2. Panel **Source Control** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>G</kbd>):
   - **+** junto a un archivo = `git add`.
   - Escribir el mensaje y **Commit** = `git commit`.
   - **Sync Changes** = `git pull` + `git push`.
3. Abajo a la izquierda, el nombre de la rama: clic para cambiar o crear ramas.
4. *Publish to GitHub* sube una carpeta nueva a un repositorio nuevo.
5. Terminal integrada (<kbd>Ctrl</kbd>+<kbd>ñ</kbd> o <kbd>Ctrl</kbd>+<kbd>`</kbd>) para combinar botones y comandos.

Extensiones recomendadas:

- **GitHub Pull Requests**: revisar y comentar PR dentro del editor.
- **GitLens**: autor de cada línea e historial enriquecido.
- **GitHub Copilot**: sugerencias de código (plan gratuito con límites).

## Otras herramientas

RStudio (pestaña *Git*), PyCharm y demás IDE de JetBrains, QGIS mediante complementos, y clientes como GitKraken o
Sourcetree. Todos usan el mismo repositorio, así que se pueden combinar.

[Volver al README](../README.md)
