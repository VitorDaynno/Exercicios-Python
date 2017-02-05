'''
Created on 25 de set de 2016

@author: vitor
'''
divida=float(input('Digite a divida inicial: '))
juros=int(input('Digite o percetual do juros: '))
valor_pago=float(input('Digite o valor pago mensalmente: '))
mes=0
valor_total_juros=0
valor_inicial=divida
while divida > 0:
    valor_total_juros= valor_total_juros + divida*(juros/100)
    divida= divida+divida*(juros/100)
    divida=divida-valor_pago
    mes=mes+1
print('%d meses para pagar'%mes)
print('Total pago: R$ %10.2f'%(valor_inicial+valor_total_juros))
print('Total de juros: R$ %10.2f'%valor_total_juros) 