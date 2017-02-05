'''
Created on 28 de ago de 2016

@author: vitor
'''
pMercadoria= int(input('Digite o preco da mercadoria: '))
pDesconto= int(input('Digite o percetual de desconto: '))
print('O desconto foi de R$ ',pMercadoria*(pDesconto/100),' e o preco a pagar e R$ ', pMercadoria-pMercadoria*(pDesconto/100))