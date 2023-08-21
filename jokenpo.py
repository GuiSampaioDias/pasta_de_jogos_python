# ------------------------------------------------

# Autor: Guilherme Sampaio Dias

# jogo: Jokenpô

# data: 21/08/2023

# -------------------------------------------------



from time import sleep
from random import randint

jogadas = ["Pedra", "Papel", "Tesoura"]
p1 = 0
p2 = 0
empate = 0

print("\n" * 5)
print("/" * 30)
print()
print(f"Joquenpô".center(30))
print()
print("/" * 30)
sleep(1)
print("\nMuito bem vindo(a)\n")
sleep(1)
print("Vamos começar o jogo\n\n")

while True:
    print("-" * 30)
    print("\nSuas opções de jogada: \n1- Pedra\n2- Papel\n3- Tesoura\n")
    print("-" * 30)
    print('\n')
    sleep(1)
    player = input("Faça a sua jogada: ")
    while player != "1" and player != "2" and player != "3":
        player = input("\nJogada invalide!\nRefaça a sua jogada: ")
    pc = jogadas[randint(0, 2)]
    print('\n\n')
    sleep(1)
    print('Jo')
    sleep(0.5)
    print('\nKen')
    sleep(0.5)
    print('\nPô')
    print('\n\n\n')
    sleep(1)
    player = jogadas[int(player) - 1]
    if pc == player:
        print(f'Empate\nAmbos escolheram {pc}')
        empate += 1
    elif player == "Pedra":
        if pc == "Papel":
            print(f"Você jogou Pedra o Pc jogou Papel")
            sleep(0.5)
            print("Vitória do pc")
            p2 += 1
        if pc == "Tesoura":
            print(f'Você jogou Pedra o Pc jogou Tesoura')
            sleep(0.5)
            print(f'Parabéns pela vitória')
            p1 += 1
    
    elif player == "Papel":
        if pc == "Pedra":
            print(f'Você jogou {player} o Pc jogou {pc}')
            sleep(0.5)
            print(f'Parabéns pela vitória') 
            p1 += 1
        elif pc == "Tesoura":
            print(f'Você jogou {player} o Pc jogou {pc}')
            sleep(0.5)
            print(f'Vitória do Pc')
            p2 += 1

    else:
        if pc == "Pedra":
            print(f'Você jogou {player} o Pc jogou {pc}')
            sleep(0.5)
            print('Vitória do Pc')
            p2 += 1
        elif pc == "Papel":
            print(f'Você jogou {player} o pc jogou {pc}')
            sleep(0.5)
            print('Parabéns pela vitória')
            p1 += 1

    print()
    jogar = input('Digite: \n1 para jogar mais uma vez  \n2 para finalizar o jogo\n')
    while jogar != "1" and jogar != "2":
        jogar = input('Jogada inválida\nFaça a sua jogada: ')
    if jogar == "2":
        break
    else:
        sleep(0.5)
        print('\nLegal vamor jogar mais uma vez')

print('\n\nFinalizando o jogo\n')
print(f'Vocês jogaram {empate + p1 + p2}')
print(f'Você ganhou {p1} partida(s)')
print(f'O Pc ganhou {p2} partida(s)')