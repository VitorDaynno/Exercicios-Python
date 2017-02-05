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
boneco=["X  O "," | "," \|"," \|/"," /"," /\\"]
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
    print(boneco[0] if erros >= 1 else "X")
    if erros == 2:
        print("x%s" % boneco[1])
    elif erros == 3:
        print("x%s" % boneco[2])
    elif erros >=4:
        print("x%s" % boneco[3])
    if erros == 5:
        print("x%s" % boneco[4])
    elif erros>=6:
        print("x%s" % boneco[5])
    print("X\n=============")
    if erros == 6:
        print("Enforcado")
        print("A palavra secreta era: "+palavras[indice])
        break
        