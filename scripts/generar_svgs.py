"""
Genera las imágenes animadas (SVG + SMIL) del README.

Todas las figuras se escriben en assets/readme/. No usan fuentes externas ni
JavaScript, así que GitHub las muestra animadas dentro de <img>.

Uso:
    python scripts/generar_svgs.py
"""

from pathlib import Path
from xml.sax.saxutils import escape

SALIDA = Path(__file__).resolve().parents[1] / "assets" / "readme"

# Paleta (tema oscuro de GitHub)
FONDO = "#0d1117"
PANEL = "#161b22"
BORDE = "#30363d"
TEXTO = "#e6edf3"
SUAVE = "#8b949e"
VERDE = "#3fb950"
AZUL = "#2f81f7"
MORADO = "#a371f7"
NARANJA = "#d29922"
CIAN = "#39d0d8"

SANS = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', 'Fira Code', Consolas, 'Liberation Mono', 'Courier New', monospace"


def kt(*vals):
    """keyTimes como texto, recortados a [0, 1] y no decrecientes."""
    out, prev = [], 0.0
    for v in vals:
        v = min(max(v, prev), 1.0)
        out.append(f"{v:.4f}")
        prev = v
    return ";".join(out)


def guardar(nombre, contenido):
    SALIDA.mkdir(parents=True, exist_ok=True)
    (SALIDA / nombre).write_text(contenido, encoding="utf-8")
    print(f"  {nombre:<18} {len(contenido) / 1024:6.1f} KB")


# ---------------------------------------------------------------- divisor
def divisor():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 12" width="1200" height="12" role="presentation">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{AZUL}" stop-opacity="0"/>
      <stop offset="0.5" stop-color="{VERDE}"/>
      <stop offset="1" stop-color="{AZUL}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect x="0" y="5" width="1200" height="2" fill="{BORDE}"/>
  <rect x="-400" y="4" width="400" height="4" rx="2" fill="url(#g)">
    <animate attributeName="x" values="-400;1200" dur="5s" repeatCount="indefinite"/>
  </rect>
