'''
Created on 28 de ago de 2016

@author: vitor
'''

salario= int(input('Digite o salario: '))
pAumento= int(input('Digite a porcetagem de aumento: '))
print('O aumento foi de R$ ',salario*(pAumento/100),' e o novo salario e R$ ', salario+salario*(pAumento/100))