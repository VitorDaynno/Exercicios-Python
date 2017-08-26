#-*- coding: utf-8 -*-

jogo = [['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']] 
regra = [[7,8,9],[4,5,6],[1,2,3]] 
print("Digite o número no teclado númerico para escolher a casa")
for linha in regra:
  print(linha)
anterior = 'O'

while True:
  #Imprime o tabuleiro
  if anterior == 'O':
    print('\n Vez do X:')
    anterior = 'X'
  else:
    print('\n Vez do O')
    anterior = 'O'
  i=0
  while i < len(jogo):
    print(jogo[i][0]+'|'+jogo[i][1]+'|'+jogo[i][2])
    if i != 2:
        print('---+---+---')
    i = i + 1
    
  #Escolhas
  jogada = input()
  if jogada == 7:
    jogo[0][0] = ' '+anterior+' '
  elif jogada == 8:
    jogo[0][1] = ' '+anterior+' '
  elif jogada == 9:
    jogo[0][2] = ' '+anterior+' '
  elif jogada == 4:
    jogo[1][0] = ' '+anterior+' '
  elif jogada == 5:
    jogo[1][1] = ' '+anterior+' '
  elif jogada == 6:
    jogo[1][2] = ' '+anterior+' '
  elif jogada == 1:
    jogo[2][0] = ' '+anterior+' '
  elif jogada == 2:
    jogo[2][1] = ' '+anterior+' '
  elif jogada == 3:
    jogo[2][2] = ' '+anterior+' '
  else:
    print('Número inválido')
    
  #Verifica vitória
  #Horizontais
  if jogo[0][0] == jogo[0][1] == jogo[0][2] != '   ':
    print(jogo[0][0] +' ganhou')
    break
  if jogo[1][0] == jogo[1][1] == jogo[1][2] != '   ':
    print(jogo[1][0] +' ganhou')
    break
  if jogo[2][0] == jogo[2][1] == jogo[2][2] != '   ':
    print(jogo[2][0] +' ganhou')
    break
  
  #Verticais
  if jogo[0][0] == jogo[1][0] == jogo[2][0] != '   ':
    print(jogo[0][0] +' ganhou')
    break
  if jogo[0][1] == jogo[1][1] == jogo[2][1] != '   ':
    print(jogo[0][1] +' ganhou')
    break
  if jogo[0][2] == jogo[1][2] == jogo[2][2] != '   ':
    print(jogo[0][2] +' ganhou')
    break
  
  #Diagonais
  if jogo[0][0] == jogo[1][1] == jogo[2][2] != '   ':
    print(jogo[0][0] +' ganhou')
    break
  if jogo[2][0] == jogo[1][1] == jogo[0][2] != '   ':
    print(jogo[2][0] +' ganhou')
    break