</svg>
"""


# ---------------------------------------------------------------- banner
def banner():
    W, H = 1200, 360
    T = 9.0  # ciclo del grafo de commits

    # Grafo de commits a la derecha: main abajo, rama arriba.
    gx0, gy_main, gy_rama = 760, 150, 86
    main_x = [gx0, gx0 + 70, gx0 + 300, gx0 + 370]
    rama_x = [gx0 + 130, gx0 + 190, gx0 + 245]
    partes = []
    # línea main (se dibuja)
    largo_main = main_x[-1] - main_x[0]
    partes.append(
        f'<line x1="{main_x[0]}" y1="{gy_main}" x2="{main_x[-1]}" y2="{gy_main}" stroke="{AZUL}" stroke-width="4" '
        f'stroke-linecap="round" stroke-dasharray="{largo_main}" stroke-dashoffset="{largo_main}">'
        f'<animate attributeName="stroke-dashoffset" values="{largo_main};{largo_main};0;0;{largo_main}" '
        f'keyTimes="{kt(0, 0.02, 0.75, 0.94, 1)}" dur="{T}s" repeatCount="indefinite"/></line>'
    )
    # rama: sale de main_x[1] y vuelve en main_x[2]
    d_rama = (
        f"M{main_x[1]} {gy_main} C{main_x[1] + 30} {gy_main} {rama_x[0] - 30} {gy_rama} {rama_x[0]} {gy_rama} "
        f"L{rama_x[-1]} {gy_rama} C{rama_x[-1] + 25} {gy_rama} {main_x[2] - 25} {gy_main} {main_x[2]} {gy_main}"
    )
    lr = 300
    partes.append(
        f'<path d="{d_rama}" fill="none" stroke="{VERDE}" stroke-width="4" stroke-linecap="round" '
        f'stroke-dasharray="{lr}" stroke-dashoffset="{lr}">'
        f'<animate attributeName="stroke-dashoffset" values="{lr};{lr};0;0;{lr}" '
        f'keyTimes="{kt(0, 0.15, 0.62, 0.94, 1)}" dur="{T}s" repeatCount="indefinite"/></path>'
    )

    def nodo(x, y, color, t):
        return (
            f'<circle cx="{x}" cy="{y}" r="0" fill="{FONDO}" stroke="{color}" stroke-width="4">'
            f'<animate attributeName="r" values="0;0;11;8;8;0" keyTimes="{kt(0, t, t + 0.03, t + 0.06, 0.94, 1)}" '
            f'dur="{T}s" repeatCount="indefinite"/></circle>'
        )

    tiempos_main = [0.03, 0.13, 0.66, 0.74]
    for x, t in zip(main_x, tiempos_main):
        partes.append(nodo(x, gy_main, AZUL, t))
    for x, t in zip(rama_x, [0.30, 0.42, 0.53]):
        partes.append(nodo(x, gy_rama, VERDE, t))

    def etiqueta(x, y, txt, color, t, anchor="middle"):
        return (
            f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="13" fill="{color}" text-anchor="{anchor}" opacity="0">{escape(txt)}'
            f'<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="{kt(0, t, t + 0.05, 0.94, 1)}" '
            f'dur="{T}s" repeatCount="indefinite"/></text>'
        )

    partes.append(etiqueta(main_x[0] - 8, gy_main + 34, "main", AZUL, 0.03, "start"))
    partes.append(etiqueta(rama_x[1], gy_rama - 22, "mi-rama", VERDE, 0.30))
    partes.append(etiqueta(main_x[2], gy_main + 34, "merge", MORADO, 0.66))
    grafo = "\n    ".join(partes)

    # Tubería de 5 etapas abajo (pulso que recorre)
    etapas = ["Crear repo", "Clonar", "Commit", "Push", "Pull request"]
    x0, x1, y = 120, 1080, 290
    paso = (x1 - x0) / (len(etapas) - 1)
    P = 8.0
    tubo = [
        f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{BORDE}" stroke-width="3"/>',
        f'<rect x="{x0}" y="{y - 3}" width="0" height="6" fill="url(#brillo)">'
        f'<animate attributeName="width" values="0;{x1 - x0};{x1 - x0};0" keyTimes="0;0.9;0.93;1" dur="{P}s" repeatCount="indefinite"/></rect>',
        f'<circle cx="{x0}" cy="{y}" r="7" fill="{TEXTO}">'
        f'<animate attributeName="cx" values="{x0};{x1};{x1}" keyTimes="0;0.9;1" dur="{P}s" repeatCount="indefinite"/>'
        f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.88;0.92;1" dur="{P}s" repeatCount="indefinite"/></circle>',
    ]
    for i, nombre in enumerate(etapas):
        cx = x0 + i * paso
        llegada = 0.9 * i / (len(etapas) - 1)
        tubo.append(
            f'<circle cx="{cx:.0f}" cy="{y}" r="24" fill="{FONDO}" stroke="{BORDE}" stroke-width="2"/>'
            f'<circle cx="{cx:.0f}" cy="{y}" r="24" fill="none" stroke="url(#acento)" stroke-width="3" opacity="0.25">'
            f'<animate attributeName="opacity" values="0.25;0.25;1;0.4;0.25" keyTimes="{kt(0, max(llegada - 0.01, 0.0001), llegada + 0.01, llegada + 0.2, 1)}" '
            f'dur="{P}s" repeatCount="indefinite"/></circle>'
            f'<text x="{cx:.0f}" y="{y + 6}" font-family="{MONO}" font-size="15" font-weight="700" fill="{TEXTO}" text-anchor="middle">{i + 1}</text>'
            f'<text x="{cx:.0f}" y="{y + 50}" font-family="{SANS}" font-size="15" fill="{SUAVE}" text-anchor="middle">{nombre}</text>'
        )
    tuberia = "\n    ".join(tubo)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
  <title id="t">Introducción a GitHub: control de versiones y colaboración en la nube</title>
  <desc id="d">Banner animado: un grafo de commits con una rama que se une a main, y un pulso que recorre las etapas crear repositorio, clonar, commit, push y pull request.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{FONDO}"/><stop offset="1" stop-color="#111a2b"/>
    </linearGradient>
    <linearGradient id="acento" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{AZUL}"/><stop offset="1" stop-color="{VERDE}"/>
    </linearGradient>
    <linearGradient id="brillo" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#fff" stop-opacity="0.45"/>
      <stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <pattern id="rejilla" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="{AZUL}" stroke-opacity="0.07" stroke-width="1"/>
      <animateTransform attributeName="patternTransform" type="translate" from="0 0" to="40 40" dur="10s" repeatCount="indefinite"/>
    </pattern>
  </defs>

  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" fill="url(#rejilla)"/>
  <rect x="0" y="0" width="8" height="{H}" fill="url(#acento)"/>

  <text x="60" y="70" font-family="{MONO}" font-size="14" fill="{VERDE}" letter-spacing="4">CONTROL DE VERSIONES  ·  COLABORACIÓN  ·  NUBE</text>
  <text x="60" y="128" font-family="{SANS}" font-size="50" font-weight="700" fill="{TEXTO}">Introducción a GitHub</text>
  <text x="60" y="166" font-family="{SANS}" font-size="21" fill="#c9d1d9">Git en el navegador, el escritorio y la terminal</text>
  <text x="60" y="196" font-family="{SANS}" font-size="15" fill="{SUAVE}">Windows · Linux · comandos esenciales · servicios de la plataforma</text>

  <g>
    {grafo}
  </g>

  <g>
    {tuberia}
  </g>
</svg>
"""


