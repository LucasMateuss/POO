""" Vamos voltar para a classe Usuario que desenvolvemos nas atividades anteriores. No entanto, em vez de
usar métodos setter, vamos definir os valores para o primeiro e último nome através de um método construtor.
Esta é a classe Usuario:

class Usuario():
__primeiroNome = “”
__ultimoNome = “”

1. Acrescente à classe Usuario um método construtor para definir um valor para a propriedade
primeiroNome assim que o objeto for criado.

2. Acrescente ao construtor a capacidade de definir o valor da propriedade ultimoNome, bem como a
propriedade primeiroNome.

3. Adicione à classe Usuario um método público chamado getNomeCompleto() que retorna o
nome completo do usuário.

4. Crie um novo objeto, usuario1, e passe para o construtor os valores do primeiro e último nome. O
primeiro nome é "Johnny" e o sobrenome é "Bravo" (você pode escolher sua combinação preferida
de primeiro e último nome).

5. Obtenha o nome completo e imprima-o na tela. """


class usuario:
    def __init__(self, primeiroNome=None, ultimoNome=None):
        if primeiroNome != None:
            self.__primeiroNome = primeiroNome
        if ultimoNome != None:
            self.__ultimoNome = ultimoNome

    def __str__(self):
        return f"Nome completo: {self.__primeiroNome} {self.__ultimoNome}"


print(usuario("Lucas", "Souza"))
