# -------------------------------------------------

# Desafio : Dilema dos Prisioneiros

# Autor: Guilherme Sampaio Dias

# Fonte do desafio: Professor 
# Desafio proposto por: Fernando Neves Lins

# Data: 20/08/2023
# -------------------------------------------------


from random import randint
from time import sleep 
TXT = 0
TXC = 0
CXC = 0

um =  randint(1, 2)
dois = 0
ingenuo = randint(1, 2)
estrategia = 0
coopera = True


def finalizado(a, b, c):
    total = a + b + c
    if total == 0:
        print()
        print("Não foi feito nehuma jogada")
        print("FIM")
    else:
        txt = a / total * 100
        txc = b / total * 100
        cxc = c / total * 100
        print()
        print(f'No total foram feitas {total} partidas.')
        print(f'Ambos se trairam {txt}% das vezes.')
        print(f'Teve uma traição e uma coperação e {txc}% das vezes.')
        print(f'Ambos se ajudaram em {cxc}% das vezes.')
        print("\n.\n.\n.\nFIM!")

def txt():
    print('\n\n--------------------------------------------')
    return "Ambos se trairam, 5 anos de prisão para cada.\n\n"

def txc():
    print('\n\n--------------------------------------------')
    return "Você traiu o seu comparsa e ele ficou calado.\n Pode ir para casa, mas ele ficara preso por 10 anos.\n\n"

def cxt():
    print('\n\n----------------------------------------------------')
    return "Você ficou em silencio, mas seu comparsa te delatou.\nVocê pegara máxima de 10 anos. \n\n"

def cxc():
    print('\n\n----------------------------------------------------------')
    return "Ambos ficaram calados. Pena minima de 2 anos para cada um."


print("\n1- Olho por olho\n2- Olho por dois olhos")
print("3- Não iterado\n4- Retaliador permanente\n5-Provador Ingênuo")
print('6- Finalizar o programa')
print()


while True:
    
    if estrategia == 0:
        estrategia = input("Digite o número da sua estratégia: ")
    while  estrategia != "1" and estrategia != "2" and estrategia != "3" and estrategia != "4" and estrategia != "5":
        estrategia = input("Valor inválido, refassa a sua etratégia (de 1 a 5): ")
    if estrategia == "6":
        print(finalizado(TXT, TXC, CXC)) 
        break
    else:
        print('\nAgora é muito importante você pensar bem o que vc vai fazer...')
        print()
        sleep(1)
        print('1- Trair: joga o seu conparsa no fogueira')
        sleep(1)
        print('2- Cooperar: fica em silencio e não entrega o comparsa')
        sleep(1)

        jogador1 = input("Escolha o que você vai fazer : ")
        while jogador1 != "1" and jogador1 != '2':
            jogador1 = input("Jogada inválida, escolha 1 ou 2: ")
        

        if estrategia == "1":
            if jogador1 == "1" and um == 1 :
                print(txt())
                TXT +=1
                um = 1
            elif jogador1 == "1" and um == 2:
                TXC += 1
                print(txc())
                um = 1
            elif jogador1 == "2" and um == 2:
                print(cxc())
                CXC += 1
                um = 2
            elif jogador1 == "2" and um == 1:
                print(cxt())
                TXC +=1
                um = 2

        elif estrategia =="2":
            if dois > 1:
                pc = True
            else:
                pc = False
            if jogador1 == "1" and pc == False:
                print(txt())
                TXT += 1
                dois += 1
            
            elif jogador1 == "1" and pc:
                print(txc())
                TXC += 1
                dois += 1

            elif jogador1 == "2" and pc == False:
                print(cxt())
                TXT += 1
                dois = 0
            
            elif jogador1 =="2" and pc:
                print(cxc())
                CXC += 1
                dois = 0
        
        elif estrategia == "3":
            comparsa = randint(1,2)
            if jogador1 == "1":
                if comparsa == 1:
                    TXT += 1
                    print(txt())
                else: 
                    TXC += 1
                    print(txc())

            else:
                if comparsa == 1:
                    TXC += 1
                    print(cxt())  
                else:
                    CXC +=1
                    print(cxc())

        elif estrategia == "4":
            if jogador1 == "1":
                coopera = False
                print(txt())
                TXT += 1
            else:
                if coopera:
                    print(cxc())
                    CXC += 1
                else:
                    print(cxt())
                    TXC += 1

        elif estrategia == "5":
            if jogador1 == "1":
                if ingenuo == 1:
                    TXT += 1
                    print(txt())
                else:
                    TXC += 1
                    print(txc())
                ingenuo = 1
            else:
                if ingenuo == 1:
                    TXC += 1
                    print(cxt())
                else:
                    CXC += 1
                    print(cxc())
                ingenuo = randint(1, 2)


    print('\nVocê vai jogar de novo a mesma estratégia ou mudar de estratégia?\n1- Manter \n2- Mudar')
    final = input('\n Digite 1 ou 2:')
    while final != '1' and final != '2':
        final = input('Opção não cadastrada. Faça a sua escolha: ')
    if final =='2':
        estrategia = 0
        print("\n1- Olho por olho\n2- Olho por dois olhos")
        print("3- Não iterado\n4- Retaliador permanente\n5-Provador Ingênuo")
        print('6- Finalizar o programa')
        print()
    else: 
        print()
        print('Mantendo a mesma estrategia....')


    
