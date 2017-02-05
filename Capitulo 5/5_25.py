'''
Created on 25 de set de 2016

@author: vitor
'''
n=int(input('Digite o numero: '))
b=2
while True:
    p=(b+(n/b))/2
    quadrado=p**2
    b=p
    if abs(n-quadrado)<0.0001:
        break
    
print('%5.2f'%b)
