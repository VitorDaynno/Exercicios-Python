'''
Created on 25 de set de 2016

@author: vitor
'''
num=int(input('Digite o numero: '))
i=1
while True:
    if num == 0 or num == 1:
        print('Nao primo')
        break
    elif num == 2:
        print('Primo')
        break
    elif num==(2*i+1):
        print('Primo')
        break
    elif num%(2*i+1)==0 or num%2==0:
        print('Nao primo')
        break
    i=i+1