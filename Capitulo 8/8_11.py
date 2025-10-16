def valida_string(texto, min, max):
  tamanho_texto = len(texto)

  return tamanho_texto > min and tamanho_texto < max

print(valida_string(input("Digite uma string: "), 5, 10))