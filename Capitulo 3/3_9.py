'''
Created on 28 de ago de 2016

@author: vitor
'''

dia= int(input('Digite o numero de dia: '))
horas= int(input('Digite o numero de horas: '))
minutos= int(input('Digite o numero de minutos: '))
segundos= int(input('Digite o numero de segundos: '))
print(segundos+minutos*60+horas*3600+dia*86400,' segundos')