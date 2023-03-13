""" 1. Qual palavra-chave (keyword) você usaria para ter acesso às propriedades e métodos de uma classe
estando dentro dela?
c) A palavra-chave self

Exercício de Codificação
Na atividade prática anterior, escrevemos o método hello() dentro da classe Usuario. No exercício a
seguir, adicionaremos a este método a capacidade de acessar as propriedades da classe com a palavra-chave
self.
A classe Usuario poderia ser codificada assim:
class Usuario():
# as propriedades
primeiroNome = “”
ultimoNome = “”
#metodo que diz Olá ao usuario
def hello(self)
return "Olá"

2. Acrescente ao método hello() a capacidade de acessar a propriedade primeiroNome, para que
o método possa retornar a string "Olá, primeiroNome".

3. Crie um novo objeto com o primeiro nome de "Jonnie" e sobrenome de "Bravo".

4. Use o comando print no método hello() para o objeto usuario1 e observe o resultado. """


class usuario:
    primeiroNome = ""
    ultimoNome = ""

    def hello(self):
        return f"Olá {self.primeiroNome}"


usuario1 = usuario()
usuario1.primeiroNome = "Jonnie"
usuario1.ultimoNome = "Bravo"

print(usuario1.hello())
