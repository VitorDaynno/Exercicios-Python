'''
Created on 28 de ago de 2016

@author: vitor
'''

num1= float(input('Digite numero 1: '))
num2= float(input('Digite numero : '))
operacao= input('Digite a operacao que deseja: ')
if operacao=='soma':
    print(num1+num2)
elif operacao=='subtracao':
    print(num1-num2)
elif operacao=='multiplicacao':
    print(num1*num2)
elif operacao=='divisao':
    print(num1/num2)