<img src="../assets/readme/divider.svg" alt="" width="100%">

# Servicios de GitHub

[Volver al README](../README.md)

Cuotas del plan gratuito para cuentas personales según la
[documentación de planes de GitHub](https://docs.github.com/es/get-started/learning-about-github/githubs-plans),
consultada en octubre de 2026. Pueden cambiar; conviene revisarlas antes de depender de ellas.

## Colaboración

**Issues.** Lista de tareas, errores y preguntas de un proyecto. Cada issue tiene número, responsables, etiquetas y
conversación. Sirven como bitácora de decisiones.

**Pull requests.** Propuesta de integrar una rama en otra. Muestra las diferencias, permite comentar línea a línea, pedir
cambios y aprobar. Es el corazón del trabajo en equipo.

**Discussions.** Foro para preguntas abiertas e ideas que no son tareas concretas.

**Projects.** Tableros (tipo Kanban), tablas y cronogramas que se alimentan de issues y pull requests.

**Wiki.** Documentación de varias páginas asociada al repositorio.

## Automatización y publicación

**Actions.** Ejecuta tareas automáticamente cuando ocurre algo (un push, un pull request, una hora programada): pruebas,
compilación, generación de figuras, publicación. Ilimitado en repositorios públicos con los ejecutores estándar;
2000 minutos al mes en privados.

Ejemplo real en este repositorio: [`.github/workflows/verificar.yml`](../.github/workflows/verificar.yml).

```yaml
name: Verificar
on: [push, pull_request]
jobs:
  verificar:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python ejemplos/hola_github.py
```

**Pages.** Publica un sitio web estático (HTML o Markdown) desde una rama. Gratis en repositorios públicos. Sirve para
páginas personales, documentación, cursos y presentaciones.

**Releases.** Versiones descargables con notas de cambios. Con la integración de **Zenodo**, cada release recibe un **DOI**
para citar el software en artículos y tesis.

**Packages.** Registro de paquetes (npm, PyPI vía otras herramientas, Docker, Maven...). 500 MB en el plan gratuito.

## Desarrollo en la nube

**Codespaces.** Una máquina virtual con VS Code en el navegador, lista para programar sin instalar nada. 120 horas-núcleo y
15 GB al mes (una máquina de 2 núcleos rinde 60 horas).

**github.dev.** Editor ligero en el navegador (tecla <kbd>.</kbd> en cualquier repositorio). Gratis, sin terminal.

## Inteligencia artificial

**Copilot.** Asistente que sugiere código y responde preguntas dentro del editor y en github.com. Tiene un plan gratuito
con límites mensuales; estudiantes y docentes verificados en GitHub Education acceden a beneficios adicionales.

## Seguridad

**Dependabot.** Avisa cuando una librería usada tiene una vulnerabilidad conocida y abre pull requests para actualizarla.

**Secret scanning y push protection.** Detectan contraseñas o llaves subidas por error en repositorios públicos.

**Ramas protegidas.** Exigen revisión o pruebas antes de integrar en `main` (en repositorios privados requiere plan de pago).

## Perfil y comunidad

- **Perfil**: un repositorio con el mismo nombre que el usuario (`usuario/usuario`) muestra su README en la página del perfil.
- **Stars, watch y fork**: marcar favoritos, seguir novedades y copiar proyectos.
- **Organizaciones**: cuentas compartidas para grupos de investigación, cursos o empresas, con equipos y permisos.
- **GitHub Classroom**: distribuir y recoger tareas de programación en cursos.

[Volver al README](../README.md)
