'''
Created on 1 de out de 2016

@author: vitor
'''
lista1=[1,2,3,4]
lista2=[4,3,2,1]
lista3=[]
x=0
while x<4:
    aux=0
    y=0
    while y<len(lista3):
        if lista3[y]==lista1[x]:
            aux=1
        y=y+1
    if aux==0:
        lista3.append(lista1[x])
    x=x+1
x=0
while x<4:
    aux=0
    y=0
    while y<len(lista3):
        if lista3[y]==lista2[x]:
            aux=1
        y=y+1
    if aux==0:
        lista3.append(lista2[x])
    x=x+1
x=0
print(lista3)