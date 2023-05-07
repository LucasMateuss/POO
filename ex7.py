from math import pi

""" 1. Crie uma classe Pessoa com os atributos nome e idade. Crie uma classe Aluno que herda de
Pessoa e adicione o atributo nota. Crie um método para imprimir as informações da Pessoa e um
método para imprimir as informações do Aluno. """

class pessoa():
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

class aluno(pessoa):
    def __init__ (self, nome, idade, nota):
        super().__init__(nome, idade)
        self.nota = nota
    
    def __str__ (self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nNota: {self.nota}'
    
aluno1 = aluno('Lucas', 19, 9)
print(aluno1)


""" 2. Crie uma classe Veiculo com os atributos marca, modelo e ano. Crie classes filhas Carro e
Moto que adicionam o atributo quantidade_de_portas e cilindradas, respectivamente. Crie
um método para imprimir as informações do Veiculo e um método para imprimir as informações
do Carro e da Moto. """

class veiculo():
    def __init__ (self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class carro(veiculo):
    def __init__ (self, marca, modelo, ano, qtdPortas):
        super().__init__(marca, modelo, ano)
        self.qtdPortas = qtdPortas

    def __str__ (self):
        return f'\nMarca: {self.marca}\nModelo: {self.modelo}\nAno = {self.ano}\nQuantidade de Portas: {self.qtdPortas}'
    
class moto(veiculo):
    def __init__ (self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def __str__ (self):
        return f'\nMarca: {self.marca}\nModelo: {self.modelo}\nAno = {self.ano}\nCilindradas: {self.cilindradas}'
    
carro1 = carro('Honda', 'Civic', 1999, 4)
print(carro1)
moto1 = moto('Honda', 'Shadow', 2009, 750)
print(moto1)


""" 3. Crie uma classe Animal com os atributos nome e peso, e um método comer(). Em seguida, crie
duas subclasses, Cachorro e Gato, que herdam da classe Animal. Adicione um método
latir() na classe Cachorro e um método miar() na classe Gato. """

class animal():
    def __init__ (self, nome, peso):
        self.nome = nome
        self.peso = peso

    def comer (self):
        print('\nComendo')
        self.peso += 1

class cachorro(animal):
    def __init__ (self, nome, peso):
        super().__init__(nome, peso)

    def __str__ (self):
        return f'\nNome: {self.nome}\nPeso: {self.peso}\nAuAu'
    
class gato(animal):
    def __init__ (self, nome, peso):
        super().__init__(nome, peso)

    def __str__ (self):
        return f'\nNome: {self.nome}\nPeso: {self.peso}\nMiau'
    
cachorro1 = cachorro('Paçoca', 7)
print(cachorro1)
cachorro1.comer()
print(cachorro1)
gato1 = gato('Garfield', 2.5)
print(gato1)
gato1.comer()
print(gato1)

""" 4. Crie uma classe Pessoa com os atributos nome e idade. Em seguida, crie uma classe
Funcionario que herda da classe Pessoa e adicione o atributo salario. Crie um método
aumento() na classe Funcionario que aumenta o salário em uma porcentagem específica."""

class pessoa():
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

class funcionario(pessoa):
    def __init__ (self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def aumento (self, porcentagem):
        self.salario += self.salario * (porcentagem / 100)

    def __str__ (self):
        return f'\nNome: {self.nome}\nIdade: {self.idade}\nSalário: {self.salario}'

funcionario1 = funcionario('Lucas', '19', 1800)
print(funcionario1)
funcionario1.aumento(10)
print(funcionario1)


""" 5. Crie uma classe Forma com o método area(). Em seguida, crie duas subclasses: Retangulo e
Circulo, que herdam da classe Forma. Adicione os atributos comprimento e largura na
classe Retangulo e o atributo raio na classe Circulo. Agora calcula a área de cada polígono. """

class forma():
    def area(self, objeto):
        return f"Area do {objeto} = "
    
class retangulo(forma):
    def __init__ (self, comprimento, largura, nome):
        self. comprimento = comprimento
        self.largura = largura
        self.nome = nome

    def area (self):
        return f"\n{super().area(self.nome)} {self.comprimento * self.largura}"
    
class circulo(forma):
    def __init__(self, raio, nome):
        self.nome = nome
        self.raio = raio

    def area(self):
        return f"\n{super().area(self.nome)} {pi * self.raio ** 2}"
    
retangulo1 = retangulo(9, 4, 'Retângulo')
print(retangulo1.area())
circulo1 = circulo(5, 'Círculo')
print(circulo1.area())