# ---------------------------------------------------------------- escritura tipo máquina
def tipeo(lineas, ancho=1000, alto=56, fs=21, prompt="$ "):
    """Escribe y borra cada línea, con cursor. Una sola animación global."""
    cw = fs * 0.6
    t_char, t_borrar, espera, pausa = 0.055, 0.022, 2.2, 0.35
    duraciones = [len(l) * t_char + espera + len(l) * t_borrar + pausa for l in lineas]
    T = sum(duraciones)
    bloques = []
    inicio = 0.0
    ancho_prompt = len(prompt) * cw
    for i, linea in enumerate(lineas):
        n = len(linea)
        largo = n * cw
        total = largo + ancho_prompt
        x = (ancho - total) / 2
        xt = x + ancho_prompt
        tiempos, valores = [0.0], [0.0]
        for k in range(1, n + 1):
            tiempos.append(inicio + k * t_char)
            valores.append(k * cw)
        fin_escribir = inicio + n * t_char
        for k in range(1, n + 1):
            tiempos.append(fin_escribir + espera + k * t_borrar)
            valores.append((n - k) * cw)
        tiempos.append(T)
        valores.append(0.0)
        ktxt = ";".join(f"{t / T:.5f}" for t in tiempos)
        vtxt = ";".join(f"{v:.1f}" for v in valores)
        cursor_vals = ";".join(f"{xt + v:.1f}" for v in valores)
        fin = inicio + duraciones[i] - pausa
        bloques.append(
            f'<clipPath id="c{i}"><rect x="{xt:.1f}" y="0" width="0" height="{alto}">'
            f'<animate attributeName="width" dur="{T:.2f}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{ktxt}" values="{vtxt}"/></rect></clipPath>\n'
            f'<text x="{x:.1f}" y="{alto * 0.64:.0f}" font-family="{MONO}" font-size="{fs}" fill="{SUAVE}" opacity="0">{escape(prompt)}'
            f'<animate attributeName="opacity" dur="{T:.2f}s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;{inicio / T:.5f};{fin / T:.5f}" values="0;1;0"/></text>\n'
            f'<text clip-path="url(#c{i})" x="{xt:.1f}" y="{alto * 0.64:.0f}" font-family="{MONO}" font-size="{fs}" fill="url(#tg)" '
            f'textLength="{largo:.1f}" lengthAdjust="spacingAndGlyphs" xml:space="preserve">{escape(linea)}</text>\n'
            f'<rect y="{alto * 0.24:.0f}" width="3" height="{alto * 0.52:.0f}" fill="{VERDE}" x="{xt:.1f}" opacity="0">'
            f'<animate attributeName="x" dur="{T:.2f}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{ktxt}" values="{cursor_vals}"/>'
            f'<animate attributeName="opacity" dur="{T:.2f}s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;{inicio / T:.5f};{fin / T:.5f}" values="0;1;0"/></rect>'
        )
        inicio += duraciones[i]
    resumen = "; ".join(lineas)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{ancho}" height="{alto}" viewBox="0 0 {ancho} {alto}" role="img" aria-label="{escape(resumen)}">
