'''
Created on 1 de out de 2016

@author: vitor
'''
dicionario={}
palavra=input('Entre com a palavra: ')
x=0
while x<len(palavra):
    if palavra[x] in dicionario:
        dicionario[palavra[x]]+=1
    else:
        dicionario[palavra[x]]=1
    x+=1
print(dicionario)