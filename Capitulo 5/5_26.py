'''
Created on 25 de set de 2016

@author: vitor
'''
num1=int(input('Digite o numero 1: '))
num2=int(input('Digite o numero 2: '))
while True:
    if num1<num2:
        break
    num1=num1-num2
print('O resto da divisao e: ',num1)