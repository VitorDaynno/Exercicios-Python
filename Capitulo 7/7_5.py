'''
Created on 15 de out de 2016

@author: vitor
'''

string1= input('Entre com a primeira string: ')
string2= input('Entre com a segunda string: ')
string3=''

i=0
while i<len(string1):
    if string2.count(string1[i])==0:
       string3=string3+string1[i]
    i=i+1
    
print(string3)