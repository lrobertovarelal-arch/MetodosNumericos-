#!/usr/bin/env python3
"""Suma dos decimales finitos; sin argumentos utiliza 0.1 y 0.2."""
import math
import re
import sys

PATRON = r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?"


def main():
    argumentos = sys.argv[1:]
    if not argumentos:
        a, b = 0.1, 0.2
    elif len(argumentos) == 2:
        if any(re.fullmatch(PATRON, texto) is None for texto in argumentos):
            print("Error: se requieren dos números decimales finitos.", file=sys.stderr)
            return 1
        a, b = map(float, argumentos)
        if not all(map(math.isfinite, (a, b))):
            print("Error: se requieren dos números decimales finitos.", file=sys.stderr)
            return 1
    else:
        print("Uso: python3 suma.py [numero1 numero2]", file=sys.stderr)
        return 1
    resultado = a + b
    if not math.isfinite(resultado):
        print("Error: la suma excede el rango de doble precisión.", file=sys.stderr)
        return 1
    print(f"{resultado:.17g}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
