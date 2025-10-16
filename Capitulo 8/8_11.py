def valida_string(text, min, max):
  text_lenght = len(text)

  return text_lenght > min and text_lenght < max

print(valida_string(input("Digite uma string: "), 5, 10))