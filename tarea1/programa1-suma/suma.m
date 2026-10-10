% Suma dos decimales finitos; sin argumentos utiliza 0.1 y 0.2.
argumentos = argv();
if isempty(argumentos)
  a = 0.1; b = 0.2;
elseif numel(argumentos) == 2
  patron = '^[+-]?([0-9]+(\.[0-9]*)?|\.[0-9]+)([eE][+-]?[0-9]+)?\z';
  for k = 1:2
    if isempty(regexp(argumentos{k}, patron, 'once'))
      fprintf(2, 'Error: se requieren dos números decimales finitos.\n');
      exit(1);
    end
  end
  a = str2double(argumentos{1}); b = str2double(argumentos{2});
  if !isfinite(a) || !isfinite(b)
    fprintf(2, 'Error: se requieren dos números decimales finitos.\n');
    exit(1);
  end
else
  fprintf(2, 'Uso: octave-cli suma.m [numero1 numero2]\n');
  exit(1);
end
resultado = a + b;
if !isfinite(resultado)
  fprintf(2, 'Error: la suma excede el rango de doble precisión.\n');
  exit(1);
end
fprintf('%.17g\n', resultado);
