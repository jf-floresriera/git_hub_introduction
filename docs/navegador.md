<img src="../assets/readme/divider.svg" alt="" width="100%">

# Trabajar desde el navegador

Todo lo de esta guía se hace en [github.com](https://github.com) sin instalar nada.

[Volver al README](../README.md)

## Crear la cuenta

1. Ir a [github.com/signup](https://github.com/signup), escribir correo, contraseña y nombre de usuario.
2. Activar la **verificación en dos pasos** (Settings → Password and authentication). GitHub la exige a quien contribuye código.
3. Estudiantes y docentes: solicitar [GitHub Education](https://education.github.com/) con el correo institucional para
   acceder al Student Developer Pack.

## Recorrido por la página de un repositorio

| Pestaña | Qué muestra |
|---|---|
| **Code** | Archivos, README, botón verde *Code* para clonar o descargar ZIP |
| **Issues** | Tareas, errores, ideas |
| **Pull requests** | Cambios propuestos para revisar |
| **Actions** | Automatizaciones y sus resultados |
| **Projects** | Tableros de planificación |
| **Wiki** | Documentación extensa |
| **Settings** | Nombre, visibilidad, colaboradores, Pages, ramas protegidas |

## Crear un repositorio

1. Botón **New** (o el signo **+** arriba a la derecha → *New repository*).
2. **Repository name**: corto, sin espacios (`analisis-ndvi`, `tesis_codigo`).
3. **Public** o **Private**.
4. Marcar **Add a README file**; opcionalmente un `.gitignore` (por ejemplo *Python*) y una licencia.
5. **Create repository**.

## Subir y editar archivos

- **Subir**: *Add file → Upload files*, arrastrar archivos o carpetas, escribir el mensaje del commit, *Commit changes*.
- **Crear**: *Add file → Create new file*. Escribir `carpeta/archivo.md` en el nombre crea la carpeta.
- **Editar uno**: abrir el archivo → lápiz → editar → *Commit changes*.
- **Editar varios a la vez**: pulsar <kbd>.</kbd> en el repositorio (o cambiar `github.com` por `github.dev` en la URL).
  Se abre un editor tipo VS Code en el navegador; los cambios se confirman desde el panel *Source Control*.

## Historial y comparación

- *Commits* (reloj junto al último commit) muestra la lista de versiones.
- Al abrir un commit se ve en verde lo agregado y en rojo lo eliminado.
- En un archivo, **History** muestra solo sus cambios y **Blame** quién escribió cada línea.

## Ramas y pull requests desde la web

1. Selector de rama (dice `main`) → escribir un nombre nuevo → *Create branch*.
2. Editar archivos en esa rama.
3. Aparece el aviso **Compare & pull request** → describir el cambio → *Create pull request*.
4. En la pestaña *Files changed* se comenta línea a línea y se aprueba (*Review changes*).
5. **Merge pull request** → *Confirm merge* → *Delete branch*.

## Issues

- *New issue*, título claro y descripción. Se pueden asignar personas, etiquetas y un hito.
- Escribir `Closes #12` en un pull request cierra el issue 12 automáticamente al integrarlo.
- Menciones con `@usuario` notifican a esa persona.

## Fork: aportar a un proyecto ajeno

1. **Fork** (arriba a la derecha) crea una copia en tu cuenta.
2. Hacer los cambios en la copia.
3. *Contribute → Open pull request* propone los cambios al proyecto original.

## Publicar un sitio con Pages

*Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save*. En uno o dos minutos el sitio
queda en `https://USUARIO.github.io/REPO/`. Práctica: [`../ejercicios/04_github_pages.md`](../ejercicios/04_github_pages.md).

## Markdown en un minuto

```markdown
# Título
## Subtítulo
**negrita**, *cursiva*, `código`
- lista
1. lista numerada
[enlace](https://github.com)
![imagen](ruta/imagen.png)
> [!NOTE]
> Nota destacada
```

[Volver al README](../README.md)
