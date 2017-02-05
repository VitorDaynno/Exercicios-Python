'''
Created on 25 de set de 2016

@author: vitor
'''
num=input('Digite o numero: ')
inicio=0
final=len(num)-1
while True:
    if num[inicio]!=num[final]:
        print('Nao palindromo')
        break
    if inicio==final:
        print('Palindromo')
        break
    inicio=inicio+1
    final=final-1