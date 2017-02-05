'''
Created on 2 de set de 2016

@author: vitor
'''
inicio=int(input('Digite o primeiro numero: '))
fim=int(input('Digite o segundo numero: '))
resto=inicio
x=0
while resto>=fim:
    resto=resto-fim
    x=x+1
print('divisao: ',x)
print('resto: ',resto)