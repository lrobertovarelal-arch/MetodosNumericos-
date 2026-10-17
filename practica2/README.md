# Práctica 2 · Raíces de ecuaciones no lineales

**UEA 1151039 · Métodos Numéricos en Ingeniería · Trimestre 26-O · UAM Azcapotzalco**
**Profesor:** M. en C. Gabriel Hurtado Avilés

| | |
|---|---|
| Equipo | Trabajo individual |
| Integrantes (nombre, matrícula y licenciatura) | Luis Roberto Varela López · 2253001715 · Ingeniería Mecánica |
| Ecuación asignada | Pendiente de asignación por el profesor |
| Fecha | 17 de octubre de 2026 |

---

## 1. Octave y Python con el paracaidista

Capturas de `octave raices.m` y de `python3 raices.py` sin cambiar nada. Sus tablas
coinciden con las de las láminas de la unidad II.

![Octave](img/01-octave.png)
![Python](img/02-python.png)

## 2. Las cinco líneas que completamos en `raices.c`

```c
/* COMPLETAR 1: Error relativo aproximado */
return fabs((nuevo - anterior) / nuevo) * 100.0;

/* COMPLETAR 2: Falsa posición */
x = b - f(b) * (a - b) / (f(a) - f(b));

/* COMPLETAR 3: Punto fijo */
x_nuevo = g(x);

/* COMPLETAR 4: Newton-Raphson */
x_nuevo = x - f(x) / fp(x);

/* COMPLETAR 5: Secante modificada */
x_nuevo = x - delta * f(x) / (f(x + delta) - f(x));
```


![Compilación](img/03-c-compilacion.png)
![Ejecución en C](img/04-c-ejecucion.png)

¿Coinciden las tablas de C con las de Octave y Python? Sí / No, y en qué.

**Comparación de resultados**

Sí. Los programas de C y Octave produjeron tablas idénticas en los valores mostrados, incluyendo las aproximaciones, los errores relativos y el número de iteraciones. El programa de Python también obtuvo las mismas raíces e iteraciones.

| Método | Raíz aproximada | Iteraciones | Error aproximado (%) |
|---|---:|---:|---:|
| Bisección | 14.812500 | 6 | 0.4219 |
| Falsa posición | 14.781695 | 3 | 0.0845 |
| Punto fijo | 14.762313 | 4 | 0.3102 |
| Newton-Raphson | 14.780204 | 3 | 0.0102 |
| Secante modificada | 14.780206 | 3 | 0.0073 |

Los cinco métodos alcanzaron la tolerancia establecida de 0.5 %. Bisección necesitó seis iteraciones, mientras que falsa posición, Newton-Raphson y secante modificada necesitaron tres. Las diferencias entre las raíces aproximadas se deben a que cada método sigue un procedimiento distinto y se detiene cuando satisface el criterio de error relativo aproximado.
## 3. Las gráficas de Python

![Función](img/funcion.png)
![Convergencia](img/convergencia.png)

### Interpretación de las gráficas

**Gráfica de la función (`funcion.png`)**

La primera gráfica representa la función del problema del paracaidista en el intervalo [12, 16], junto con la recta horizontal y = 0 y las raíces aproximadas obtenidas mediante los cinco métodos numéricos.

Se observa que las aproximaciones se encuentran alrededor de 14.78 kg/s, valor correspondiente al coeficiente de arrastre buscado. Los marcadores aparecen próximos entre sí porque todos los métodos alcanzaron la tolerancia establecida.

**Gráfica de convergencia (`convergencia.png`)**

La segunda gráfica muestra la evolución del error relativo aproximado en función del número de iteración, utilizando una escala logarítmica en el eje vertical.

La línea horizontal representa la tolerancia del 0.5 %. Los métodos de falsa posición, Newton-Raphson y secante modificada alcanzaron dicha tolerancia en tres iteraciones; punto fijo necesitó cuatro y bisección seis.

La comparación permite observar que la rapidez de convergencia depende del método utilizado. En este problema, Newton-Raphson y secante modificada lograron errores aproximados particularmente pequeños con pocas iteraciones.

## 4. Nuestra ecuación

| | |
|---|---|
| f(x) | |
| f'(x) | |
| g(x) | |
| Intervalo [a, b] | |
| x₀ y δ | |
| Tolerancia | εa ≤ 0.5 % |

![C con nuestra ecuación](img/05-c-ecuacion.png)
![Python con nuestra ecuación](img/06-python-ecuacion.png)

### Tablas (salida de C)

**Bisección**

| k | a | b | x | f(x) | εa (%) |
|---|---|---|---|---|---|
| 1 | | | | | — |
| 2 | | | | | |

**Falsa posición**

| k | a | b | x | f(x) | εa (%) |
|---|---|---|---|---|---|
| 1 | | | | | — |
| 2 | | | | | |

**Punto fijo**

| k | x | f(x) | εa (%) |
|---|---|---|---|
| 0 | | | — |
| 1 | | | |

**Newton-Raphson**

| k | x | f(x) | εa (%) |
|---|---|---|---|
| 0 | | | — |
| 1 | | | |

**Secante modificada**

| k | x | f(x) | εa (%) |
|---|---|---|---|
| 0 | | | — |
| 1 | | | |

Agreguen las filas que hagan falta.

### Resumen

| Método | Raíz | Iteraciones | εa (%) | f(raíz) | Error verdadero (%) |
|---|---|---|---|---|---|
| Bisección | | | | | |
| Falsa posición | | | | | |
| Punto fijo | | | | | |
| Newton-Raphson | | | | | |
| Secante modificada | | | | | |

Raíz de referencia (SciPy):

### Análisis

¿Qué método necesitó menos iteraciones y cuál más? ¿Por qué los cinco no dan
exactamente el mismo número? ¿Alguno no alcanzó la tolerancia o tardó mucho más que
los otros? ¿Por qué?

## 5. Cada integrante en su computadora

Cada integrante corre `raices.c` con la ecuación del equipo en su propia computadora y sube
su captura con un commit propio (ver `COMO_CORRER.md`, sección 7).

| Integrante | Usuario de GitHub | Captura |
|---|---|---|
| | | `img/07-integrante-apellido.png` |
| | | |
| | | |

![Integrante 1](img/07-integrante-apellido.png)

## Uso de inteligencia artificial

Ninguno / Cuál y para qué.

Se utilizó ChatGPT (OpenAI) como herramienta de apoyo durante el desarrollo de la práctica. Su uso consistió en explicar los fundamentos matemáticos de los cinco métodos numéricos, orientar la implementación de las fórmulas faltantes en C, apoyar la programación de las gráficas en Python y colaborar en la interpretación de los resultados y la redacción de la documentación.

Los programas se ejecutaron en el entorno Docker del estudiante y sus resultados se comprobaron mediante la comparación de las tablas generadas en Octave, Python y C.

## Referencias

- Chapra, S. C., y Canale, R. P. (2015). *Métodos numéricos para ingenieros* (7.ª ed.). McGraw-Hill Education.
- Burden, R. L., y Faires, J. D. (2011). *Análisis numérico* (9.ª ed.). Cengage Learning.
- Hurtado Avilés, G. (2026). *Métodos Numéricos en Ingeniería, Unidad II: Raíces de ecuaciones no lineales*. Material del curso, UAM Azcapotzalco.
- OpenAI. (2026). *ChatGPT*. https://chatgpt.com/
