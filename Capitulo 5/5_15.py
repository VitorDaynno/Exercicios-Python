'''
Created on 25 de set de 2016

@author: vitor
'''
total=0
while True:
    codigo=int(input('Digite o codigo do produto: '))
    if codigo==1:
        total=total+0.5
    elif codigo==2:
        total=total+1
    elif codigo==3:
        total=total+4
    elif codigo==5:
        total=total+7
    elif codigo==9:
        total=total+8
    elif codigo==0:
        break
    else:
        print('Codigo invalido')
print('Valor total: R$%5.2f'%total)