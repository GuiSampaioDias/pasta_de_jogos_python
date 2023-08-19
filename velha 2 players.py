# Jogo da velha para 2 jogadores autoria: Guilherme Sampaio Dias

from random import randint
from time import sleep
cpu = []
player = []
jogadas = []
p =['','','','','','','','',''] #posiçoes
def exibe1(p):
    print()
    print(f'{p[0]:^3}|{p[1]:^3}|{p[2]:^3}' + ' ' * 15 + ' 0 | 1 | 2')
    print('___|___|___'+' ' * 15 + '___|___|___')
    print('   |   |   ' + ' ' * 15 + '   |   |   ')
    print(f'{p[3]:^3}|{p[4]:^3}|{p[5]:^3}' + ' ' * 15 + ' 3 | 4 | 5 ')
    print('___|___|___' + ' ' * 15 + '___|___|___')
    print('   |   |   ' + ' ' * 15 + '   |   |   ')
    print(f'{p[6]:^3}|{p[7]:^3}|{p[8]:^3}' + ' ' * 15  +' 6 | 7 | 8 ')
    print()
def exibe2(p):
    print()
    print(f'{p[0]:^3}|{p[1]:^3}|{p[2]:^3}')
    print('___|___|___')
    print('   |   |   ')
    print(f'{p[3]:^3}|{p[4]:^3}|{p[5]:^3}')
    print('___|___|___')
    print('   |   |   ')
    print(f'{p[6]:^3}|{p[7]:^3}|{p[8]:^3}')
    print()
    

exibe1(p)
while True:
    jogada = int(input('Jogador 1 \nFaça a sua jogada: '))
    while jogada < 0 or jogada >= 9 or jogada in jogadas:
        print('Jogada inválida!')
        jogada = int(input('Jogador 1\nFaça a sua jogada: '))
    player.append(jogada)
    jogadas.append(jogada)
    p[jogada] = 'X'
    sleep(1)
    exibe1(p)

    if 0 in player and 1 in player and 2 in player:
        player = 1
        break
    if 3 in player and 4 in player and 5 in player:
        player = 1
        break
    if 6 in player and 7 in player and 8 in player:
        player = 1
        break
    if 0 in player and 3 in player and 6 in player:
        player = 1
        break
    if 1 in player and 4 in player and 7 in player:
        player = 1
        break
    if 2 in player and 5 in player and 8 in player:
        player = 1
        break
    if 0 in player and 4 in player and 8 in player:
        player = 1
        break
    if 2 in player and 4 in player and 6 in player:
        player = 1
        break
    if 1 in jogadas and 2 in jogadas and 3 in jogadas and 4 in jogadas and 5 in jogadas and 6 in jogadas and 7 in jogadas and 8 in jogadas and 0 in jogadas:
        break
    
    while True:
        computador = int(input('Jogador 2\nFaça a sua jogada: '))
        while computador < 0 or computador > 8 or computador in jogadas:
            print('jogada invalida')
            computador = int(input('Jogador 2\nFaça a sua jogada: '))
        cpu.append(computador)
        jogadas.append(computador)
        p[computador] = 'O'
        sleep(1)
        exibe1(p)
        break    
    if 0 in cpu and 1 in cpu and 2 in cpu:
        cpu = 1
        break
    if 3 in cpu and 4 in cpu and 5 in cpu:
        cpu = 1
        break
    if 6 in cpu and 7 in cpu and 8 in cpu:
        cpu = True
        break
    if 0 in cpu and 3 in cpu and 6 in cpu:
        cpu = 1
        break
    if 1 in cpu and 4 in cpu and 7 in cpu:
        cpu = 1
        break
    if 2 in cpu and 5 in cpu and 8 in cpu:
        cpu = 1
        break
    if 0 in cpu and 4 in cpu and 8 in cpu:
        cpu = 1
        break
    if 2 in cpu and 4 in cpu and 6 in cpu:
        cpu = 1
        break
    
    sleep(1)
    exibe1(p)

exibe2(p)
sleep(1)
if player == 1:
    print(f'Parabéns jogador 1! \nVocê venceu!')
elif cpu == 1:
    print('Parabens jogador 2!\n Você venceu!')
else:
    print('Empatamos!!!')
