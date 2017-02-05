'''
Created on 15 de out de 2016

@author: vitor
'''
string1= input('Entre com a primeira string: ')
string2= input('Entre com a segunda string: ')
string3=''

if len(string1)<len(string2):
    aux=string1
    string1=string2
    string2=aux
    
i=0
while i<len(string2):
    if string1.count(string2[i])==0:
       string3=string3+string2[i]
    i=i+1
i=0
while i<len(string1):
    if string2.count(string1[i])==0:
       string3=string3+string1[i]
    i=i+1
print(string3)