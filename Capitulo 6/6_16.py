'''
Created on 1 de out de 2016

@author: vitor
'''
L=[1,5,4,8,2]
fim=5
while fim>1:
    trocou=False
    x=0
    while x<(fim-1):
        if L[x]<L[x+1]:
            trocou=True
            temp=L[x]
            L[x]=L[x+1]
            L[x+1]=temp
        x+=1
    if not trocou:
        break
    fim-=1
for e in L:
    print(e)