<title>{escape(resumen)}</title>
<defs><linearGradient id="tg" x1="0" x2="1"><stop offset="0" stop-color="#7ee787"/><stop offset="1" stop-color="{CIAN}"/></linearGradient></defs>
{chr(10).join(bloques)}
</svg>
"""


# ---------------------------------------------------------------- terminal
def terminal():
    """Sesión de terminal que se escribe sola: clonar, rama, commit y push."""
    sesion = [
        ("cmd", "git clone https://github.com/jf-floresriera/git_hub_introduction.git"),
        ("out", "Cloning into 'git_hub_introduction'... done."),
        ("cmd", "cd git_hub_introduction"),
        ("cmd", "git switch -c mi-rama"),
        ("out", "Switched to a new branch 'mi-rama'"),
        ("cmd", 'echo "Hola, GitHub" > saludo.txt'),
        ("cmd", "git status --short"),
        ("new", "?? saludo.txt"),
        ("cmd", "git add saludo.txt"),
        ("cmd", 'git commit -m "Agrega saludo"'),
        ("out", "[mi-rama 3f2a1c9] Agrega saludo"),
        ("out", " 1 file changed, 1 insertion(+)"),
        ("cmd", "git push -u origin mi-rama"),
        ("ok", " * [new branch]      mi-rama -> mi-rama"),
    ]
    W, fs, lh = 1100, 17, 29
    cw = fs * 0.6
    top, left = 70, 34
    H = top + len(sesion) * lh + 30
    t_char, t_salida, pausa_cmd = 0.045, 0.35, 0.45
    # Línea de tiempo
    eventos, t = [], 0.6
    for tipo, txt in sesion:
        if tipo == "cmd":
            eventos.append((t, t + len(txt) * t_char))
            t += len(txt) * t_char + pausa_cmd
        else:
            eventos.append((t + t_salida - 0.3, t + t_salida - 0.3))
            t += t_salida
    fin_contenido = t
    T = fin_contenido + 4.0
    fade = (T - 0.6) / T

    colores = {"out": SUAVE, "new": "#f85149", "ok": VERDE}
    filas = []
    for i, ((tipo, txt), (t0, t1)) in enumerate(zip(sesion, eventos)):
        y = top + i * lh
        if tipo == "cmd":
            px = left
            xt = px + 2 * cw
            n = len(txt)
            tiempos = [0.0] + [t0 + k * t_char for k in range(1, n + 1)] + [T * fade, T]
            valores = [0.0] + [k * cw for k in range(1, n + 1)] + [n * cw, 0.0]
            ktxt = ";".join(f"{v / T:.5f}" for v in tiempos)
            vtxt = ";".join(f"{v:.1f}" for v in valores)
            filas.append(
                f'<clipPath id="l{i}"><rect x="{xt:.1f}" y="{y - lh + 6}" width="0" height="{lh}">'
                f'<animate attributeName="width" dur="{T:.2f}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{ktxt}" values="{vtxt}"/></rect></clipPath>'
                f'<text x="{px}" y="{y}" font-family="{MONO}" font-size="{fs}" fill="{VERDE}" opacity="0">$'
                f'<animate attributeName="opacity" dur="{T:.2f}s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;{max(t0 - 0.25, 0.01) / T:.5f};{fade:.5f}" values="0;1;0"/></text>'
                f'<text clip-path="url(#l{i})" x="{xt:.1f}" y="{y}" font-family="{MONO}" font-size="{fs}" fill="{TEXTO}" '
                f'textLength="{n * cw:.1f}" lengthAdjust="spacingAndGlyphs" xml:space="preserve">{escape(txt)}</text>'
            )
            # cursor mientras se escribe
            cur_t = [0.0] + [t0 + k * t_char for k in range(0, n + 1)] + [t1 + 0.2, T]
            cur_v = [xt] + [xt + k * cw for k in range(0, n + 1)] + [xt + n * cw, xt]
            filas.append(
                f'<rect x="{xt:.1f}" y="{y - fs + 2}" width="{cw:.1f}" height="{fs + 3}" fill="{VERDE}" opacity="0">'
                f'<animate attributeName="x" dur="{T:.2f}s" repeatCount="indefinite" calcMode="discrete" '
                f'keyTimes="{";".join(f"{v / T:.5f}" for v in cur_t)}" values="{";".join(f"{v:.1f}" for v in cur_v)}"/>'
                f'<animate attributeName="opacity" dur="{T:.2f}s" repeatCount="indefinite" calcMode="discrete" '
                f'keyTimes="0;{max(t0 - 0.25, 0.01) / T:.5f};{(t1 + 0.2) / T:.5f}" values="0;0.75;0"/></rect>'
            )
        else:
            filas.append(
                f'<text x="{left}" y="{y}" font-family="{MONO}" font-size="{fs}" fill="{colores[tipo]}" opacity="0" xml:space="preserve">{escape(txt)}'
                f'<animate attributeName="opacity" dur="{T:.2f}s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;{t0 / T:.5f};{fade:.5f}" values="0;1;0"/></text>'
            )
    # cursor final parpadeando
    yfin = top + len(sesion) * lh
    filas.append(
        f'<text x="{left}" y="{yfin}" font-family="{MONO}" font-size="{fs}" fill="{VERDE}" opacity="0">$'
        f'<animate attributeName="opacity" dur="{T:.2f}s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;{fin_contenido / T:.5f};{fade:.5f}" values="0;1;0"/></text>'
        f'<rect x="{left + 2 * cw:.1f}" y="{yfin - fs + 2}" width="{cw:.1f}" height="{fs + 3}" fill="{VERDE}" opacity="0">'
        f'<animate attributeName="opacity" dur="{T:.2f}s" repeatCount="indefinite" calcMode="discrete" '
        f'keyTimes="{kt(0, fin_contenido / T, (fin_contenido + 0.5) / T, (fin_contenido + 1) / T, (fin_contenido + 1.5) / T, (fin_contenido + 2) / T, (fin_contenido + 2.5) / T, fade)}" '
        f'values="0;0.8;0;0.8;0;0.8;0;0"/></rect>'
    )
    resumen = "; ".join(t for k, t in sesion if k == "cmd")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
  <title id="t">Sesión de terminal: del clon al push</title>
  <desc id="d">Comandos que se escriben solos: {escape(resumen)}</desc>
  <rect width="{W}" height="{H}" rx="14" fill="{FONDO}" stroke="{BORDE}"/>
  <rect width="{W}" height="40" rx="14" fill="{PANEL}"/>
  <rect y="26" width="{W}" height="14" fill="{PANEL}"/>
  <line x1="0" y1="40" x2="{W}" y2="40" stroke="{BORDE}"/>
  <circle cx="26" cy="20" r="6" fill="#f85149"/><circle cx="46" cy="20" r="6" fill="{NARANJA}"/><circle cx="66" cy="20" r="6" fill="{VERDE}"/>
  <text x="{W / 2:.0f}" y="25" font-family="{MONO}" font-size="13" fill="{SUAVE}" text-anchor="middle">bash  ·  Git Bash (Windows)  ·  terminal (Linux)</text>
  {chr(10).join(filas)}
</svg>
"""


