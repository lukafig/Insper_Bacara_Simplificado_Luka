#EP - Design de Software
#Equipe: Luka de Figueiredo
#Data: 05/10/2020 

from random import *

#pergunta quantos jogadores tem
n_jogadores = int(input("Quantos jogadores ? "))
#pergunta qunatos baralhos serao utilizados
n_baralhos = int(input("Quantos baralhos ? 1, 6 ou 8 "))

#cria o baralho com o numero de baralhos utilizados
baralho = ([1,2,3,4,5,6,7,8,9,0,0,0,0]*4)* n_baralhos

#define as comisões
if n_baralhos == 1:
    comisao_J = 0.0129
elif n_baralhos == 6:
    comisao_J = 0.0124
else:
    comisao_J = 0.0124

if n_baralhos == 1:
    comisao_B = 0.0101
elif n_baralhos == 6:
    comisao_B = 0.0106
else:
    comisao_B = 0.0106

if n_baralhos == 1:
    comisao_E = 0.1575
elif n_baralhos == 6:
    comisao_E = 0.1444
else:
    comisao_E = 0.1436

#Checa quantas fichas cada jogador tem
fichas_jogador = [0]*n_jogadores
for i in range (0,n_jogadores):
    print("Jogador de numero", i+1)
    fichas_jogador[i] = int(input("Quantas fichas você tem ?"))
    
#cria a lista aposta   
aposta = [0]*n_jogadores
Qaposta = [0]*n_jogadores




#pega duas cartas para cada jogador e soma os valores
def jogo():
    x1 = 0
    x2 = 0

    carta1 = carta(baralho)
    K = randint(0,n_baralhos)
    CartaX = carta1[0] * carta1[1] * K
    baralho.pop(CartaX)
    x1 = x1 + carta1[2]
    
    carta2 = carta(baralho)
    K = randint(0,n_baralhos)
    CartaX = carta2[0] * carta2[1] * K
    baralho.pop(CartaX)
    x2 = x2 + carta2[2]
    
    carta3 = carta(baralho)
    K = randint(0,n_baralhos)
    CartaX = carta3[0] * carta3[1] * K
    baralho.pop(CartaX)
    x1 = x1 + carta3[2]
    
    carta4 = carta(baralho)
    CartaX = carta4[0] * carta4[1] * K
    baralho.pop(CartaX)
    x2 = x2 + carta4[2]
#se a soma for menor que 5 o program pega a terceira carta para quem precisar
    if x1 < 5 or x2 < 5:
        if x1 > 5:
            CartaY = carta(baralho)
            CartaX = CartaY[0] * CartaY[1] * K
            baralho.pop(CartaX)
            x1 = x1 + CartaY[2]
        else:
            CartaY = carta(baralho)
            CartaX = CartaY[0] * CartaY[1] * K
            baralho.pop(CartaX)
            x1 = x1 + CartaY[2]
    return [x1,x2]
#funcao que pega a carta
def carta(baralho:list):
    naipe = randint(0,3)
    numero = randint(0,12)
    valor = String(numero)
    '''print(numero,naipe,valor)'''
    return [numero,naipe,valor]
#funcao que determina o valor da carta pega
def String(x):
    baralho_novo = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    VALORS = [1,2,3,4,5,6,7,8,9,0,0,0,0]
    if x == 10 or x == 11 or x == 12 or x == 9:
        return 0
    else:
        II = VALORS.index(x)
        return VALORS[II]

#roda o jogo
jogo=jogo()
#loop que verifica em quem os jogadores iram apostar e quanto
#tambem verifica quem ganha e mostra o que aconteceu e quanto ganhou/perdeu
for i in range(0,n_jogadores):
    print("Jogador de numero", i+1)
    Qaposta[i] = input("Em quem quer apostar ? Jogador, Banco ou em um Empate. ")
    str(Qaposta)
    aposta[i] = int(input("Quanto quer apostar ? "))
if jogo[0] > jogo[1]:
    print ("Soma do Jogador ganhou")
elif jogo[1] < jogo[0]: 
    print ("Soma do banco ganhou")
else:  
    print("Empatou")
for i in range(0,n_jogadores):
    if Qaposta[i] == "Jogador":
        if jogo[0] > jogo[1]:
            fichas_jogador[i] = fichas_jogador[i] + aposta[i] - aposta[i]* comisao_J
            print ("Fichas do jogador numero", i+1)
        elif jogo[1] < jogo[0]:
            fichas_jogador[i] = fichas_jogador[i] - aposta[i]
            print ("Fichas do jogador numero", i+1)
        else:
            fichas_jogador[i] = fichas_jogador[i] - aposta[i]
            print ("Fichas do jogador numero", i+1)
        print(fichas_jogador[i])
    elif Qaposta[i] == "Banco":
        if jogo[1] > jogo[0]:
            fichas_jogador[i] = fichas_jogador[i] - aposta[i]
            print ("Fichas do jogador numero", i+1)
        elif jogo[0] < jogo[1]:
            fichas_jogador[i] = fichas_jogador[i] + aposta[i] - aposta[i]*comisao_B
            print ("Fichas do jogador numero", i+1)
        else:
            fichas_jogador[i] = fichas_jogador[i] - aposta[i]
            print ("Fichas do jogador numero", i+1)
        print(fichas_jogador[i])
    else:
        if jogo[1] > jogo[0]:
            fichas_jogador[i] = fichas_jogador[i] - aposta[i]
            print ("Fichas do jogador numero", i+1)
        elif jogo[0] > jogo[1]:
            fichas_jogador[i] = fichas_jogador[i] - aposta[i]
            print ("Fichas do jogador numero", i+1)
        else:
            fichas_jogador[i] = fichas_jogador[i] + aposta[i] - aposta[i]*comisao_E
            print ("Fichas do jogador numero", i+1)
        print(fichas_jogador[i])
