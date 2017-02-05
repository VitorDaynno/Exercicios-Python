'''
Created on 1 de out de 2016

@author: vitor
'''
ultimo=10
fila=list(range(1,ultimo+1))
while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair")
    operacao = input("Operacao(F,A ou S): ")
    x=0
    while x<len(operacao):
        if operacao[x] == "A":
            if(len(fila))>0:
                atendido = fila.pop(0)
                print(" Cliente %d atendido" % atendido)
            else:
                print("Fila! Ninguem para atender.")
        elif operacao[x] == "F":
            ultimo+=1
            fila.append(ultimo)
        elif operacao[x] == "S":
            break
        else:
            print("Operacao invalida! Digite apenas F, A ou S!")    
        x+=1
    if operacao[x]=="S":
        break