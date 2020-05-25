# A def vai imprimir a forca para cada erro e caso erre 6x tmb imprime a msg "Lamento! Perdeu!"
def forca(x=0):
  if x==0:
    print("------------")
    print("|          |")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==1:
    print("------------")
    print("|          |")
    print("|          0")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==2:
    print("------------")
    print("|          |")
    print("|          0")
    print("|          |")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==3:
    print("------------")
    print("|          |")
    print("|          0")
    print("|         -|")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==4:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|               ")
    print("|               ")
    print("|               ")
    print("|")
  elif x==5:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|         /      ")
    print("|               ")
    print("|               ")
    print("|")
  elif x==6:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|         / \\    ")
    print("|               ")
    print("|    Lamento! Perdeu! ")
    print("|")
#VARIAVEIS GLOBAIS
erros=0 # acumulador de erros até 6
#RECEBE PALAVRA INICIAL
palavra=input('Informe a palavra: ');
# lista que recebe '_' para cada letra de palavra
temp=[]
for letra in palavra:
  temp.append('_')
# laço while pq não se sabe a quantidade de letra da palavra
while True:
  print('\n'*20) # limpa a tela
  forca(erros) # chamei a def q imprime desenho da forca
  #imprime a adivinhacao com os traços de cada letra da palavra
  print('\n\nAdivinhe: ', end='')
  # usa o for p impresão '_' de cada letra em palavra
  for let in temp:
     # end=' ' assim o print imprime os espaços na mesma linha
    print(let, end=' ')
  print('\n'*2) # da dois espaços para baixo
  #Verifica se perdeu
  if erros==6:
    break #sai do jogo (sai do while)
  #Verificar se o jogador ganhou
  ganhouJogo=True
  # usando for let na lista temp
  for let in temp:
    # enquanto let tiver espaço vazio ganhouJogo=False e jogo continua
    if let=='_':
      ganhouJogo=False
    # caso não tenha mais espaço vazio break Venceu
  if ganhouJogo:
    print('\nPARABÉNS VENCEDOR!!!')
    break
  #captura a letra do usuario
  letraDig=input("Informe uma letra: ")
  #verifica se acertou alguma letra
  errouLetra=True
  # i percorre cada indice da lista que recebeu palavra
  for i, let in enumerate(palavra):
    # verifica se acertou add a letra
    if palavra[i]==letraDig:
      # lista temp recebe a letra no indice correspondente da palavra
      temp[i]=palavra[i]
      # então não soma erro dar um novo loop p informa outra letra
      errouLetra=False
    # caso erre soma +1 até chegar 6 q break e perdeu!
  if errouLetra:
    erros=erros+1