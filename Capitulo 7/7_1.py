'''
Created on 15 de out de 2016

@author: vitor
'''

string1= input('Entre com a primeira string: ')
string2= input('Entre com a segunda string: ')
aux=string1.find(string2)
if aux>0:
    print(string2,' encontrado na posicao %d de '%aux,string1 )