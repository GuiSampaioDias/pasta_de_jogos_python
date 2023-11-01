"""class Professor:
    def __init__ (self,nome,drt,contratacao,status,disciplina,cargaMax):
        self.nome = nome
        self.drt = drt
        self.contratacao = contratacao
        self.status = status
        self.disciplina = disciplina
        self.cargaMax = cargaMax"""
"""
class Professor:
    def __init__(self, nome, drt, contratacao, status, disciplina, cargaMax):
        self.nome = nome
        self.drt = drt
        self.contratacao = contratacao
        self.status = status
        self.disciplina = disciplina
        self.cargaMaxima = cargaMax

    def setDisciplina(self, disciplina):
        self.disciplina = disciplina
    def setCargaMaxima(self, cargaMax):
            if cargaMax <= 40:
                self.cargaMaxima = cargaMax
            else:
                print('Carga máxima ultrapassou o limite!')
    def exibe(self):
            print(f'Nome........: {self.nome}')
            print(f'DRT.........: {self.drt}')
            print(f'Contratação.: {self.contratacao}')
            print(f'Status......: {self.status}')
            print(f'Disciplina..: {self.disciplina}')
            print(f'Carga máxima: {self.cargaMaxima}')
            print()
"""
#exe 1
"""
class Livro:
    def __init__ (self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas =  num_paginas

"""
# exer 2
"""
class Triangulo:
    def __init__ (self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
        

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c

a = float(input('Lado a : '))
b = float(input('Lado b : '))
c = float(input('Lado c : '))
t=Triangulo(a,b,c)
print(f'O perimetro é {t.calcular_perimetro():.2f}')
        
"""
# exer 3
"""
class Televisao:
    def __init__(self):
        self.canal = None
        self.volume = 0

    def aumentar_volume(self):
        self.volume +=1

    def diminuir_volume(self):
        self.volume -= 1

    def alterar_canal(self,canal):
        self.canal=canal

tv=Televisao()
tv.alterar_canal(6)
tv.aumentar_volume()
tv.aumentar_volume()


print(f'A tv esta no canal {tv.canal}')
print(f'A tv esta vo volume {tv.volume}')
"""
"""
class Televisao:
    def __init__(self):
        self.canal = None
        self.volume = 0

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

    def alterar_canal(self, canal):
        self.canal = canal
tv = Televisao()
tv.alterar_canal(6)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()

print(f'A tv está no canal {tv.canal}')    # A tv está no canal 6
print(f'A tv está no volume {tv.volume}')  # A tv está no volume 2

"""
#exer 4
"""
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, a):
        self.salario += (a/100)*self.salario

n = input('Qual o nome do funcionário: ')
s = float(input('Salário do funcionário: R$ '))
funcionario= Funcionario(n, s)
a = float(input('Qual o percentual que será acrecido do salário: '))
funcionario.aumentar_salario(a)
print(f'O funcionário {funcionario.nome} passara a receber R$ {funcionario.salario}')
"""
#exer 5
"""
class Carro:
    def __init__(self):
        self.quantidade_combustivel = 0

    def adicionar_combustivel(self,litros):
        self.quantidade_combustivel += litros

    def obter_combustivel(self):
        return self.quantidade_combustivel

    def andar(self, distancia):
        self.quantidade_combustivel -=(distancia *0.2)

meu_carro = Carro()
meu_carro.adicionar_combustivel(20)
meu_carro.andar(80)
print('Litros de combustível no tanque: ', meu_carro.obter_combustivel())

"""

#exerc 01 dia 28/03/2023
"""
class Carro:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibir_dados(self):
        print(f'Marca.: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Placa.: {self.placa}')
        print()
        
c1 = Carro('Toyota', 'Corola', 'cdh213')
c2 = Carro('Fiat', 'Fiesta', 'dj123')
c1.exibir_dados()
c2.exibir_dados()
"""

