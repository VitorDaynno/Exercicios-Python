'''
Created on 28 de ago de 2016

@author: vitor
'''

quantidadeEnergia= float(input('Digite a quantidade de energia: '))
instalacao= input('Digite o tipo de instalacao: ')
if instalacao=='R':
    if quantidadeEnergia <= 500:
        print('Preco a pagar R$ ', quantidadeEnergia*0.4)
    else:
        print('Preco a pagar R$ ', quantidadeEnergia*0.65)
if instalacao=='C':
    if quantidadeEnergia<=1000:
        print('Preco a pagar R$ ', quantidadeEnergia*0.55)
    else:
        print('Preco a pagar R$ ', quantidadeEnergia*0.60)
if instalacao=='I':
    if quantidadeEnergia<=5000:
        print('Preco a pagar R$ ', quantidadeEnergia*0.55)
    else:
        print('Preco a pagar R$ ', quantidadeEnergia*0.6)