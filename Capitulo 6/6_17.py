'''
Created on 1 de out de 2016

@author: vitor
'''
estoque={"tomate":[1000,2.30],
         "alface":[500,0.45],
         "batata":[2001,1.20],
         "feijao":[100,1.50]}
produto=input("Digite o produto: ")
quantidade=int(input("Digite a quantidade: "))

if produto in estoque:
    print("Vendas")
    preco= estoque[produto][1]
    custo=preco*quantidade
    print("%12s: %3d x %6.2f = %.2f" %(produto,quantidade,preco,custo))
    print("Custo total: %21.2f\n" %custo)

print("Estoque: \n")
for chave, dados in estoque.items():
    print("Descrica: ",chave)
    print("Quantidade: ", dados[0])
    print("Preco: %6.2f\n "%dados[1])