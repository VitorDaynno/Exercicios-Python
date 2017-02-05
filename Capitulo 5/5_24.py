'''
Created on 25 de set de 2016

@author: vitor
'''
limite=int(input('Digite o numero: '))
i=1
num=0
x=0
while x<limite:
    while True:
        if num == 0 or num == 1:
            break
        elif num == 2:
            break
        elif num==(2*i+1):
            print(num,' ')
            x=x+1
            break
        elif num%(2*i+1)==0 or num%2==0:
            break
        i=i+1
    num=num+1