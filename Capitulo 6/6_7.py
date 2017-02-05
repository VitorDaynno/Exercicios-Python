'''
Created on 1 de out de 2016

@author: vitor
'''
texto=input('Digite os paranteses')
lista=[]
x=0
resposta='Erro'
while x<len(texto):
    if texto[x] == '(':
        lista.append('(')
    elif len(lista)>0:
        if lista.pop(-1) == '(':
            resposta='OK'
        else:
            resposta='Erro'
    else:
        resposta='Erro'
    x+=1
print(resposta)
 