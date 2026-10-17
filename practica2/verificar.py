#!/usr/bin/env python3
"""Verificación reproducible: ejecutar desde practica2 con python3 verificar.py."""
import contextlib
import io
from pathlib import Path
import subprocess
import tempfile
import platform
import math
import numpy
import scipy
import matplotlib
from decimal import Decimal, getcontext
import raices as r

with contextlib.redirect_stdout(io.StringIO()):
    resultados = [r.biseccion(r.A,r.B), r.falsa_posicion(r.A,r.B),
                  r.punto_fijo(r.X0), r.newton(r.X0), r.secante_modificada(r.X0,r.DELTA)]
getcontext().prec = 60

def independiente(x):
    # cos(x) y cosh(x) por series de Taylor en aritmética decimal.
    coseno = hiperbolico = Decimal(1)
    termino = Decimal(1)
    for k in range(1, 120):
        termino *= x*x / Decimal((2*k-1)*(2*k))
        hiperbolico += termino
        coseno += termino if k % 2 == 0 else -termino
    return coseno*hiperbolico+1

lo, hi = Decimal('1.8'), Decimal('1.9')
for _ in range(190):
    medio = (lo+hi)/2
    if independiente(medio) > 0:
        lo = medio
    else:
        hi = medio
ref = (lo+hi)/2
assert abs(r.brentq(r.f,r.A,r.B,xtol=1e-14)-float(ref)) < 1e-13
assert r.f(r.A)*r.f(r.B) < 0
for x in numpy.linspace(r.A,r.B,101):
    # Derivada contrastada con diferencias centrales.
    h = 1e-5
    deriv = (r.f(x+h)-r.f(x-h))/(2*h)
    assert math.isclose(r.fp(x),float(deriv),rel_tol=1e-8,abs_tol=1e-8)
for a in resultados:
    assert a['ok'] and a['k'] <= r.NMAX
    assert 0 <= a['ea'] <= r.TOL
    assert abs((float(ref)-a['x'])/float(ref))*100 <= r.TOL
    # Cada método se detiene en el primer error que satisface el criterio.
    assert all(e is None or e > r.TOL for _,_,e in a['historia'][:-1])
    assert all(math.isfinite(x) for _,x,_ in a['historia'])
with tempfile.TemporaryDirectory() as d:
    exe = str(Path(d)/'raices')
    subprocess.run(['gcc','-O2','-std=c17','-Wall','-Wextra','-Werror','-pedantic','raices.c','-lm','-o',exe],check=True)
    c = subprocess.check_output([exe],text=True)
    py = subprocess.check_output(['python3','raices.py'],text=True)
    # Comparación de TODAS las filas impresas y resumen, no sólo raíces finales.
    assert c.splitlines()[1:] == py.split('Verificación con SciPy')[0].rstrip().splitlines()[1:]
    Path('resultados/salida_c.txt').write_text(c)
    Path('resultados/salida_python.txt').write_text(py)
print('Verificación correcta: cinco métodos, tolerancias aproximada y verdadera <= 0.5 %.')
print('Todas las tablas C/Python coinciden a la precisión impresa; C sin advertencias.')
print('Referencia independiente (Decimal, 60 dígitos):',ref)
print('Python',platform.python_version(),'NumPy',numpy.__version__,'SciPy',scipy.__version__,
      'Matplotlib',matplotlib.__version__)
print(subprocess.check_output(['gcc','--version'],text=True).splitlines()[0])
