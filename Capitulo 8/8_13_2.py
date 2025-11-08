import random

n = random.randint(1, 10)
tentativa = 1

while tentativa <= 3:
  print("Tentativa {0}:\n".format(tentativa))

  x = int(input("Escolha um número entre 1 e 10: "))

  if x == n:
    print("Você acertou!")
    break
  else:
    print("Você errou.\n")
    tentativa+=1