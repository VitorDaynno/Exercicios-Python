'''
Created on 1 de out de 2016

@author: vitor
'''
lista1=[0,0,0,0]
lista2=[0,0,0,0]
x=0
print('Digite os elementos da lista 1')
while x<4:
    lista1[x]=int(input('Elemento %d: '%(x+1)))
    x=x+1
x=0
print('Digite os elementos da lista 2')
while x<4:
    lista2[x]=int(input('Elemento %d: '%(x+1)))
    x=x+1
lista3=lista1+lista2
print(lista3) 
    