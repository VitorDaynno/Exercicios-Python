'''
Created on 2 de set de 2016

@author: vitor
'''
saldo=float(input('Digite o deposito inicial: '))
juros=float(input('Digite a taxa de juros: '))
x=0
valorInicial=saldo
while x<=24:
    saldo=saldo+saldo*(juros/100)   
    print('Mes ' ,x,': R$ %10.2f'%saldo)
    x=x+1
print('Voce ganhou: R$ %10.2f'%(saldo-valorInicial))