from math import pi 

""" 1. Crie uma hierarquia de classes para animais, com uma classe mãe Animal e subclasses Cachorro,
Gato e Peixe. Cada subclasse deve ter um método falar() que retorne uma string
representando o som que o animal faz. Demonstre o polimorfismo chamando falar() nas
instâncias de cada subclasse. """

class animal:
    def falar(self):
        return 'Som animal'
    
class cachorro(animal):
    def falar(self):
        return 'au au'
    
class gato(animal):
    def falar(self):
        return 'miau'
    
class peixe(animal):
    def falar(self):
        return 'bloob'
    
cachorro1 = cachorro()
gato1 = gato()
peixe1 = peixe()

for animal in (cachorro1, gato1, peixe1):
    print(f'\n{animal.falar()}')


""" 2. Crie uma classe Animal com um método falar(). Em seguida, crie duas classes filhas,
Cachorro e Gato, que herdam da classe Animal. Cada uma destas classes filhas deve ter seu
próprio método falar() que retorne um som diferente (e.g. latidos para o cachorro e miados para
o gato). Em seguida, crie uma lista de animais que inclua um cachorro e um gato. Por fim, itere
sobre a lista e chame o método falar() de cada animal. """

class animal:
    def falar(self):
        return 'Som animal'
    
class cachorro(animal):
    def falar(self):
        return 'au au'
    
class gato(animal):
    def falar(self):
        return 'miau'
    
class peixe(animal):
    def falar(self):
        return 'bloob'
    
cachorro1 = cachorro()
gato1 = gato()
peixe1 = peixe()

animais = [cachorro1, gato1, peixe1]

for animal in animais:
    print(f'\n{animal.falar()}')


""" 3. Crie uma classe chamada Carro com um método dirigir(). Em seguida, crie duas subclasses,
CarroGasolina e CarroEletrico, cada uma com sua própria implementação de dirigir().
Demonstre o polimorfismo passando instâncias de ambas as subclasses para uma função que recebe
um objeto Carro. """

class carro():
    def dirigir(self):
        return 'Estou dirigindo um carro'
    
class carroGasolina(carro):
    def dirigir(self):
        return 'Estou dirigindo um carro movido a gasolina'
    
class carroEletrico(carro):
    def dirigir(self):
        return 'Estou dirigindo um carro Elétrico'
    
carro1 = carroGasolina()
carro2 = carroEletrico()

print(f'\n{carro1.dirigir()}{carro2.dirigir()}')


""" 4. Crie uma classe Forma com um método area(). Em seguida, crie duas classes filhas, Circulo e Quadrado, que herdam da classe Forma. Cada uma destas classes filhas deve ter seu próprio método area() que calcula a área do círculo ou do quadrado, respectivamente. Em seguida, crie uma lista de formas que inclua um círculo e um quadrado. Por fim, itere sobre a lista e chame o método area() de cada forma. """

class forma():
    def area(self):
        return 'Área de uma forma'
    
class circulo(forma):
    def area(self, raio):
        return f'Área do Círculo: {pi * (raio ** 2 )}'
    
class quadrado(forma):
    def area(self, lado):
        return f'Área do Quadrado: {lado ** 2}'
    
forma1 = circulo()
forma2 = quadrado()
formas = [forma1, forma2]

for forma in formas:
    print(f'\n{forma.area(2)}')

""" 5. Crie uma classe Empregado com um método pagar_salario(). Em seguida, crie duas classes
filhas, EmpregadoHora e EmpregadoMes, que herdam da classe Empregado. Cada uma das
classes filhas deve ter seu próprio método pagar_salario() que calcula o salário com base no
número de horas trabalhadas ou no salário mensal, respectivamente. Em seguida, crie uma lista de
funcionários que inclua um funcionário horista e um funcionário mensalista. Por fim, itere sobre a
lista e chame o método pagar_salario() de cada funcionário. """

class empregado():
    def pagarSalario(self):
        pass

class empregadoHora(empregado):
    def pagarSalario(self, pagHora):
        return f'\nUm empregado trabalhando 40 horas semanais e ganhando RS{pagHora} por hora irá ter um sálario de R${160 * pagHora}'

class empregadoMes(empregado):
    def pagarSalario(self, pagmes):
        return f'\nUm empregado trabalhando 40 horas semanais ganha {pagmes}'
    
funcionario1 = empregadoHora()
funcionario2 = empregadoMes()

print(funcionario1.pagarSalario(12))
print(funcionario2.pagarSalario(1800))

""" 6. Crie uma classe chamada ContaBancaria com os métodos deposito() e retirada(). Crie
duas subclasses: ContaPoupanca e ContaCorrente. Cada uma dessas subclasses deve ter sua
própria taxa de juros (a taxa de juros da Conta Poupança é maior que a da Conta Corrente). """

class contaBancaria():
    def __init__ (self, saldo = 0):
        self.saldo = saldo

        
    def deposito(self):
        pass


    def retirada(self):
        pass


class contaPoupanca(contaBancaria):
    def deposito(self, valor):
        self.saldo += valor * 1.05

    def retirada(self, valor):
        self.saldo -= valor


class contaCorrente(contaBancaria):
    def deposito(self, valor):
        self.saldo += valor * 1.02

    def retirada(self, valor):
        self.saldo -= valor

conta1 = contaPoupanca()
conta2 = contaCorrente()

conta1.deposito(1800)
print(conta1.saldo)
conta1.retirada(90)
print(conta1.saldo)

conta2.deposito(1800)
print(conta2.saldo)
conta2.retirada(90)
print(conta2.saldo)
