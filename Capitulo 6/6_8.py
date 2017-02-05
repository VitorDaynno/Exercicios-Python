'''
Created on 1 de out de 2016

@author: vitor
'''
L=[15,7,27,39]
p=int(input('Digite o valor a procurar:'))
achou=False
x=0
while x<len(L):
    if L[x]==p:
        print('%d achado na posicao %d' %(p,x))
        break
    if x+1==len(L):
        print('%d nao encontrado' %p)
    x+=1

    