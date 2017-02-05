'''
Created on 1 de out de 2016

@author: vitor
'''
L=[15,7,27,39]
p=int(input('Digite o valor a procurar:'))
v=int(input('Digite o valor a procurar:'))
achou=False
x=0
pI=-1
vI=-1
while x<len(L):
    if L[x]==p :
       pI=x        
    if L[x]==v:
        vI=x
    x+=1
if pI>=0:
    print('%d achado na posicao %d' %(p,pI))
else:
    print('Nao achado')
if vI>=0:
    print('%d achado na posicao %d' %(p,vI))
else:
    print('Nao achado')