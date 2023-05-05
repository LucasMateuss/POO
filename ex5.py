""" • Classe Bola: Crie uma classe que modele uma bola:
a. Atributos: Cor, circunferência, material
b. Métodos: trocaCor e mostraCor """


class bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, corNova):
        self.cor = corNova

    def mostraCor(self):
        return f"A cor da bola é {self.cor}"


bolaModelo = bola(cor="azul", circunferencia="70cm", material="couro")
print(bolaModelo.mostraCor())
bolaModelo.trocaCor("branca")
print(bolaModelo.mostraCor())


""" • Classe Quadrado: Crie uma classe que modele um quadrado:
a. Atributos: Tamanho do lado
b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área; """


class quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudaLado(self, ladoNovo):
        self.lado = ladoNovo

    def mostraLado(self):
        return f"Cada lado do quadrado mede {self.lado}cm"

    def calculaArea(self):
        return f"A área do quadrado mede {self.lado ** 2}cm quadrados"


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


class pessoa:
    def __init__(self, nome, idade, peso, altura):
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


pessoa1 = pessoa(nome="Lucas", idade=19, peso=70, altura=1.8)
pessoa1.envelhecer()
pessoa1.engordar()
pessoa1.emagrecer()
pessoa1.crescer()
print(pessoa1)


""" • Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve
possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os
seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os
demais atributos são obrigatórios. """


class contaCorrente:
    def __init__(self, numeroConta, nomeCorrentista, saldo=0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def alterarNome(self, novoNome):
        self.nomeCorrentista = novoNome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor


pessoa1 = contaCorrente(numeroConta=456, nomeCorrentista="Pedro", saldo=50000)
pessoa1.alterarNome = "Lucas"
print(pessoa1.alterarNome)
pessoa1.deposito(25000)
print(pessoa1.saldo)
pessoa1.saque(40000)
print(pessoa1.saldo)

""" • Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve
ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o
número do canal e o nível do volume permanecem dentro de faixas válidas. """


class tv:
    def __init__(self, numeroCanal=1, volume=30):
        self.numeroCanal = numeroCanal
        self.volume = volume

    def trocaCanal(self, novoCanal):
        self.numeroCanal = novoCanal

    def aumentarVolume(self):
        self.volume += 1

    def diminuirVolume(self):
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

# class tamagushi():
#     def __init__ (self, nome, fome, saude, idade):
#         self._nome = nome
#         self._idade = idade
#         self._fome = fome
#         self._saude = saude

#     @property
#     def nome (self):
#         return self._nome

#     @nome.setter
#     def nome (self, novoNome):
#         self._nome = novoNome

#     @property
#     def fome (self):
#         return self._fome

#     @fome.setter
#     def fome (self, novaFome):
#         self._fome = novaFome

#     @property
#     def saude (self):
#         return self._saude

#     @saude.setter
#     def saude (self, novaSaude):
#         self._saude = novaSaude

#     @property
#     def idade (self):
#         return self._idade

#     @idade.setter
#     def idade (self, novaIdade):
#         self._idade = novaIdade

#     def calculaHumor (self):
#         return self._fome + self._saude

#     def __str__ (self):
#         return f"""
#         \nNome: {self.nome}
#         Fome: {self._fome}
#         Saude: {self._saude}
#         Idade: {self._idade}
#         Humor: {self.calculaHumor()}
#         """

# bichinho = tamagushi(str(input('\nDigite o nome do seu Tamagushi: ')), 10, 5, 1)
# opcao = 0
# while opcao != 4:
#     opcao = int(input("""
#     \n=-=-=-=-= Cuide do seu Tamagushi =-=-=-=-=
#     [ 1 ] Alimentar
#     [ 2 ] Cuidar
#     [ 3 ] Dormir
#     [ 4 ] Sair
#     Sua escolha: """))
#     if opcao == 1:
#         bichinho.fome -= 1
#         bichinho.saude += 1
#     elif opcao == 2:
#         bichinho.saude += 2
#     elif opcao == 3:
#         bichinho.fome += 1
#         bichinho.saude += 1
#         bichinho.idade += 1
#     elif opcao == 4:
#         print("Até Mais. Volte Logo!")
#     else:
#         print('Insira uma opção válida')
#     print(bichinho)


""" • Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago)
e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente,
criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e
verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o
outro. É possível criar um macaco canibal? """


class macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, *comidas):
        for comida in comidas:
            if isinstance(comida, macaco):
                self.bucho.append(comida.nome)
            else:
                self.bucho.append(comida)

    def digerir(self):
        self.bucho[0]

    def verBucho(self):
        estomago = ", ".join(comida for comida in self.bucho)
        return f"Bucho: {estomago}"


