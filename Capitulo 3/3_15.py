'''
Created on 28 de ago de 2016

@author: vitor
'''
quantidadeCigarro= int(input('Digite a quantidade de cigarros fumados por dia: '))
quantidadeAno= int(input('Digite quantos anos e fumante: '))
aux=(((quantidadeAno*365)*quantidadeCigarro)*10)/1440
print('%5.2f dias perdidos'%aux)