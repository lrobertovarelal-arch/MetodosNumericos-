/* Calculadora interactiva: una entrada por línea, con recuperación de errores. */
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Devuelve 1 para número válido, -1 para entrada inválida y 0 para EOF. */
static int leer_numero(const char *mensaje, double *numero)
{
    char linea[256];
    printf("%s", mensaje);
    fflush(stdout);
    if (fgets(linea, sizeof linea, stdin) == NULL) return 0;
    if (strchr(linea, '\n') == NULL && !feof(stdin)) {
        int c;
        while ((c = getchar()) != '\n' && c != EOF) { }
        puts("Error: entrada demasiado larga.");
        return -1;
    }
    char *fin;
    *numero = strtod(linea, &fin);
    if (fin == linea) {
        puts("Error: entrada no numérica.");
        return -1;
    }
    while (isspace((unsigned char)*fin)) ++fin;
    if (*fin != '\0' || !isfinite(*numero)) {
        puts("Error: se requiere un número finito sin texto adicional.");
        return -1;
    }
    return 1;
}

int main(void)
{
    for (;;) {
        puts("\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n0. Salir");
        double opcion, a, b, resultado;
        int estado = leer_numero("Opción: ", &opcion);
        if (estado == 0) { puts("Fin de entrada. Hasta luego."); break; }
        if (estado < 0) continue;
        if (opcion < 0 || opcion > 4 || opcion != floor(opcion)) {
            puts("Error: opción inválida; elija un entero de 0 a 4.");
            continue;
        }
        if (opcion == 0) { puts("Hasta luego."); break; }
        estado = leer_numero("Primer número: ", &a);
        if (estado == 0) { puts("Fin de entrada. Hasta luego."); break; }
        if (estado < 0) continue;
        estado = leer_numero("Segundo número: ", &b);
        if (estado == 0) { puts("Fin de entrada. Hasta luego."); break; }
        if (estado < 0) continue;
        switch ((int)opcion) {
            case 1: resultado = a + b; break;
            case 2: resultado = a - b; break;
            case 3: resultado = a * b; break;
            case 4:
                if (b == 0.0) {
                    puts("Error: división entre cero.");
                    continue;
                }
                resultado = a / b;
                break;
            default: return EXIT_FAILURE; /* El menú valida las opciones. */
        }
        if (!isfinite(resultado)) {
            puts("Error: resultado fuera del rango de doble precisión.");
            continue;
        }
        printf("Resultado: %.17g\n", resultado);
    }
    return EXIT_SUCCESS;
}
