""" • Classe Bola: Crie uma classe que modele uma bola:
a. Atributos: Cor, circunferência, material
b. Métodos: trocaCor e mostraCor """

class bola():
    def __init__ (self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, corNova):
        self.cor = corNova

    def mostraCor(self):
        return f'A cor da bola é {self.cor}'

bolaModelo = bola(cor='azul', circunferencia='70cm', material='couro')
print(bolaModelo.mostraCor()) 
bolaModelo.trocaCor('branca')
print(bolaModelo.mostraCor())


""" • Classe Quadrado: Crie uma classe que modele um quadrado:
a. Atributos: Tamanho do lado
b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área; """

class quadrado():
    def __init__ (self, lado):
        self.lado = lado

    def mudaLado(self, ladoNovo):
        self.lado = ladoNovo

    def mostraLado(self):
        return f'Cada lado do quadrado mede {self.lado}cm'

    def calculaArea(self):
        return f'A área do quadrado mede {self.lado ** 2}cm quadrados'

quadradoModelo = quadrado(6)
print(quadradoModelo.mostraLado())
quadradoModelo.mudaLado(5)
print(quadradoModelo.mostraLado())
print(quadradoModelo.calculaArea())


""" • Classe Retangulo: Crie uma classe que modele um retangulo:
a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades
de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e
de rodapés necessárias para o local. """

""" class retangulo():
    def __init__ (self, comprimento = None, largura =  None):
        self.comprimento = comprimento
        self.largura = largura

    def mudaLados(self, comprimentoNovo, larguraNova):
        self.comprimento = comprimentoNovo
        self.largura = larguraNova

    def mostraLado(self):
        return f'O comprimento do retângulo é de {self.comprimento}m e a largura é de {self.largura}m'

    def calculaArea(self):
        return self.comprimento * self.largura

    def calculaPerimetro(self):
        return (self.comprimento * 2) * (self.largura * 2)

comprimento = int(input('Digite o comprimento da sala: '))
largura = int(input('Digite a largura da sala: '))

sala = retangulo(comprimento, largura)

areaSala = sala.calculaArea()
perimetroSala = sala.calculaPerimetro()

tamanhoPiso = float(input('Informe quantos mts2 o piso possue: '))
tamanhoRodape = float(input('Informe quantos mts2 o rodapé possue: '))

quantidadePiso = areaSala / tamanhoPiso
quantidadeRodape = perimetroSala / tamanhoRodape

print(f'Serão necessários {quantidadePiso} pisos e {quantidadeRodape} rodapés') """


""" • Classe Pessoa: Crie uma classe que modele uma pessoa:
a. Atributos: nome, idade, peso e altura
b. Métodos: envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,
ela deve crescer 0,5 cm. """

class pessoa():
    def __init__ (self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1

    def engordar(self): 
        self.peso += 4

    def emagrecer(self):
        self.peso -= 3
    
    def crescer(self):
        if self.idade < 21:
            self.idade += 0.5
    
    def __str__(self):
        return f"nome: {self.nome}\nidade: {int(self.idade)}\naltura: {self.altura}\npeso: {self.peso}"


pessoa1 = pessoa(nome = 'Lucas', idade = 19, peso = 70 , altura = 1.8)
pessoa1.envelhecer()
pessoa1.engordar()
pessoa1.emagrecer()
pessoa1.crescer()
print(pessoa1)



""" • Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve
possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os
seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os
demais atributos são obrigatórios. """

class contaCorrente():
    def __init__ (self, numeroConta, nomeCorrentista, saldo = 0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def alterarNome (self, novoNome):
        self.nomeCorrentista = novoNome

    def deposito (self, valor):
        self.saldo += valor

    def saque (self, valor):
        self.saldo -= valor

pessoa1 = contaCorrente(numeroConta = 456, nomeCorrentista = 'Pedro', saldo = 50000)
pessoa1.alterarNome = 'Lucas'
print(pessoa1.alterarNome)
pessoa1.deposito(25000)
print(pessoa1.saldo)
pessoa1.saque(40000)
print(pessoa1.saldo)

""" • Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve
ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o
número do canal e o nível do volume permanecem dentro de faixas válidas. """

class tv():
    def __init__ (self, numeroCanal = 1, volume = 30):
        self.numeroCanal = numeroCanal
        self.volume = volume

    def trocaCanal (self, novoCanal):
        self.numeroCanal = novoCanal

    def aumentarVolume (self):
        self.volume += 1

    def diminuirVolume (self):
        self.volume -= 1

televisao = tv()
televisao.trocaCanal(3)
print(televisao.numeroCanal)
televisao.diminuirVolume()
televisao.diminuirVolume()
televisao.diminuirVolume()
televisao.aumentarVolume()
print(televisao.volume)


""" • Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
a. Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade;
Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar
em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os
atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo
para armazenar esta informação por que ela pode ser calculada a qualquer momento. """

class tamagushi():
    def __init__ (self, nome, fome, saude, idade):
        self.nome = nome
        self.idade = idade
        self.fome = fome
        self.saude = saude

    def 


""" • Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago)
e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente,
criando pelo menos dois       """