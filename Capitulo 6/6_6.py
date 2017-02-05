'''
Created on 1 de out de 2016

@author: vitor
'''
ultimo=10
ultimo1=10
fila=list(range(1,ultimo+1))
fila1=list(range(1,ultimo1+1))
while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila 1,G para adicionar um cliente ao fim da fila 2,")
    print("A para realizar o atendimento na fila 1 ou B para realizar o atendimento na fila 2. S para sair")
    operacao = input("Operacao(F,A ou S): ")
    x=0
    while x<len(operacao):
        if operacao[x] == "A":
            if(len(fila))>0:
                atendido = fila.pop(0)
                print(" Cliente %d atendido na fila 1" % atendido)
            else:
                print("Fila! Ninguem para atender.")
        elif operacao[x] == "B":
            if(len(fila1))>0:
                atendido = fila1.pop(0)
                print(" Cliente %d atendido na fila 2" % atendido)
            else:
                print("Fila! Ninguem para atender.")
        elif operacao[x] == "F":
            ultimo+=1
            fila.append(ultimo)
        elif operacao[x] == "G":
            ultimo1+=1
            fila.append(ultimo1)
        elif operacao[x] == "S":
            break
        else:
            print("Operacao invalida! Digite apenas F, A ou S!")    
        x+=1
    if operacao[x]=="S":
        break