<img src="../assets/readme/divider.svg" alt="" width="100%">

# Guía rápida de comandos

Los comandos de Git son **iguales en Windows y Linux**. En Windows se pueden escribir en PowerShell, en el Símbolo del
sistema o en Git Bash. Lo que va después de `#` es un comentario y no se escribe.

[Volver al README](../README.md)

## 1. Configuración (una sola vez por equipo)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@unal.edu.co"
git config --global init.defaultBranch main     # la rama principal se llamará main
git config --global core.editor "code --wait"   # usar VS Code como editor (opcional)
git config --global core.autocrlf true          # solo Windows
git config --global core.autocrlf input         # solo Linux y macOS
git config --list --show-origin                  # revisar la configuración
```

## 2. Crear u obtener un repositorio

```bash
git init                                  # convierte la carpeta actual en repositorio
git clone https://github.com/USUARIO/REPO.git          # copia un repositorio remoto
git clone https://github.com/USUARIO/REPO.git otra     # ... en una carpeta con otro nombre
git clone --depth 1 URL                   # solo la última versión (más rápido)
```

## 3. El ciclo diario

```bash
git status                     # qué cambió y qué está preparado
git diff                       # cambios aún no preparados, línea a línea
git diff --staged              # cambios ya preparados
git add archivo.py             # preparar un archivo
git add .                      # preparar todo lo de la carpeta
git commit -m "Mensaje claro"  # guardar una versión
git commit -am "Mensaje"       # add + commit de archivos ya conocidos
git push                       # subir a GitHub
git pull                       # traer y unir lo nuevo de GitHub
```

Un buen mensaje de commit dice **qué** cambia en imperativo y en pocas palabras:
`Agrega cálculo del NDVI`, `Corrige ruta de los datos`, `Actualiza README`.

## 4. Historial

```bash
git log                              # historial completo
git log --oneline --graph --all      # historial compacto con ramas
git log -p archivo.py                # cambios de un archivo a lo largo del tiempo
git show ID                          # qué hizo un commit
git blame archivo.py                 # quién cambió cada línea
```

## 5. Ramas

```bash
git branch                     # listar ramas locales
git branch -a                  # incluir las remotas
git switch -c nueva-rama       # crear y pasarse
git switch main                # cambiar de rama
git merge nueva-rama           # unir nueva-rama a la rama actual
git branch -d nueva-rama       # borrar una rama ya integrada
git push origin --delete nueva-rama   # borrarla en GitHub
```

En tutoriales antiguos aparece `git checkout`; `git switch` y `git restore` son sus reemplazos modernos y más claros.

## 6. Repositorios remotos

```bash
git remote -v                                  # ver a dónde apunta origin
git remote add origin https://github.com/USUARIO/REPO.git
git remote set-url origin git@github.com:USUARIO/REPO.git   # cambiar a SSH
git push -u origin main                         # primer push de la rama
git fetch                                       # traer sin unir
git pull --rebase                               # traer y poner tus commits encima
```

## 7. Deshacer

| Situación | Comando |
|---|---|
| Descartar cambios de un archivo (no preparado) | `git restore archivo` |
| Sacar un archivo del área de preparación | `git restore --staged archivo` |
| Corregir el mensaje del último commit (aún no subido) | `git commit --amend -m "Nuevo mensaje"` |
| Deshacer el último commit pero conservar los cambios | `git reset --soft HEAD~1` |
| Revertir un commit ya subido (crea uno nuevo que lo anula) | `git revert ID` |
| Recuperar un archivo de un commit anterior | `git restore --source ID archivo` |
| Guardar cambios sin commit para después | `git stash` · `git stash list` · `git stash pop` |

> [!WARNING]
> `git reset --hard` y `git push --force` **borran trabajo**. Úsalos solo si sabes exactamente qué se pierde.

## 8. Etiquetas y versiones

```bash
git tag v1.0 -m "Versión entregada"
git push --tags
gh release create v1.0 --notes "Primera versión"   # crea un Release en GitHub
```

## 9. GitHub CLI (`gh`)

```bash
gh auth login                      # iniciar sesión
gh auth status                     # comprobar la sesión
gh repo create NOMBRE --public --source=. --push   # crear repo desde la carpeta actual
gh repo clone USUARIO/REPO         # clonar
gh repo view --web                 # abrir el repo en el navegador
gh issue list                      # ver issues
gh issue create --title "..." --body "..."
gh pr create --fill                # abrir pull request de la rama actual
gh pr list                         # ver pull requests
gh pr checkout 12                  # traer el PR 12 para probarlo
gh pr merge 12 --squash            # integrar el PR 12
gh run list                        # ver ejecuciones de GitHub Actions
```

## 10. Ayuda

```bash
git help comando        # manual completo (por ejemplo: git help commit)
git comando -h          # resumen corto
gh comando --help
```

[Volver al README](../README.md)
