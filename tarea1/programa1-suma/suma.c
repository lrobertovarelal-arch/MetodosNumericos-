/* Suma de dos números decimales finitos en doble precisión. */
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

/* Misma sintaxis en C, Python y Octave: signo, decimal y exponente opcional. */
static int leer_numero(const char *texto, double *numero)
{
    const char *p = texto;
    int digitos = 0;
    if (*p == '+' || *p == '-') ++p;
    while (*p >= '0' && *p <= '9') { ++p; ++digitos; }
    if (*p == '.') {
        ++p;
        while (*p >= '0' && *p <= '9') { ++p; ++digitos; }
    }
    if (digitos == 0) return 0;
    if (*p == 'e' || *p == 'E') {
        ++p;
        if (*p == '+' || *p == '-') ++p;
        int exponente = 0;
        while (*p >= '0' && *p <= '9') { ++p; ++exponente; }
        if (exponente == 0) return 0;
    }
    if (*p != '\0') return 0;
    char *fin;
    *numero = strtod(texto, &fin);
    return *fin == '\0' && isfinite(*numero);
}

int main(int argc, char *argv[])
{
    double a = 0.1, b = 0.2;
    if (argc != 1 && argc != 3) {
        fprintf(stderr, "Uso: %s [numero1 numero2]\n", argv[0]);
        return EXIT_FAILURE;
    }
    if (argc == 3 && (!leer_numero(argv[1], &a) || !leer_numero(argv[2], &b))) {
        fprintf(stderr, "Error: se requieren dos números decimales finitos.\n");
        return EXIT_FAILURE;
    }
    double resultado = a + b;
    if (!isfinite(resultado)) {
        fprintf(stderr, "Error: la suma excede el rango de doble precisión.\n");
        return EXIT_FAILURE;
    }
    printf("%.17g\n", resultado);
    return EXIT_SUCCESS;
}
