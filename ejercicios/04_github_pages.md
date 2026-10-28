<img src="../assets/readme/divider.svg" alt="" width="100%">

# Práctica 4 · Publicar una página con GitHub Pages

**Objetivo:** tener una página web pública en `https://TU_USUARIO.github.io/mi-pagina/`.
**Tiempo:** 15 minutos.

## Pasos

1. Crear un repositorio **público** llamado `mi-pagina`.
2. Copiar a ese repositorio el archivo de ejemplo [`../ejemplos/pagina/index.html`](../ejemplos/pagina/index.html):
   - en la web: *Add file → Upload files*, o
   - en la terminal:

```bash
git clone https://github.com/TU_USUARIO/mi-pagina.git
cd mi-pagina
# copiar index.html a esta carpeta y editar nombre y descripción
git add index.html
git commit -m "Primera versión de la página"
git push
```

3. **Settings → Pages → Build and deployment**: *Source* = **Deploy from a branch**, *Branch* = **main** / **(root)**, **Save**.
4. Esperar uno o dos minutos y abrir `https://TU_USUARIO.github.io/mi-pagina/`.
5. Editar algo, hacer commit y push, y ver cómo se actualiza el sitio. La pestaña **Actions** muestra el despliegue.

## Variante: página de perfil

Un repositorio llamado exactamente `TU_USUARIO.github.io` se publica en `https://TU_USUARIO.github.io/`.

## Comprobación

- [ ] La página abre en el navegador.
- [ ] Un cambio subido con `git push` aparece en el sitio.

[Volver al README](../README.md)
