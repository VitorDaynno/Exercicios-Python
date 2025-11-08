def valida_opcoes(opcoes):
  opcoes_tratadas = []

  for opcao in opcoes:
    opcoes_tratadas.append(
      opcao.lower()
    )

  while True:
    opcao_digitada = (input("Digite uma opção: ")).lower()

    if opcao_digitada in opcoes_tratadas:
      print("Opção válida!")
      return

    print("Opção inválida! Digite novamente outra opção.")

valida_opcoes(["A", "b", "c", "D"])