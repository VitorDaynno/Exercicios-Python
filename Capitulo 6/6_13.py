'''
Created on 1 de out de 2016

@author: vitor
'''
T=[-10,-8,0,1,2,5,-2,-4]
minimo=T[0]
maximo=T[0]
media=0
for e in T:
    if e<minimo:
        minimo=e
    if e>maximo:
        maximo=e
    media=media+e
media=media/len(T)
print('Temperatura minima: ',minimo)
print('Temperatura maxima:',maximo)
print('Temperatura media: ',media)