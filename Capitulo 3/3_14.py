'''
Created on 28 de ago de 2016

@author: vitor
'''

quantidadeKm= int(input('Digite a quantidade de km percorrida: '))
quantidadeDia= int(input('Digite a quantidade de dias: '))
print('Preco a pagar R$ ', 60 * quantidadeDia + 0.15 * quantidadeKm)