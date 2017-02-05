'''
Created on 25 de set de 2016

@author: vitor
'''
num=int(input('Digite um numero maior que 0 e 0 para sair:'))
quant=0
soma=0
while True:
    if num==0:
        break
    quant=quant+1
    soma=soma+num
    num=int(input('Digite um numero maior que 0 e 0 para sair:'))
print('Quantidade digitada: ',quant)
print('Soma total: ',soma)
print('Media aritmetica: ',(soma/quant))