# Práctica 1 · La serie de Maclaurin y el criterio de paro

**UEA 1151039 · Métodos Numéricos en Ingeniería · Trimestre 26-O · UAM Azcapotzalco**
**Profesor:** M. en C. Gabriel Hurtado Avilés

| | |
|---|---|
| Equipo | |
| Integrantes (nombre, matrícula y licenciatura) | |
| Repositorio de la Tarea 1 de | |
| Fecha | |

## 1. Octave y Python

![Octave](img/01-octave.png)
![Python](img/02-python.png)

¿Coinciden con la lámina 25 de la unidad I?

Las salidas de C, Python y Octave coinciden entre sí y con la tabla transcrita en
`COMO_CORRER.md`: 6 términos, aproximación 1.648697916666667 y error verdadero
0.00141649 %. La lámina oficial no está incluida en el repositorio; queda pendiente
compararla directamente y agregar las capturas de las ejecuciones.

## 2. Las dos líneas que completamos en `maclaurin.c`

```c
/* COMPLETAR 1 */
termino = termino * X / n;
/* COMPLETAR 2 */
ea = fabs((aprox - anterior) / aprox) * 100.0;
```

La primera línea obtiene el siguiente término de la serie por recurrencia. La
segunda calcula el error relativo aproximado en porcentaje y utiliza `anterior`,
eliminando su advertencia de compilación. Antes, `ea = 0.0` provocaba el paro tras
un término. Se conservan el ciclo, la impresión y el criterio original:
εs = 0.5 × 10^(2 − CIFRAS) %, con paro cuando εa ≤ εs o n ≥ NMAX.

![C](img/03-c.png)

## 3. Más cifras significativas

| Cifras | εs (%) | Términos | Aproximación | Error verdadero (%) |
|---|---|---|---|---|
| 3 | 0.05 | 6 | 1.648697916666667 | 0.00141649 |
| 6 | 0.00005 | 9 | 1.648721265035962 | 3.43549e-07 |
| 17 | 5e-16 | 16 | 1.648721270700128 | 2.69354e-14 |

Resultados ejecutados en el contenedor `metodos_equipo` con GCC 12.2.0, Python
3.11.2 y Octave 7.3.0. Se usaron copias temporales con `CIFRAS` igual a 3, 6 y 17;
las tablas y los resúmenes coincidieron en los tres lenguajes. El error verdadero
mostrado se calcula contra `exp(0.5)` en precisión de máquina, no contra una
referencia de precisión arbitraria.

Con 17 cifras, εa termina en 0 porque el siguiente término ya no cambia la suma
representable. Esto no demuestra 17 cifras correctas. La salida de 15 decimales
tampoco basta para medirlas exactamente. Los errores aproximados finales son
0.0157953 %, 5.87614e-06 % y 0 %, respectivamente.

### Verificación y material gráfico

La compilación con `-Wall -Wextra -Werror` pasó sin advertencias. También se probó
una copia temporal con `NMAX = 2`: terminó con el mensaje de tolerancia no
alcanzada, verificando el límite de iteraciones. Los comandos para ejecutar y
comparar las salidas están en `COMO_CORRER.md`.

Este README solicita imágenes de las ejecuciones de Octave, Python y C; no
especifica gráficas de convergencia ni de error. No se generaron gráficas ni se
inventaron capturas. Si el documento oficial solicita otras figuras, hace falta
consultarlo antes de prepararlas.

1. ¿Cuántos términos hacen falta en cada caso?
2. En cada fila de la tabla, ¿εa es mayor o menor que εt? ¿Por qué conviene detenerse con εa?
3. Con 17 cifras el programa termina. ¿Cuántas cifras del resultado son correctas en realidad?
   Relaciónenlo con 0.1 + 0.2 de la Tarea 1.

## Uso de inteligencia artificial

Codex: completar las dos líneas de C, comparar las ejecuciones en el contenedor
y documentar los resultados y las limitaciones del material disponible.

## Referencias

- `maclaurin.py` y `maclaurin.m`: implementaciones de referencia de la práctica.
- `COMO_CORRER.md`: comandos y tabla esperada incluida en el repositorio.

