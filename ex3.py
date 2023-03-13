""" 1. Nós usamos o modificador de acesso private a fim de:
d) B e C estão corretas

Exercício de codificação

2. Vamos voltar para a classe Usuario que desenvolvemos nas atividades anteriores. Agora vamos
definir o primeiroNome do usuário como uma propriedade privada (private).
Esta é a classe Usuario:
class Usuario:
# seu código vai aqui

2.1 Crie uma propriedade na classe Usuario chamada primeiroNome e evite que qualquer código
de fora da classe altere o seu valor, usando o modificador de acesso apropriado.

2.2 Crie um método para definir o valor da propriedade primeiroNome. Use o modificador de
acesso correto para ele.

2.3 Agora, crie um método para retornar o valor primeiroNome.

2.4 Crie um objeto chamado usuario1. Depois defina seu primeiro nome como "Joe" e faça com
que ele retorne este nome.

3. Crie uma classe chamada Empregado(), com três propriedades: nome, salario (deve ser
privada) e projeto. Ela também possui um método chamado “trabalho()”, que deverá
imprimir o nome do funcionário e o projeto em que ele está trabalhando e um outro método
chamado “mostrar()” para exibir os detalhes desse empregado (i.e. nome e salário). Atente
para o modificador de acesso da propriedade “salario”. Use o método adequado para ter
acesso a ela. Crie um objeto desta classe (i.e. instância) e use os métodos para visualizar os
dados.

4. Crie uma classe chamada Robo(). Ela deverá ter duas propriedades privadas: nome e
ano_construcao. Também deverá ter um método de nome “diga_alo()”, para mostrar na
tela o nome do robô e seu ano de construção. Crie os métodos “setters” e “getters”
necessários. Instancie a classe e use os métodos criados para visualizar / atualizar os dados.

5. Implemente uma classe chamada Laptop que possua um atributo privado chamado “preco”
que armazena o preço do laptop (sem qualquer validação). Em seguida, implemente um método
para ler esse atributo chamado “get_preco()” e um método para modificar esse atributo
chamado “set_preco()” sem validação também. Em seguida, crie uma instância da classe
Laptop siga estas etapas:
• usando o método “get_preco()” imprima o valor do atributo “preco” na tela
• usando o método “set_preco()”, defina o valor do atributo “preco” para 3999”

6. Implemente uma classe chamada Pessoa que tenha dois atributos privados chamados
“primeiroNome” e “ultimoNome”, respectivamente. Em seguida, implemente métodos
chamados “getPrimeiroNome()” e “getUltimoNome()”, para ler os atributos, e os
métodos “setPrimeiroNome()” e “setUltimoNome()” para atribuir valores a eles. Depois
crie uma instância da classe Pessoa definindo os seguintes valores:
primeiroNome = 'João'
ultimoNome = 'Carvalho'

Após, imprima os valores desses atributos no console. """


class usuario:
    __primeiroNome = ""

    def setName(self, primeiroNome):
        self.__primeiroNome = primeiroNome

    def getName(self):
        return self.__primeiroNome


usuario1 = usuario()
usuario1.setName("Joe")
print(usuario1.getName())


class empregado:
    nome = ""
    projeto = ""
    __salario = ""

    def trabalho(self):
        return f"O(A) Funcionário(a) {self.nome} está no projeto {self.projeto}"

    def setSalario(self, salario):
        self.__salario = salario

    def mostrar(self):
        return f"Funcionário(a): {self.nome}\nSalário: {self.__salario}"


funcionario = empregado()
funcionario.nome = "Joe"
funcionario.setSalario("2200")
funcionario.projeto = "Site de Cosméticos"
print(f"\n{funcionario.trabalho()}\n{funcionario.mostrar()}")


class robo:
    __nome = ""
    __anoConstrucao = ""

    def set(self, nome, anoConstrucao):
        self.__nome = nome
        self.__anoConstrucao = anoConstrucao

    def digaAlgo(self):
        return f"Nome: {self.__nome}\nAno de Construção: {self.__anoConstrucao}"


robo1 = robo()
robo1.set("Astro Boy", "1963")
print(f"\n{robo1.digaAlgo()}")


class laptop:
    __preco = ""

    def setPreco(self, preco):
        self.__preco = preco

    def getPreco(self):
        return f"Preço: {self.__preco}"


note = laptop()
note.setPreco("3999")
print(f"\n{note.getPreco()}")


class pessoa:
    __primeiroNome = ''
    __ultimoNome = ''

    def setName(self, primeiroNome, ultimoNome):
        self.__primeiroNome = primeiroNome
        self.__ultimoNome = ultimoNome

    def getName(self):
        return f'Nome: {self.__primeiroNome}\nÚltimo Nome: {self.__ultimoNome}'
    
pessoa1 = pessoa()
pessoa1.setName('João', 'Carvalho')
print(f'\n{pessoa1.getName()}')

    