# Cómo correr los programas de la Práctica 1

**UEA 1151039 · Métodos Numéricos en Ingeniería · 26-O · UAM Azcapotzalco**

Los tres programas suman la serie de Maclaurin de eˣ en x = 0.5 hasta cumplir el
criterio de Scarborough, y deben imprimir **la misma tabla**. Es el ciclo de la lámina 24
de la unidad I, y la tabla es la de la lámina 25.

| Archivo | Cómo viene | Qué les toca |
|---|---|---|
| `maclaurin.m` | Completo | Correrlo y comparar con la lámina 25 |
| `maclaurin.py` | Completo | Correrlo; en el ejercicio 4, cambiar `CIFRAS` |
| `maclaurin.c` | Las dos líneas `COMPLETAR` están implementadas | Compilar, correr y comparar |

Todo se corre **dentro del contenedor**, en la carpeta `practica1`.

Desde PowerShell en Windows, estando en `ContenedorPractica1`:

```powershell
docker compose up -d --build
docker compose exec metodos bash
```

Dentro del contenedor:

```bash
cd /trabajo/practica1
```

## Octave

```bash
octave maclaurin.m
```

## Python

```bash
python3 maclaurin.py
```

## C: compilar y ejecutar

```bash
gcc -O2 -std=c17 -Wall -o maclaurin maclaurin.c -lm
./maclaurin
```

Cada vez que cambien `maclaurin.c` hay que volver a compilar.

### Comparación de las tres salidas

Estos comandos se ejecutan dentro del contenedor en `/trabajo/practica1`.
Los archivos de verificación se guardan en un directorio temporal:

```bash
verificacion=$(mktemp -d /tmp/maclaurin.XXXXXX)
gcc -O2 -std=c17 -Wall -Wextra -Werror -o "$verificacion/maclaurin" maclaurin.c -lm
"$verificacion/maclaurin" > "$verificacion/c.txt"
python3 maclaurin.py > "$verificacion/python.txt"
octave-cli --quiet maclaurin.m > "$verificacion/octave.txt"
tail -n +2 "$verificacion/c.txt" > "$verificacion/c-numeros.txt"
tail -n +2 "$verificacion/python.txt" > "$verificacion/python-numeros.txt"
tail -n +2 "$verificacion/octave.txt" > "$verificacion/octave-numeros.txt"
diff -u "$verificacion/c-numeros.txt" "$verificacion/python-numeros.txt"
diff -u "$verificacion/c-numeros.txt" "$verificacion/octave-numeros.txt"
```

Se omite únicamente la primera línea, que identifica el lenguaje. Ambos `diff`
deben terminar con código 0 y sin diferencias. La compilación estricta también
debe terminar con código 0.

## Qué debe salir

```
términos         aproximación        et (%)        ea (%)
       1    1.000000000000000       39.3469             -
       2    1.500000000000000        9.0204       33.3333
       3    1.625000000000000       1.43877       7.69231
       4    1.645833333333333      0.175162       1.26582
       5    1.648437500000000     0.0172116      0.157978
       6    1.648697916666667    0.00141649     0.0157953

Se alcanzó ea <= es con 6 términos.
```

La lámina 25 muestra estos mismos números con menos decimales, y una fila 7 de más para
que se vea que ya no hacía falta.

## Si su C no da esa tabla

| Sale esto | Es que… |
|---|---|
| Una sola fila y «Se alcanzó ea <= es con 1 términos» | Falta `COMPLETAR 2`: `ea` vale 0 |
| Dos filas, y la segunda igual a la primera | Falta `COMPLETAR 1`: el término vale 0 |
| `warning: variable 'anterior' set but not used` | Es una pista de que falta `COMPLETAR 2`, no un error |
| `undefined reference to 'exp'` | Faltó `-lm` al final de `gcc` |
| `octave: command not found` | Están fuera del contenedor: `docker compose exec metodos bash` |
| Cambiaron `maclaurin.c` y no cambia nada | No volvieron a compilar |

## Ejercicio 4: más cifras

En `maclaurin.py` cambien la línea `CIFRAS = 3` por `CIFRAS = 6`, corran el programa y
anoten cuántos términos hicieron falta. Repitan con `CIFRAS = 17`.

Para repetir ese ejercicio sin editar el archivo, dentro del contenedor:

```bash
python3 - <<'PY'
import maclaurin
for cifras in (3, 6, 17):
    maclaurin.CIFRAS = cifras
    maclaurin.main()
PY
```

Se verificaron 6, 9 y 16 términos, respectivamente. La tabla medida está en el
README. Las capturas allí indicadas son imágenes de las ejecuciones; el material
incluido no especifica gráficas adicionales.
