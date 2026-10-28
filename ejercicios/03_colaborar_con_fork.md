<img src="../assets/readme/divider.svg" alt="" width="100%">

# Práctica 3 · Colaborar con un fork

**Objetivo:** aportar a un repositorio en el que no tienes permiso de escritura, como se hace en proyectos de código abierto.
**Tiempo:** 20 minutos.

## Pasos

1. Abrir este repositorio: [jf-floresriera/git_hub_introduction](https://github.com/jf-floresriera/git_hub_introduction).
2. Pulsar **Fork → Create fork**. Ahora existe `TU_USUARIO/git_hub_introduction`.
3. Clonar **tu** copia y crear una rama:

```bash
git clone https://github.com/TU_USUARIO/git_hub_introduction.git
cd git_hub_introduction
git switch -c participante-TU_USUARIO
```

4. Agregar tu nombre al final de [`participantes.md`](participantes.md) con el formato indicado.
5. Confirmar y subir:

```bash
git add ejercicios/participantes.md
git commit -m "Agrega a TU_NOMBRE a participantes"
git push -u origin participante-TU_USUARIO
```

6. En GitHub: **Contribute → Open pull request**. El pull request va al repositorio original.
7. La persona responsable lo revisa e integra.

## Mantener el fork actualizado

```bash
git remote add upstream https://github.com/jf-floresriera/git_hub_introduction.git
git fetch upstream
git switch main
git merge upstream/main
git push
```

O en la web: botón **Sync fork** en la página de tu copia.

[Siguiente práctica](04_github_pages.md)