botas = macaco("Botas")
george = macaco("George")
botas.comer("Banana", "Maça", "Manga", george)
print(botas.verBucho())

""" • Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
a. Possua uma classe chamada Ponto, com os atributos x e y.
b. Possua uma classe chamada Retangulo, com os atributos largura e altura.
c. Possua uma função para imprimir os valores da classe Ponto
d. Possua uma função para encontrar o centro de um Retângulo.
e. Você deve criar alguns objetos da classe Retangulo.
f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do
retângulo, que deve ser um objeto da classe Ponto.
g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo
ponto que indique os valores de x e y para o centro do objeto.
h. O valor do centro do objeto deve ser mostrado na tela
i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo. """

""" class ponto:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __str__ (self):
        return f'x:{self.x}\ny:{self.y}'
    
class retangulo:
    def __init__ (self, largura, altura, pontoInicial):
        self.largura = largura
        self.altura = altura
        self.pontoInicial = pontoInicial

    def centro(self):
        x_centro = self.pontoInicial.x + self.largura/2
        y_centro = self.pontoInicial.y + self.altura/2
        return ponto(x_centro, y_centro)
    
ponto1 = ponto(0, 0)
retangulo1 = retangulo(5, 3, ponto1)

ponto2 = ponto(2, 2)
retangulo2 = retangulo(4, 6, ponto2)

opcao = 0

while opcao != 3:
    print("Escolha uma opção:")
    print("[ 1 ] Alterar valores do retângulo 1")
    print("[ 2 ] Alterar valores do retângulo 2")
    print("[ 3 ] Sair")

    opcao = int(input("Opção escolhida: "))

    if opcao == 1:
        largura = float(input("Nova largura do retângulo 1: "))
        altura = float(input("Nova altura do retângulo 1: "))
        x = float(input("Nova coordenada x do ponto inicial do retângulo 1: "))
        y = float(input("Nova coordenada y do ponto inicial do retângulo 1: "))

        ponto1 = ponto(x, y)
        retangulo1 = retangulo(largura, altura, ponto1)

        centro_retangulo1 = retangulo1.centro()
        print(centro_retangulo1)

    elif opcao == 2:
        largura = float(input("Nova largura do retângulo 2: "))
        altura = float(input("Nova altura do retângulo 2: "))
        x = float(input("Nova coordenada x do ponto inicial do retângulo 2: "))
        y = float(input("Nova coordenada y do ponto inicial do retângulo 2: "))

        ponto2 = ponto(x, y)
        retangulo2 = retangulo(largura, altura, ponto2)

        centro_retangulo2 = retangulo2.centro()
        print(centro_retangulo2)

    elif opcao == 3:
        print("Encerrando o programa...")

    else:
        print("Opção inválida!") """

""" • Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
i. tipoCombustivel.
ii. valorLitro
iii. quantidadeCombustivel
b. Possua no mínimo esses métodos:
i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a
quantidade de litros que foi colocada no veículo
ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de
combustível e mostra o valor a ser pago pelo cliente.
iii. alterarValor( ) – altera o valor do litro do combustível.
iv. alterarCombustivel( ) – altera o tipo do combustível.
v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na
bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de
combustível total na bomba. """

""" class bombaCombustível:
    def __init__ (self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor (self, dinheiro):
        tanque = dinheiro / self.valorLitro
        self.quantidadeCombustivel -= tanque
        return f'Foram abastecidos {int(tanque)} litros'
    
    def abastecerPorLitro (self, litros):
        tanque = litros * self.valorLitro
        self.quantidadeCombustivel -= tanque
        return f'Foram abastecidos {int(tanque)} litros'

    @property
    def valorLitro(self):
        return self._valorLitro

    @valorLitro.setter
    def valorLitro(self, novo_valor):
        self._valorLitro = novo_valor

    @property
    def tipoCombustivel(self):
        return self._tipoCombustivel

    @tipoCombustivel.setter
    def tipoCombustivel(self, novo_tipo):
        self._tipoCombustivel = novo_tipo

    @property
    def quantidadeCombustivel(self):
        return self._quantidadeCombustivel
    
    @quantidadeCombustivel.setter
    def quantidadeCombustivel(self, nova_quantidade):
        self._quantidadeCombustivel = nova_quantidade

bomba = bombaCombustível('Diesel', 4.7, 750)
print(bomba.abastecerPorValor(55))
print(bomba.abastecerPorLitro(30))


• Classe Carro: Implemente uma classe chamada Carro com as seguintes propriedades:
a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa
quantidade de combustível no tanque.
b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância,
reduzindo o nível de combustível no tanque de gasolina.
d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
e. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
meuFusca = Carro(15) # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20) # abastece com 20 litros de combustível.
meuFusca.andar(100) # anda 100 quilômetros.
meuFusca.obterGasolina() # Imprime o combustível que resta no tanque. """

