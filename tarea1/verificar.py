#!/usr/bin/env python3
"""Pruebas reproducibles: python3 -B verificar.py dentro de /trabajo."""
from pathlib import Path
import re
import subprocess
import tempfile

RAIZ = Path(__file__).resolve().parent


def ejecutar(comando, entrada=None):
    return subprocess.run(comando, input=entrada, text=True, capture_output=True, timeout=20)


def compilar(fuente, destino):
    p = ejecutar(['gcc', '-O2', '-std=c17', '-Wall', '-Wextra', '-Werror', str(fuente), '-o', str(destino), '-lm'])
    assert p.returncode == 0 and not p.stderr, p.stderr


def main():
    with tempfile.TemporaryDirectory(prefix='tarea1-') as d:
        suma, calculadora = Path(d)/'suma', Path(d)/'calculadora'
        compilar(RAIZ/'programa1-suma/suma.c', suma)
        compilar(RAIZ/'programa2-calculadora/calculadora.c', calculadora)
        print('Compilación C17 con -Wall -Wextra -Werror: 2/2 sin advertencias')
        programas = [[str(suma)], ['python3', str(RAIZ/'programa1-suma/suma.py')],
                     ['octave-cli', '--quiet', str(RAIZ/'programa1-suma/suma.m')]]
        casos = [([], '0.30000000000000004'), (['0.1', '0.2'], '0.30000000000000004'),
                 (['2', '3'], '5'), (['-2.5', '1.25'], '-1.25'), (['1e2', '.5'], '100.5'),
                 (['+2.', '3'], '5'), (['0', '0'], '0'), (['-0', '0'], '0')]
        for argumentos, esperado in casos:
            for programa in programas:
                p = ejecutar(programa + argumentos)
                assert p.returncode == 0 and p.stdout.strip() == esperado and not p.stderr, (programa, argumentos, p)
            print('Suma', argumentos or 'sin argumentos', '->', esperado, '(C/Python/Octave)')
        invalidos = [['1'], ['1', '2', '3'], ['abc', '2'], ['1x', '2'], ['nan', '1'],
                     ['inf', '2'], ['1e309', '1'], ['1e308', '1e308'], ['', '1'],
                     [' ', '1'], ['0x10', '1'], ['1e', '2'], ['1\n', '2']]
        for argumentos in invalidos:
            for programa in programas:
                p = ejecutar(programa + argumentos)
                assert p.returncode != 0 and not p.stdout and p.stderr, (programa, argumentos, p)
        print(f'Argumentos inválidos: {len(invalidos)} casos rechazados en cada lenguaje')
        casos_calc = [
            ('Suma', '1\n2\n3\n0\n', ['Resultado: 5', 'Hasta luego.'], ['5']),
            ('Resta', '2\n7\n10\n0\n', ['Resultado: -3', 'Hasta luego.'], ['-3']),
            ('Multiplicación', '3\n-2\n4\n0\n', ['Resultado: -8', 'Hasta luego.'], ['-8']),
            ('División', '4\n7\n2\n0\n', ['Resultado: 3.5', 'Hasta luego.'], ['3.5']),
            ('División por cero y recuperación', '4\n5\n0\n1\n2\n3\n0\n', ['Error: división entre cero.', 'Resultado: 5', 'Hasta luego.'], ['5']),
            ('Menú no numérico y recuperación', 'abc\n1\n2\n3\n0\n', ['Error: entrada no numérica.', 'Resultado: 5'], ['5']),
            ('Operando no numérico y recuperación', '1\nabc\n2\n7\n10\n0\n', ['Error: entrada no numérica.', 'Resultado: -3'], ['-3']),
            ('Segundo operando inválido', '1\n2\nabc\n0\n', ['Error: entrada no numérica.', 'Hasta luego.'], []),
            ('Opción inexistente', '9\n0\n', ['Error: opción inválida', 'Hasta luego.'], []),
            ('Opción fraccionaria', '1.5\n0\n', ['Error: opción inválida', 'Hasta luego.'], []),
            ('Texto adicional', '1\n2abc\n0\n', ['Error: se requiere un número finito', 'Hasta luego.'], []),
            ('Operando infinito', '1\ninf\n0\n', ['Error: se requiere un número finito', 'Hasta luego.'], []),
            ('Resultado desbordado', '3\n1e308\n1e308\n0\n', ['Error: resultado fuera del rango', 'Hasta luego.'], []),
            ('Línea larga y recuperación', 'x'*300+'\n1\n2\n3\n0\n', ['Error: entrada demasiado larga.', 'Resultado: 5'], ['5']),
            ('Salir', '0\n', ['Hasta luego.'], []),
            ('Fin de entrada', '', ['Fin de entrada. Hasta luego.'], []),
            ('EOF durante operación', '1\n2\n', ['Fin de entrada. Hasta luego.'], []),
            ('Salida sin salto final', '0', ['Hasta luego.'], []),
        ]
        for nombre, entrada, esperados, resultados in casos_calc:
            p = ejecutar([str(calculadora)], entrada)
            assert p.returncode == 0 and not p.stderr, (nombre, p)
            assert all(texto in p.stdout for texto in esperados), (nombre, p.stdout)
            assert re.findall(r'Resultado: ([^\n]+)', p.stdout) == resultados, (nombre, p.stdout)
            print('Calculadora:', nombre, '-> OK')
        print(f'TOTAL: {len(casos)*3} sumas válidas, {len(invalidos)*3} rechazos y {len(casos_calc)} casos de calculadora; todos pasaron.')


if __name__ == '__main__':
    main()
