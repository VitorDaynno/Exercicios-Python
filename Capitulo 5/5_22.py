'''
Created on 25 de set de 2016

@author: vitor
'''
i=0
while True:
    op=input('\nDigite a opcao desejada: \nadicao \nsubtracao \ndivisao \nmultiplicacao \nsaida\n')
    i=0
    while i<11:
        if op == 'adicao':
            print(10+i)
        elif op == 'subtracao':
            print(10-i)
        elif op == 'divisao' and i!=0:
            print('%5.2f'%(10/i))
        elif op == 'multiplicacao':
            print(10*i)
        i=i+1
    if op == 'saida':
        break