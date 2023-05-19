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


""" 6. Implemente o Diagrama de Classes de Contas Bancárias ilustrado abaixo. """

class cCorrente():
    def __init__ (self, numero, saldo, cliente):
        self._numero = numero
        self._saldo = saldo
        self.cliente = cliente

    def creditar(self, valor):
        self._saldo -= valor

    def debitar(self, valor):
        self._saldo += valor

    @property
    def saldo(self):
        return self._saldo
    

class cPoupanca(cCorrente):
    def __init__ (self, numero, saldo, cliente, saldoMinimo):
        super().__init__ (numero, saldo, cliente)
        self._saldoMinimo = saldoMinimo

    def debitar(self, valor):
        super().debitar(valor)

    def atualizar_saldo(self):
        return self.get_saldo()
    
    @property
    def saldoMinimo(self):
        return self._saldoMinimo
    

class cInvestimento(cCorrente):
    def __init__ (self, numero, saldo, cliente, diaInvestimento, periodo):
        super().__init__ (self, numero, cliente)
        self.diaInvestimento = diaInvestimento
        self.periodo = periodo 

    
class cEspecial(cCorrente):
    def __init__ (self, numero, saldo, cliente, limite):
        super().__init__ (numero, saldo, cliente)
        self.limite = limite

    def debitar(self, valor):
        super().debitar(valor)
        return self._saldo
    
cliente1 = cCorrente(1, 1500, 'Lucas')
cliente2 = cPoupanca(2, 100, 'Mateus', 1000)
cliente3 = cInvestimento(3, 1500, 'José', '29/09/2022', '2 anos')
cliente4 = cEspecial(4, 1500, 'Gabriel', 800)

cliente1.debitar(1000)
cliente1.creditar(800)
print(f'\n{cliente1.saldo}')
cliente2.debitar(1000)
print(f'\n{cliente2.saldo}')



""" 7. Implemente o Diagrama de Classes de Empregados ilustrado abaixo. """
class empregado():
    def __init__ (self, codigo, nome, email, salario):
        self.codigo = codigo
        self.nome = nome
        self.email = email
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    def aumentaSalario (self, percentual):
        self._salario += ((self._salario * percentual) / 100)

class chefe(empregado):
    def __init__ (self, codigo, nome, email, salario, beneficio):
        super().__init__ (codigo, nome, email, salario)
        self.beneficio = beneficio

    def aumentaSalario(self, percentual):
        super().aumentaSalario(percentual) 
        self._salario += self.beneficio

    
class estagiario(empregado):
    def __init__ (self, codigo, nome, email, salario, desconto):
        super().__init__ (codigo, nome, email, salario)
        self.desconto = desconto

    def aumentaSalario(self, percentual):
        super().aumentaSalario(percentual) 
        self._salario -= self.desconto


chefe1 = chefe('1', 'Lucas', 'lucas@gmail.com', 5000, 500)
estagiario1 = estagiario('2', 'Pedro', 'pedro@gmail.com', 1100, 100)
chefe1.aumentaSalario(10)
estagiario1.aumentaSalario(20)  
print(f'\n{chefe1.salario}\n{estagiario1.salario}')


""" 8. Implemente o código para as classes abaixo:
a) crie uma classe chamada Ingresso que possui um valor em reais e um método
imprimeValor()
b) crie uma classe VIP que herda de Ingresso e possui um valor adicional. Crie também um método
que retorne o valor do ingresso VIP (como o adicional incluído).
c) crie uma classe Normal, que herda Ingresso e possui um método que imprime: "Ingresso Normal".
d) crie uma classe CamaroteInferior (que possui a localização do ingresso e métodos para acessar e
imprimir esta localização) e uma classe CamaroteSuperior, que é mais cara (possui valor
adicional). Esta última possui um método para retornar o valor do ingresso. Ambas as classes herdam
a classe VIP. """

class ingresso():
    def __init__ (self, reais):
        self.reais = reais

    def imprimeValor(self):
        print(f'Valor do Ingresso: R${self.reais}')

class vip(ingresso):
    def __init__ (self, reais, valorAdicional):
        super().__init__ (reais)
        self.valorAdicional = valorAdicional

    def imprimeValorVip(self):
        print(f'Valor do Ingresso VIP: R${(self.reais) + (self.valorAdicional)}')

class normal(ingresso):
    def imprimeIngressoNormal(self):
        print('Ingresso Normal')

class camaroteInferior(vip):
    def __init__ (self, localizacao, metodoDeAcesso):
        self.localizacao = localizacao 
        self.metodoDeAcesso = metodoDeAcesso

    def imprimeCamaroteInferior(self):
        print(f'Camarote: A1\nMétodo de Acesso: Porta vermelha')

