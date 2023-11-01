#dicionario ex1

"""
produtos={}

for _ in range(5):
    nome = input('Nome: ')
    preco = float(input('Preço: '))
    produtos[nome] = preco
    print()

print('Produtos com preço > R$ 50.00')

for nome in produtos:
    if produtos[nome] > 50:
        print (nome)
"""

# dicionario ex2

alunos = dict()

for i in range(2):
    ra = int(input('RA: '))
    n1 = float(input('N1: '))
    n2 = float(input('N2: '))
    n3 = float(input('N3: '))
    alunos[ra] = [n1, n2, n3]
    print()

for ra in alunos:
    media = sum(alunos[ra])/len(alunos[ra])
    print(f'RA: {ra} | Média: {media}')

#dicionario ex3
"""

def conta_vogais(texto):
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for caracter in texto:
        if caracter in 'aeiou':
            vogais[caracter] += 1
    return vogais

def exibe(vogais):
    print('-' * 20)
    print('Contagem das vogais')
    print('-' * 20)
    for vogal in 'aeiou':
        print(f'Vogal {vogal} : {vogais[vogal]} unidades')

def main():
    texto = input('Palavra: ')
    vogais = conta_vogais(texto)
    exibe(vogais)
main()
"""



