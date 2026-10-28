<img src="../assets/readme/divider.svg" alt="" width="100%">

# Práctica 1 · Primer repositorio

**Objetivo:** crear un repositorio en GitHub, trabajar en él desde el equipo y subir los cambios.
**Tiempo:** 20 minutos. **Requisitos:** cuenta de GitHub, Git instalado y configurado ([guía](../docs/instalacion.md)).

## Parte A · En el navegador

1. Crear un repositorio llamado `practica-git`, público, **con README**.
2. Editar el README desde la web: agregar una línea con tu nombre y programa. *Commit changes*.

## Parte B · En la terminal

```bash
# 1. Clonar (copiar la URL del botón verde Code)
git clone https://github.com/TU_USUARIO/practica-git.git
cd practica-git

# 2. Crear un archivo
#    Linux / Git Bash:
echo "print('Hola, GitHub')" > hola.py
#    PowerShell:
#    Set-Content hola.py "print('Hola, GitHub')"

# 3. Ver el estado: hola.py aparece sin seguimiento
git status

# 4. Preparar y confirmar
git add hola.py
git commit -m "Agrega script de saludo"

# 5. Subir
git push
```

3. Recargar la página del repositorio: `hola.py` ya está en GitHub.
4. Abrir **Commits** y comparar los dos commits (el de la web y el de la terminal).

## Parte C · Traer cambios de la nube

1. En la web, editar `hola.py` y agregar una segunda línea. *Commit changes*.
2. En la terminal:

```bash
git pull
git log --oneline
```

## Comprobación

- [ ] El repositorio tiene 3 commits.
- [ ] `git status` dice `nothing to commit, working tree clean`.
- [ ] Puedes explicar la diferencia entre `git add`, `git commit` y `git push`.

[Siguiente práctica](02_ramas_y_pull_request.md)
