""" 1. Qual das alternativas abaixo melhor define o termo “classe”?
b) Define e obtém as propriedades e métodos dela.

2. Qual das alternativas abaixo melhor define o termo “objeto”?
a) Um objeto nos dá a capacidade de trabalhar com a classe e ter várias instâncias desta mesma classe.

3. Qual das alternativas abaixo melhor explica o termo "propriedade"?
b) Uma variável dentro de uma classe.

4. Qual das alternativas abaixo melhor explica o termo "método"?
c) A incorporação de uma ação real.''

Exercício de codificação
Quase todos os aplicativos ou blogs lidam com os usuários. Seja o processo de registro (cadastro), o login e
logout, o envio de lembretes aos usuários que perderam suas senhas ou a alteração delas sob demanda, todo
o código que lida com os usuários pode ser agrupado em uma única classe. Em nosso exemplo, chamamos a
classe que lida com usuários, Usuario, de acordo com a convenção de nomenclatura vigente.
Vamos escrever uma classe Usuario com as ferramentas que acabamos de adquirir. Esta classe conterá o nome
e sobrenome de cada usuário e será capaz de dizer “Olá” a qualquer pessoa que use nosso aplicativo.

5. Escreva o que você acha que deveria ser o nome da classe, os nomes das propriedades para o
primeiro e último nome (sobrenome) e o nome do método que retorna “Olá”.
Nome da classe: usuario
Propriedades: primeiroNome , ultimoNome
Método: hello 

6. Escreva a classe Usuario e adicione as propriedades e o método (em Python):

7. Crie a primeira instância e chame-a de usuario1.

8. Defina os valores do primeiro e último nome para usuario1.

9. Obter o nome e sobrenome do usuário e imprima-os na tela com o comando print.

10. Use o método que retorna “Olá” com as variáveis primeiro nome e último nome para dizer Olá ao
usuário.

11. Crie (instancie) outro objeto. Chame-o de usuario2, dê a ele o primeiro nome de “Jane” e o
sobrenome de “Silva”, e depois diga “Olá” ao usuário. """

class usuario:
    primeiroNome = ''
    ultimoNome = ''

    def hello(self):
        return('Olá')
    
usuario1 = usuario()
usuario1.primeiroNome = 'Lucas'
usuario1.ultimoNome = 'Souza'

print(usuario1.primeiroNome, usuario1.ultimoNome)

print(usuario1.hello(), usuario1.primeiroNome, usuario1.ultimoNome)

usuario2 = usuario()
usuario2.primeiroNome = 'Jane'
usuario2.ultimoNome = 'Silva'

print(usuario2.hello(), usuario2.primeiroNome, usuario2.ultimoNome)
