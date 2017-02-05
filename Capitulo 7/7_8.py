'''
Created on 15 de out de 2016

@author: vitor
'''

numero = int(input("Digite um numero:"))
palavras =["obsoleto","banda","campanha","estrada","noite","galera"]
indice=(numero*776) % len(palavras)
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha=""
    for letra in palavras[indice]:
        senha+=letra if letra in acertos else "."
    print(senha)
    if senha == palavras[indice]:
        print("Voce acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Voce ja tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavras[indice]:
            acertos += tentativa
        else:
            erros += 1
            print("Voce Errou!")
    print("X==:==\nX  :  ")
    print("X  O " if erros >= 1 else "X")
    linha2=""
    if erros == 2:
        linha2 = " | "
    elif erros == 3:
        linha2 = "\|"
    elif erros >=4:
        linha2 = " \|/"
    print("x%s" % linha2)
    linha3=""
    if erros == 5:
        linha3+=" / "
    elif erros>=6:
        linha3+=" / \ "
    print("X%s" % linha3)
    print("X\n=============")
    if erros == 6:
        print("Enforcado")
        print("A palavra secreta era: "+palavras[indice])
        break
        