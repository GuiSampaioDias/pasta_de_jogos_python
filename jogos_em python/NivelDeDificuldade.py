#=============================================================

# Nome: Nível de dificuldade

# autor: Guilheme Sampaio Dias
# data: 01-09-2023

# Jogo proposto por: MiguelVenditti

#==============================================================

def nivel_de_dificuldade():
    niveis = ["1", "2", "3"] # criei essa variavel de verificação fora do loopin para evitar redundancia
    while True:
        dificuldade = input("Qual o seu nível de habilidade?\n(1) Expert\n(2) Intermediario\n(3) Amador\nR: ")
        if dificuldade in niveis: break # O usuário só sairá deste loopin quando ele der uma opção válida
        else:
            print('Por favor insira uma opção válida')
    
# Convertendo a resposta

    if dificuldade == "1":
        return '\n5 vidas\n'
    elif dificuldade == "2":
        return '\n10 vidas\n'
    else:
        return '\n20 vidas\n'

print(nivel_de_dificuldade())

# Considerações finais mantive o código o mais próximo ao original
# Só coloquei dentro de uma função por boas práticas.
# Provavelmente vc verá mais para frente no seu curso a importância das funções