'''
Created on 28 de ago de 2016

@author: vitor
'''
num1= int(input('Digite numero 1: '))
num2= int(input('Digite numero 2: '))
num3= int(input('Digite numero 3: '))

maior=num1
menor=num1
if num2>maior:
    maior=num2
if num3>maior:         
    maior=num3 
if num2<menor:
    menor=num2
if num3<menor:
    menor=num3
print('Maior: ',maior,'\nMenor: ',menor)