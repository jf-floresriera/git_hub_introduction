"""
Script de ejemplo para el primer commit.

Muestra un saludo y un resumen del ciclo básico de Git. Lo ejecuta también
GitHub Actions en cada push (ver .github/workflows/verificar.yml).

Uso:
    python ejemplos/hola_github.py
    python ejemplos/hola_github.py --nombre "Ana"
"""

import argparse
import platform

CICLO = [
    ("git add", "prepara los cambios"),
    ("git commit", "guarda una versión con mensaje"),
    ("git push", "sube las versiones a GitHub"),
    ("git pull", "trae lo último de GitHub"),
]


def saludo(nombre: str) -> str:
    return f"Hola, {nombre}. Este script corre en {platform.system()} con Python {platform.python_version()}."


def main() -> None:
    parser = argparse.ArgumentParser(description="Saludo de ejemplo para practicar Git.")
    parser.add_argument("--nombre", default="GitHub", help="nombre para el saludo")
    args = parser.parse_args()

    print(saludo(args.nombre))
    print("\nCiclo básico:")
    ancho = max(len(c) for c, _ in CICLO)
    for comando, descripcion in CICLO:
        print(f"  {comando:<{ancho}}  ->  {descripcion}")


if __name__ == "__main__":
    main()
