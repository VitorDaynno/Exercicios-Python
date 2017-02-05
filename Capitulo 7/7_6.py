'''
Created on 15 de out de 2016

@author: vitor
'''
string1= input('Entre com a primeira string: ')
string2= input('Entre com a segunda string: ')
string3= input('Entre com a terceira string: ')

i=0
while i<len(string1):
    if string2.count(string1[i])>0:
        aux=string2.find(string1[i])
        print(string3[aux])
    else:
        print(string1[i])
    i=i+1