# ---------------------------------------------------------------- flujo git
def flujo():
    W, H = 1200, 470
    T = 10.0
    cajas = [
        ("Directorio de trabajo", "tus archivos, tal como", "los editas", AZUL),
        ("Área de preparación", "staging: lo que irá", "en el próximo commit", NARANJA),
        ("Repositorio local", "historial de commits", "en tu equipo (.git)", VERDE),
        ("Repositorio remoto", "GitHub: la copia en la", "nube para colaborar", MORADO),
    ]
    bw, bh, by = 226, 150, 110
    xs = [30, 335, 640, 944]
    comandos = ["git add", "git commit", "git push"]
    partes = []
    # cajas
    for i, ((tit, s1, s2, col), x) in enumerate(zip(cajas, xs)):
        llegada = [0.02, 0.22, 0.42, 0.62][i]
        partes.append(
            f'<rect x="{x}" y="{by}" width="{bw}" height="{bh}" rx="14" fill="{PANEL}" stroke="{BORDE}" stroke-width="2"/>'
            f'<rect x="{x}" y="{by}" width="{bw}" height="{bh}" rx="14" fill="none" stroke="{col}" stroke-width="3" opacity="0.2">'
            f'<animate attributeName="opacity" values="0.2;0.2;1;0.35;0.2" keyTimes="{kt(0, llegada, llegada + 0.04, llegada + 0.18, 1)}" dur="{T}s" repeatCount="indefinite"/></rect>'
            f'<rect x="{x}" y="{by}" width="{bw}" height="6" rx="3" fill="{col}"/>'
            f'<text x="{x + bw / 2}" y="{by + 48}" font-family="{SANS}" font-size="19" font-weight="700" fill="{TEXTO}" text-anchor="middle">{tit}</text>'
            f'<text x="{x + bw / 2}" y="{by + 84}" font-family="{SANS}" font-size="15" fill="{SUAVE}" text-anchor="middle">{s1}</text>'
            f'<text x="{x + bw / 2}" y="{by + 106}" font-family="{SANS}" font-size="15" fill="{SUAVE}" text-anchor="middle">{s2}</text>'
        )
    # flechas de ida
    ya = by + bh / 2
    for i, cmd in enumerate(comandos):
        xa, xb = xs[i] + bw + 6, xs[i + 1] - 10
        partes.append(
            f'<line x1="{xa}" y1="{ya}" x2="{xb}" y2="{ya}" stroke="{SUAVE}" stroke-width="2" marker-end="url(#punta)"/>'
            f'<text x="{(xa + xb) / 2}" y="{ya - 14}" font-family="{MONO}" font-size="12" fill="{TEXTO}" text-anchor="middle">{cmd}</text>'
        )
    # ficha (archivo) que viaja
    fx = [xs[0] + bw / 2, xs[1] + bw / 2, xs[2] + bw / 2, xs[3] + bw / 2]
    vals = ";".join(f"{v - 14:.0f}" for v in [fx[0], fx[0], fx[1], fx[1], fx[2], fx[2], fx[3], fx[3]])
    partes.append(
        f'<g opacity="0"><animate attributeName="opacity" values="0;1;1;0;0" keyTimes="{kt(0, 0.02, 0.7, 0.74, 1)}" dur="{T}s" repeatCount="indefinite"/>'
        f'<g><animateTransform attributeName="transform" type="translate" '
        f'values="{";".join(f"{v - 14:.0f} {by + bh - 30}" for v in [fx[0], fx[0], fx[1], fx[1], fx[2], fx[2], fx[3], fx[3]])}" '
        f'keyTimes="{kt(0, 0.08, 0.2, 0.28, 0.4, 0.48, 0.6, 1)}" dur="{T}s" repeatCount="indefinite"/>'
        f'<path d="M0 0H18L28 10V36H0Z" fill="{TEXTO}"/><path d="M18 0V10H28" fill="none" stroke="{FONDO}" stroke-width="1.5"/>'
        f'<rect x="5" y="16" width="16" height="2.5" fill="{FONDO}"/><rect x="5" y="23" width="12" height="2.5" fill="{FONDO}"/></g></g>'
    )
    # flechas de vuelta (abajo)
    yb1, yb2 = by + bh + 60, by + bh + 120
    # fetch: remoto -> local
    partes.append(
        f'<path d="M{xs[3] + bw / 2} {by + bh + 8} V{yb1} H{xs[2] + bw / 2} V{by + bh + 14}" fill="none" stroke="{MORADO}" stroke-width="2" marker-end="url(#puntaM)"/>'
        f'<text x="{(xs[3] + xs[2] + bw) / 2}" y="{yb1 - 10}" font-family="{MONO}" font-size="13" fill="{TEXTO}" text-anchor="middle">git fetch</text>'
    )
    # pull: remoto -> trabajo
    partes.append(
        f'<path d="M{xs[3] + bw / 2 + 30} {by + bh + 8} V{yb2} H{xs[0] + bw / 2} V{by + bh + 14}" fill="none" stroke="{MORADO}" stroke-width="2" marker-end="url(#puntaM)"/>'
        f'<text x="{(xs[0] + xs[3] + bw) / 2}" y="{yb2 - 10}" font-family="{MONO}" font-size="13" fill="{TEXTO}" text-anchor="middle">git pull  (fetch + merge)   ·   git clone la primera vez</text>'
    )
    # punto que vuelve por pull
    camino = f"M{xs[3] + bw / 2 + 30} {by + bh + 8} V{yb2} H{xs[0] + bw / 2} V{by + bh + 14}"
    partes.append(
        f'<circle r="7" fill="{MORADO}" opacity="0">'
        f'<animateMotion path="{camino}" dur="{T}s" repeatCount="indefinite" keyPoints="0;0;1;1" keyTimes="{kt(0, 0.7, 0.95, 1)}" calcMode="linear"/>'
        f'<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="{kt(0, 0.7, 0.72, 0.94, 0.96)}" dur="{T}s" repeatCount="indefinite"/></circle>'
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
  <title id="t">Cómo viaja un cambio en Git</title>
  <desc id="d">Un archivo pasa del directorio de trabajo al área de preparación con git add, al repositorio local con git commit y a GitHub con git push. De vuelta, git fetch trae el historial remoto y git pull lo integra en tus archivos.</desc>
  <defs>
    <marker id="punta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5L0 10Z" fill="{SUAVE}"/></marker>
    <marker id="puntaM" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5L0 10Z" fill="{MORADO}"/></marker>
  </defs>
  <rect width="{W}" height="{H}" rx="14" fill="{FONDO}"/>
  <text x="40" y="50" font-family="{SANS}" font-size="22" font-weight="700" fill="{TEXTO}">Cómo viaja un cambio en Git</text>
  <text x="40" y="78" font-family="{SANS}" font-size="15" fill="{SUAVE}">Tres zonas en tu equipo y una en la nube. Los comandos mueven los cambios de una a otra.</text>
  {chr(10).join(partes)}
</svg>
"""


# ---------------------------------------------------------------- ramas
def ramas():
    W, H = 1200, 330
    T = 12.0
    ym, yr = 230, 120
    main = [(110, 0.04, "a1"), (250, 0.10, "b2"), (880, 0.62, "m5"), (1040, 0.70, "f6")]
    rama = [(420, 0.26, "c3"), (560, 0.36, "d4"), (700, 0.46, "e5")]
    p = []
    L = 930
    p.append(
        f'<line x1="110" y1="{ym}" x2="1040" y2="{ym}" stroke="{AZUL}" stroke-width="5" stroke-linecap="round" stroke-dasharray="{L}" stroke-dashoffset="{L}">'
        f'<animate attributeName="stroke-dashoffset" values="{L};{L};0;0;{L}" keyTimes="{kt(0, 0.04, 0.72, 0.93, 1)}" dur="{T}s" repeatCount="indefinite"/></line>'
    )
    d = f"M250 {ym} C320 {ym} 340 {yr} 420 {yr} L700 {yr} C780 {yr} 800 {ym} 880 {ym}"
    LR = 720
    p.append(
        f'<path d="{d}" fill="none" stroke="{VERDE}" stroke-width="5" stroke-linecap="round" stroke-dasharray="{LR}" stroke-dashoffset="{LR}">'
        f'<animate attributeName="stroke-dashoffset" values="{LR};{LR};0;0;{LR}" keyTimes="{kt(0, 0.12, 0.6, 0.93, 1)}" dur="{T}s" repeatCount="indefinite"/></path>'
    )

    def nodo(x, y, col, t, h):
        return (
            f'<circle cx="{x}" cy="{y}" r="0" fill="{FONDO}" stroke="{col}" stroke-width="5">'
            f'<animate attributeName="r" values="0;0;16;12;12;0" keyTimes="{kt(0, t, t + 0.025, t + 0.05, 0.93, 1)}" dur="{T}s" repeatCount="indefinite"/></circle>'
            f'<text x="{x}" y="{y + 5}" font-family="{MONO}" font-size="11" fill="{col}" text-anchor="middle" opacity="0">{h}'
            f'<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="{kt(0, t + 0.03, t + 0.05, 0.93, 1)}" dur="{T}s" repeatCount="indefinite"/></text>'
        )

    for x, t, h in main:
        p.append(nodo(x, ym, AZUL, t, h))
    for x, t, h in rama:
        p.append(nodo(x, yr, VERDE, t, h))

    def nota(x, y, txt, col, t, anchor="middle", fs=14):
        return (
            f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{fs}" fill="{col}" text-anchor="{anchor}" opacity="0">{escape(txt)}'
            f'<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="{kt(0, t, t + 0.04, 0.93, 1)}" dur="{T}s" repeatCount="indefinite"/></text>'
        )

    p.append(nota(60, ym + 6, "main", AZUL, 0.02, "end", 15))
    p.append(nota(300, yr - 30, "git switch -c mi-rama", VERDE, 0.12, "start"))
    p.append(nota(560, yr + 48, "git add  +  git commit", SUAVE, 0.30))
    p.append(nota(700, yr - 30, "git push -u origin mi-rama", VERDE, 0.50, "start"))
    p.append(nota(880, ym + 48, "pull request  +  merge", MORADO, 0.62))
    p.append(nota(1040, ym + 48, "git pull", AZUL, 0.70))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
  <title id="t">Trabajar con ramas</title>
  <desc id="d">Se crea una rama desde main, se hacen tres commits, se sube con push, se integra a main con un pull request y se actualiza la copia local con git pull.</desc>
  <rect width="{W}" height="{H}" rx="14" fill="{FONDO}"/>
  <text x="40" y="46" font-family="{SANS}" font-size="22" font-weight="700" fill="{TEXTO}">Trabajar con ramas</text>
  <text x="40" y="72" font-family="{SANS}" font-size="15" fill="{SUAVE}">Cada cambio grande va en su propia rama; main queda estable hasta que el cambio se revisa e integra.</text>
  {chr(10).join(p)}
</svg>
"""


# ---------------------------------------------------------------- servicios
def servicios():
    W, H = 1200, 440
    T = 15.0
    items = [
        ("REPOS", "Repositorios", "código, historial y", "versiones públicas o privadas", AZUL),
        ("ISSUES", "Issues", "tareas, errores e ideas", "con etiquetas y responsables", VERDE),
        ("PR", "Pull requests", "proponer cambios, revisarlos", "y discutirlos línea a línea", MORADO),
        ("ACTIONS", "Actions", "automatizar pruebas,", "compilaciones y despliegues", NARANJA),
        ("PAGES", "Pages", "publicar un sitio web", "estático desde el repo", CIAN),
        ("SPACES", "Codespaces", "entorno de desarrollo", "completo en el navegador", AZUL),
        ("PROJECTS", "Projects", "tableros y tablas para", "planificar el trabajo", VERDE),
        ("COPILOT", "Copilot", "asistente de código", "con plan gratuito", MORADO),
        ("WIKI", "Wiki y Discussions", "documentación y foro", "de la comunidad", NARANJA),
        ("SECURITY", "Dependabot", "alertas y actualizaciones", "de dependencias", CIAN),
    ]
    cw, ch, gap = 214, 160, 18
    x0, y0 = (W - (5 * cw + 4 * gap)) / 2, 100
    p = []
    n = len(items)
    for i, (tag, tit, d1, d2, col) in enumerate(items):
        fila, colm = divmod(i, 5)
        x = x0 + colm * (cw + gap)
        y = y0 + fila * (ch + gap)
        t = i / n
        p.append(
            f'<g><rect x="{x:.0f}" y="{y}" width="{cw}" height="{ch}" rx="12" fill="{PANEL}" stroke="{BORDE}" stroke-width="1.5"/>'
            f'<rect x="{x:.0f}" y="{y}" width="{cw}" height="{ch}" rx="12" fill="{col}" fill-opacity="0.08" stroke="{col}" stroke-width="2.5" opacity="0">'
            f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="{kt(0, t, t + 0.02, t + 0.08, t + 0.12, 1)}" dur="{T}s" repeatCount="indefinite"/></rect>'
            f'<rect x="{x + 18:.0f}" y="{y + 20}" width="{len(tag) * 8.4 + 16:.0f}" height="24" rx="6" fill="{col}" fill-opacity="0.18"/>'
            f'<text x="{x + 26:.0f}" y="{y + 37}" font-family="{MONO}" font-size="13" font-weight="700" fill="{col}">{tag}</text>'
            f'<text x="{x + 18:.0f}" y="{y + 80}" font-family="{SANS}" font-size="19" font-weight="700" fill="{TEXTO}">{escape(tit)}</text>'
            f'<text x="{x + 18:.0f}" y="{y + 110}" font-family="{SANS}" font-size="13.5" fill="{SUAVE}">{escape(d1)}</text>'
            f'<text x="{x + 18:.0f}" y="{y + 130}" font-family="{SANS}" font-size="13.5" fill="{SUAVE}">{escape(d2)}</text></g>'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
  <title id="t">Servicios de la plataforma GitHub</title>
  <desc id="d">Repositorios, Issues, Pull requests, Actions, Pages, Codespaces, Projects, Copilot, Wiki y Discussions, Dependabot.</desc>
  <rect width="{W}" height="{H}" rx="14" fill="{FONDO}"/>
  <text x="{x0:.0f}" y="50" font-family="{SANS}" font-size="22" font-weight="700" fill="{TEXTO}">Más allá de guardar código</text>
  <text x="{x0:.0f}" y="76" font-family="{SANS}" font-size="15" fill="{SUAVE}">Servicios que vienen con la cuenta gratuita (algunos con cuota mensual).</text>
  {chr(10).join(p)}
</svg>
"""


# ---------------------------------------------------------------- pie
def pie():
    W, H = 1200, 120
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Haz commit temprano, haz commit seguido">
  <defs>
    <linearGradient id="a" x1="0" x2="1"><stop offset="0" stop-color="{AZUL}"/><stop offset="1" stop-color="{VERDE}"/></linearGradient>
  </defs>
  <rect width="{W}" height="{H}" rx="14" fill="{FONDO}"/>
  <g stroke="url(#a)" stroke-width="3" fill="none" opacity="0.6">
    <path d="M60 60 H1140" stroke-dasharray="6 10">
      <animate attributeName="stroke-dashoffset" values="0;-160" dur="6s" repeatCount="indefinite"/>
    </path>
  </g>
  <rect x="380" y="38" width="440" height="44" rx="22" fill="{FONDO}" stroke="{BORDE}"/>
  <text x="600" y="67" font-family="{MONO}" font-size="16" fill="{TEXTO}" text-anchor="middle">haz commit temprano, haz commit seguido</text>
</svg>
"""


if __name__ == "__main__":
    print("Generando SVG en", SALIDA)
    guardar("divider.svg", divisor())
    guardar("banner.svg", banner())
    guardar(
        "typing.svg",
        tipeo(
            [
                "git clone   →  trae un repositorio a tu equipo",
                "git add     →  prepara los cambios",
                'git commit  →  guarda una versión con mensaje',
                "git push    →  sube tus versiones a GitHub",
                "git pull    →  trae lo último de la nube",
            ]
        ),
    )
    guardar("terminal.svg", terminal())
    guardar("flujo-git.svg", flujo())
    guardar("ramas.svg", ramas())
    guardar("servicios.svg", servicios())
    guardar("footer.svg", pie())