#exer 02 28/03/2023
"""
class Funcionario:
    def __init__(self, nome, sobrenome, salario_mensal):
        self.nome = nome
        self.sobrenom = sobrenome
        if  salario_mensal > 0:
            self.salario_mensal = salario_mensal
        else:
            self.salario_mensal = 0

    def aumentar_salario(self):
        self.salario_mensal += 10 / 100 * self.salario_mensal

    def salario_anual(self):
        return 12 * self.salario_mensal

f1 = Funcionario('Pedro', 'António', 4000)
f2 = Funcionario('Ana', 'Benatti', 10000)

print('Antes do aumento')
print(f'Salário anual: {f1.salario_anual():.2f}')
print(f'Salário anual: {f2.salario_anual():.2f}')
f1.aumentar_salario()
f2.aumentar_salario()
print('\nDepois do aumento')
print(f'Salário anual: {f1.salario_anual():.2f}')
print(f'Salário anual: {f2.salario_anual():.2f}')
"""

# exer 03 28/03/2023
"""
class ContaBancaria:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = 0

    def depositar(self, valor,senha):
        if senha != self.senha:
            print('senha incorreta')
        else:
            self.saldo += valor
            print('Saldo atualizado R$ {self.saldo:.2f}')

    def sacar(self, valor, senha):
        if senha != self.senha:
            print('senha incorreta')
        else:
            if valor <= self.saldo:
                self.saldo -= valor
                print('Saldo atualizado R$ {self.saldo:.2f}')
            else:
                print('Saldo insuficiente')
            
cliente = ContaBancaria(12345, 'Gui', 123456)
cliente.depositar(100,1222)
cliente.sacar(100,1523)
cliente.depositar(50000,123456)
print(cliente.saldo)
cliente.sacar(100,123456)
print(cliente.saldo)
"""
# exerci 04 28/03/2023
"""
alunos=[]
class Aluno:
    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.notas = []

    def inserir_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        media = sum(self.notas)/ len(self.notas)
        return media
a1 = Aluno(123, 'Ana', '1A')
a1.inserir_nota(10)
a1.inserir_nota(9)
a1.inserir_nota(10)
med1=a1.calcular_media()
a2 = Aluno(123, 'Fernanda', '1A')
a2.inserir_nota(10)
a2.inserir_nota(8)
a2.inserir_nota(10)
med2=a2.calcular_media()
a3 = Aluno(123, 'Paula', '1A')
a3.inserir_nota(7)
a3.inserir_nota(9)
a3.inserir_nota(10)
med3=a3.calcular_media()
alunos.append(a1.nome)
alunos.append(a2.nome)
alunos.append(a3.nome)
print(f'A {a1.nome} teve média: {a1.calcular_media():.2f}')
print(f'A {a2.nome} teve média: {a2.calcular_media():.2f}')        
print(f'A {a3.nome} teve média: {a3.calcular_media():.2f}')
"""
#ac2 ex1
"""
def lista_convidados():
    noivo = set()
    noiva = set()
    convidado = input()
    while convidado != 'ACABOU':
        conv=convidado.split(';')
        if conv[1] == 'noivo':
            noivo.add(conv[0])
        else:
            noiva.add(conv[0])
        convidado = input()
    return (noivo, noiva)

def final(noivo, noiva):
    print('-'*20)
    print('LISTA FINAL')
    print('-'*20)
    for nome in sorted(noivo | noiva):
        print(nome,end='\n')
    print()

def noiva(noiva, noivo):      
    print('-'*20)
    print('APENAS NOIVA')
    print('-'*20)
    for nome in sorted(noiva - noivo):
        print(nome,end='\n')
    print()
def noivo(noivo, noiva):
    print('-' * 20)
    print('APENAS NOIVO')
    print('-' * 20)
    for nome in sorted(noivo- noiva):
        print(nome, end = '\n')
    print()
    
def ambos(noivo, noiva):
    print('-' * 20)
    print('POR AMBOS')
    print('-' * 20)
    for nome in sorted(noivo & noiva):
        print(nome, end = '\n')
    print()
def  apenas_um(noivo, noiva):  
    print('-' * 20)
    print('POR APENAS UM DELES')
    print('-' * 20)
    for nome in sorted(noivo ^ noiva):
        print(nome, end = '\n')


def main():
    x, y = lista_convidados() 
    final(x, y)
    noiva(y, x)
    noivo(x, y)
    ambos(x, y)
    apenas_um(x, y)

main()
"""
# exercício 01 relacionamento de classes
"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.carro = None
    
    def comprar_carro(self, carro):
        self.carro = carro
    

