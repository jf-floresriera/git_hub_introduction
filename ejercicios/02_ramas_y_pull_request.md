<img src="../assets/readme/divider.svg" alt="" width="100%">

# Práctica 2 · Ramas y pull request

**Objetivo:** hacer un cambio en una rama, proponerlo con un pull request e integrarlo.
**Tiempo:** 25 minutos. **Requisito:** haber hecho la [práctica 1](01_primer_repositorio.md).

## Parte A · Trabajar en una rama

```bash
cd practica-git
git switch -c mejora-saludo

# Editar hola.py para que pregunte el nombre:
#   nombre = input("¿Cómo te llamas? ")
#   print(f"Hola, {nombre}. Bienvenido a GitHub")

git add hola.py
git commit -m "Pide el nombre antes de saludar"
git push -u origin mejora-saludo
```

## Parte B · Pull request

1. En GitHub aparece el aviso **Compare & pull request**. Abrirlo.
2. Título: `Saludo personalizado`. En la descripción, explicar el cambio.
3. Revisar la pestaña **Files changed**.
4. Si trabajan en parejas: agregar al compañero como colaborador (*Settings → Collaborators*) y pedirle revisión
   (*Reviewers*). Que deje un comentario en una línea.
5. **Merge pull request → Confirm merge → Delete branch**.

Con GitHub CLI, los pasos 1 a 5 se pueden hacer así:

```bash
gh pr create --fill
gh pr view --web
gh pr merge --merge --delete-branch
```

## Parte C · Actualizar la copia local

```bash
git switch main
git pull
git branch -d mejora-saludo
git log --oneline --graph
```

## Reto: provocar y resolver un conflicto

1. En la web, cambiar la línea del `print` en `main`.
2. En el equipo, **sin hacer pull**, cambiar la misma línea de otra forma, hacer commit e intentar `git push`.
3. Git rechaza el push. Hacer `git pull`: aparece un conflicto.
4. Abrir `hola.py`, elegir el contenido entre las marcas `<<<<<<<`, `=======` y `>>>>>>>`, borrar las marcas y:

```bash
git add hola.py
git commit -m "Resuelve conflicto en el saludo"
git push
```

## Comprobación

- [ ] El pull request aparece como *Merged*.
- [ ] `git log --oneline --graph` muestra la rama integrada.
- [ ] Resolviste un conflicto.

[Siguiente práctica](03_colaborar_con_fork.md)
