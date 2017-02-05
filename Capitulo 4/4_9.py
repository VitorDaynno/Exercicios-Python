'''
Created on 28 de ago de 2016

@author: vitor
'''

valorCasa= float(input('Digite o valor da casa: '))
salario= float(input('Digite o salario: '))
quantidadeAnos= float(input('Digite a quantidade de anos: '))
if valorCasa/(quantidadeAnos*12) < salario*0.3:
    print('Credito aprovado')
else:
    print('Credito reprovado')