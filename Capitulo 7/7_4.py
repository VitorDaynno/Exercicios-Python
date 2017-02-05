'''
Created on 15 de out de 2016

@author: vitor
'''

string1= input('Entre com a string: ')
string_Resultado=''
i=0
while i<len(string1):
    if string_Resultado.count(string1[i])==0:
        string_Resultado=string_Resultado+string1[i]
    i=i+1
i=0    
while i<len(string_Resultado):
    print(string_Resultado[i]+':'+str(string1.count(string_Resultado[i]))+'x')
    i=i+1