class camaroteSuperior(vip):
    def __init__ (self, reais, taxaCamarote, valorAdicional):
        super().__init__ (reais, valorAdicional)
        self.taxaCamarote = taxaCamarote

    def imprimeValorCamaroteSuperior(self):
        print(f'Valor do Camarote Superior: R${(self.reais) + (self.taxaCamarote)}')


ingressoNormal = ingresso(30)
ingressoVip = vip(30, 20)
ingressoCamaroteSuperior = camaroteSuperior(30, 100, 20)

print(ingressoNormal.imprimeValor())
print(ingressoVip.imprimeValorVip())
print(ingressoCamaroteSuperior.imprimeValorCamaroteSuperior())  


""" 9. Implemente o código para as classes abaixo:
a) uma classe Funcionario com os atributos (nome, endereço, telefone, email) e com os
métodos (construtor, exibeDados())
b) crie a classe Assistente, que também é Funcionário, e que possui um número de
matrícula (use o método get).
c) sabendo que os Assistentes Técnicos possuem um bônus salarial e que os Assistentes Administrativos
possuem um turno (dia ou noite) e um adicional noturno, crie as classes Tecnico e
Administrativo. Para cada um destas classes, imprima o número de matrícula e o nome de cada
um deles. """

class funcionario():
    def __init__ (self, nome, endereco, telefone, email):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def exibeDados (self):
        print(f'\nNome: {self.nome}\nEndereço: {self.endereco}\nTelefone: {self.telefone}\nEmail: {self.email}')

class assistente(funcionario):
    def __init__ (self, nome, endereco, telefone, email, matricula):
        super().__init__ (nome, endereco, telefone, email)
        self.matricula = matricula

class tecnico(assistente):
    def __init__ (self, nome, endereco, telefone, email, matricula, salario, bonus):
            super().__init__ (nome, endereco, telefone, email, matricula)
            self.salario = salario
            self.bonus = bonus

    def salarioTecnico (self):
        return self.salario + self.bonus

class administrativo(assistente):
    def __init__ (self, nome, endereco, telefone, email, matricula, salario, turno, adicional):
            super().__init__ (nome, endereco, telefone, email, matricula)
            self.salario = salario
            self.turno = turno
            self.adicional = adicional

    def salarioAdministrativo(self):
        if (self.turno) == 'Noturno' or 'noturno':
            return self.salario + self.adicional
        else:
            return self.salario

assistenteTecnico = tecnico('Lucas', 'Joinville', '47988750246', 'lucas@gmail.com', '12345', 2100, 400)
assistenteAdministrativo = administrativo('Pedro', 'São Paulo', '11984651238', 'pedro@gmail.com', '67891', 2000, 'noturno', 300)
print(f'\nNome: {assistenteTecnico.nome}\nEndereço: {assistenteTecnico.endereco}\nTelefone: {assistenteTecnico.telefone}\nEmail: {assistenteTecnico.email}\nMatrícula: {assistenteTecnico.matricula}\nSalário: {assistenteTecnico.salarioTecnico()}')
print(f'\nNome: {assistenteAdministrativo.nome}\nEndereço: {assistenteAdministrativo.endereco}\nTelefone: {assistenteAdministrativo.telefone}\nEmail: {assistenteAdministrativo.email}\nMatrícula: {assistenteAdministrativo.matricula}\nSalário: {assistenteAdministrativo.salarioAdministrativo()}')

""" 10. Observe o Diagrama de Classes na figura abaixo:

Faça o seguinte:
a) Crie as classes e métodos conforme o diagrama
b) Instancie uma pessoa pobre e faça trabalhar
c) Instancie uma pessoa rica e que faça compras """

class pessoa():
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

class rica(pessoa):
    def __init__ (self, nome, idade, dinheiro):
        super().__init__ (nome, idade)
        self.dinheiro = dinheiro

    def fazCompras(self):
        return('Indo ao Shopping...')


class pobre(pessoa):
    def __init__ (self, nome, idade):
        super().__init__ (nome, idade)    

    def trabalha(self):
        return('Indo trabalhar...')


class miseravel(pessoa):
    def __init__ (self, nome, idade):
        super().__init__ (nome, idade)    

    def mendiga (self):
        return('Mendigando...')


rica1 = rica('Lucas', 19, 50000)
pobre1 = pobre('José', 19)
miseravel1 = miseravel('Gabriel', 20)

print(f'\nRico: {rica1.fazCompras()}\nPobre: {pobre1.trabalha()}\nMiserável: {miseravel1.mendiga()}')