class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano


meucarro = Carro('Volkswagem', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25)
eu.comprar_carro(meucarro)          
print('Meu nome:', eu.nome)                    # imprime: João
print('Modelo do meu carro:', eu.carro.modelo) # imprime: Gol
print('Placa do meu carro:', eu.carro.placa)   # imprime: AAA-1111
"""
# exercício 02 relacionamento de classes
"""
class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_valor(self):
        valor_compra = 0
        for f in self.produtos:
            valor_compra += f.preco * f.quantidade
        return valor_compra
    
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

cafe = Produto('Café solúvel', 5.50, 1)
arroz = Produto('Arroz integral', 4.90, 2)
feijao = Produto('Feijão preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é:', meu_pedido.calcular_valor())      
"""

# exercicio 03 relacionamento de classes
"""
class Carro:
    def __init__(self, pneu1, pneu2, pneu3, pneu4):
        self.ligado = False
        self.pneu1 = pneu1
        self.pneu2 = pneu2
        self.pneu3 = pneu3 
        self.pneu4 = pneu4 

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def verificar_pneu(self):
        if self.ligado == False:
            print('Carro Desligado')
        else:
            print(f'{p1.pressao}')
            print(f'{p2.pressao}')
            print(f'{p3.pressao}')
            print(f'{p4.pressao}')

class Pneu:
    def __init__(self, pressao):
        self.pressao = pressao

    def furar(self):
        self.pressao = 0 

p1 = Pneu(32)
p2 = Pneu(32)
p3 = Pneu(36)
p4 = Pneu(36)

meucarro = Carro (p1, p2, p3, p4)

meucarro.ligar()
meucarro.pneu3.furar()
meucarro.verificar_pneu()   # exibir a pressão em cada pneu
meucarro.desligar()
meucarro.verificar_pneu() 
"""
# exercício 04 relacionamento de classes

class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf 
        self.idade = idade

class Medico:
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao

class Exame:
    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado
    
    def imprimir_exame(self):
        print(f'Resultado do exame de {exame01.descricao}')
        print()
        print(f'Nome paciente: {paciente.nome}')
        print(f'CPF: {paciente.cpf}   idade: {paciente.idade} anos')
        print()
        print(f'Resultado: {exame01.resultado} para {exame01.descricao}')
        print()
        print(f'--Dados da médica responsável--')
        print(f'Nome.........: {medico.nome}')
        print(f'crm..........: {medico.crm}')
        print(f'especilização: {medico.especializacao}')
        print()

paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clinico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')
exame01.imprimir_exame()



# exercicio 05 relacionamento de classes
"""
class Cofre:
    def __init__(self):
        self.moeda = []

    def adicionar(self, moeda):
        self.moeda.append(moeda)

    def calcular_total(self):
        total = 0
        for mo in self.moeda:
            total += mo.valor
        return total
    
class Moeda:
    def __init__(self, valor):
        self.valor = valor

moeda1 = Moeda(0.25)
moeda2 = Moeda(0.50)
moeda3 = Moeda(1.00)
cofre = Cofre()
cofre.adicionar(moeda1)
cofre.adicionar(moeda2)
cofre.adicionar(moeda3)
print('O valor total é:', cofre.calcular_total())
"""