class carro:
    def __init__ (self, consumo, quantidadeCombustivel):
        self.consumo = consumo
        self.quantidadeCombustivel = quantidadeCombustivel

    def andar(self, km):
        self.quantidadeCombustivel -= (km // self.consumo)
        print(f'Você andou {km} KM e sobrou {self.quantidadeCombustivel} litros de combustível no carro')

    def adicionarGasolina (self, abastecer):
        self.quantidadeCombustivel += abastecer
        print(f'Você abasteceu {abastecer} litros e agora o carro possue {self.quantidadeCombustivel} litros no tanque')

carro1 = carro(15, 10)
print(carro1.andar(100))
print(carro1.adicionarGasolina(100))

""" • Classe Conta de Investimento: Faça uma classe chamada contaInvestimento que seja semelhante à
classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um
construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros
(sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma
poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método
adicioneJuros() cinco vezes e imprime o saldo resultante.
 """

class contaInvestimento:
    def __init__(self, numeroConta, nomeCorrentista, saldo=0, taxaJuros = 0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    def alterarNome(self, novoNome):
        self.nomeCorrentista = novoNome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def adicioneJuros (self):
        self.saldo += self.saldo * self.taxaJuros

pessoa1 = contaInvestimento(456, 'Pedro', 1000, (10 / 100))
count = 1
while count <= 5:
    pessoa1.adicioneJuros()
    count += 1
print(pessoa1.saldo)

""" • Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e
um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para
devolver nome e salário. Escreva um pequeno programa que teste sua classe.
• Aprimore a classe do exercício anterior para adicionar o método aumentarSalario
(porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
• Exemplo de uso:
harry=funcionário("Harry",25000)
harry.aumentarSalario(10) """

class funcionario:
    def __init__ (self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def aumentaSalario (self, aumento):
        self.salario += self.salario * (aumento / 100)

    def __str__ (self):
        return f"Nome: {self.nome}\nSalário: {self.salario}"

funcionario1 = funcionario('Lucas', 1000)
funcionario1.aumentaSalario(30)
print(funcionario1)
    
""" • Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário
especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

• Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores
exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada
no menu, for informada na escolha do usuário. Dica: acrescente um método especial str() à classe
Bichinho.

• Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles
através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário
tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu
deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os
bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa
mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio. """

class tamagushi():
    def __init__ (self, nome, fome, saude, idade, tedio):
        self._nome = nome
        self._idade = idade
        self._fome = fome
        self._saude = saude
        self._tedio = tedio
        

    @property
    def nome (self):
        return self._nome

    @nome.setter
    def nome (self, novoNome):
        self._nome = novoNome

    @property
    def fome (self):
        return self._fome

    @fome.setter
    def fome (self, novaFome):
        self._fome = novaFome

    @property
    def saude (self):
        return self._saude

    @saude.setter
    def saude (self, novaSaude):
        self._saude = novaSaude

    @property
    def idade (self):
        return self._idade

    @idade.setter
    def idade (self, novaIdade):
        self._idade = novaIdade

    @property
    def tedio (self):
        return self._tedio
    
    @tedio.setter
    def tedio (self, novoTedio):
        self._tedio = novoTedio

    def calculaHumor (self):
        return self._saude + self._fome - self.tedio

    def __str__ (self):
        return f"""
    \nNome: {self.nome}
    Fome: {self._fome}
    Saude: {self._saude}
    Idade: {self._idade}
    Tédio: {self._tedio}
    Humor: {self.calculaHumor()}
        """

fazendinha = [tamagushi('Shrek', 10, 5, 1, 0), tamagushi('Sheila', 10, 5, 1, 0), tamagushi('Sansão', 10, 5, 1, 0)]
opcao = 0
while opcao != 4:
    opcao = int(input("""
    \n=-=-=-=-= Cuide do seu Tamagushi =-=-=-=-=
    [ 1 ] Alimentar
    [ 2 ] Brincar
    [ 3 ] Dormir
    [ 4 ] Sair
    Sua escolha: """))
    if opcao == 1:
        qtd_comida = int(input('\nDigite o tanto de comida que você deseja dar: '))
        for bichinho in fazendinha:
            bichinho.fome -= qtd_comida
            bichinho.saude += qtd_comida
            bichinho.tedio += 1
    elif opcao == 2:
        for bichinho in fazendinha:
            bichinho.tedio -= 1
    elif opcao == 3:
        for bichinho in fazendinha:
            bichinho.fome += 1
            bichinho.saude += 1
            bichinho.idade += 1
            bichinho.tedio += 1
    elif opcao == 4:
        print("Até Mais. Volte Logo!")
    else:
        print('Insira uma opção válida')
    for bichinho in fazendinha:
        print(bichinho)
