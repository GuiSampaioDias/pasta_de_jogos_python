#-------------------------------------
#       Desafio de Código

# Autor: Guilherme Sampaio Dias

#-------------------------------------


# 1. Reverta a ordem das palavras nas frases, mantendo a ordem das palavras

"""
def main():
    test1 = 'Hello, Word! OpenAi is amazing.'
    ex1(test1)
    test2 = 'Ana foi para praia nas férias!'
    ex1(test2)
    test3 = 'A tecnologia veio para revolucionar e resignificar o mundo.'
    ex1(test3)

def ex1(frase):
    x = frase.split()
    for _ in range(1,len(x)-1):
        print(x[-_], end = ' ')
    print(f'{x[-(len(x)-1)]} {x[-len(x)]}')
    print()

main()

"""

# 2. Remova todos os caracteres duplicados da steing abaixo


"""
def main():
    test1 = 'Hello, World!'
    ex2(test1)
    test2 = 'Banana verde!'
    ex2(test2)
    
def ex2(frase):
    caracteres = []
    for _ in range(len(frase)):
        if frase[_] not in caracteres:
            caracteres.append(frase[_])
            print(frase[_], end = '')
    print()

main()
"""

# 3. Encontre a substring palindroma mais longa na string abaixo



#4. Coloque em maiúscula a primeira letra de cada frase na string 

"""
def main():
    test1 = 'hello. How are you? i´m fine, thank you.'
    ex4(test1)
    test2 = 'hoje é um bom dia estudar. você não acha?'
    ex4(test2)
    
def ex4(frase):
    for _ in range(len(frase)):
        if _ == 0:
            print(frase[_].upper(), end = '')
        elif  _ != 1 and (frase[_-2] == '.' or frase[_-2] == '?' or frase[_-2] == '!') :
            print(frase[_].upper(),end = '')
        else: 
            print(frase[_], end = '')
    print()

main()

"""

# 5. Verifique se a string é um anagrama de um palindromo

def main():
    test1 = 'Anotaram a data da maratona'
    ex5(test1)
    test2 = 'A sacada da casa'
    ex5(test2)
    test3 = 'Ame o poema'
    ex5(test3)
    test4 = 'Manga da camisa'
    ex5(test4)

def ex5(frase):
    frase = frase.replace(' ', '').lower()
    frase_invertida = frase[::-1]
    print('true' if frase == frase_invertida else 'false')

main()











