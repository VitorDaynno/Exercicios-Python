'''
Created on 1 de out de 2016

@author: vitor
'''
L=[]
while True:
    n=int(input('Digite um numero (0 sai):'))
    if n==0:
        break
    L.append(n)
for i in L:
    print(i)