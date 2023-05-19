""" Nesta atividade prática, vamos retornar à classe Usuario que usamos nas atividades anteriores. Para
implementar o princípio do polimorfismo, criaremos uma classe chamada Usuario. A partir dela
criaremos algumas classes como: para calcular o número de pontuações que um usuário tem, e o número
de artigos que ele criou ou editou. Baseado nesta classe (Usuario), vamos criar as classes Autor e
Editor, e ambas calcularão o número de pontuações com o método calcPontuacao(), embora o
valor calculado seja diferente entre estas duas classes. """

class usuario():
    def __init__(self, primereiroNome, ultimoNome, pontos = 0, numeroArtigos = 0):
        self.primereiroNome = primereiroNome
        self.ultimoNome = ultimoNome
        self.pontos = pontos
        self.__numeroArtigos = numeroArtigos


    @property
    def numeroArtigos(self):
        return self.__numeroArtigos

    @numeroArtigos.setter
    def numeroArtigos(self, nart):
        self.__numeroArtigos = nart


    def calcularPontos(self):
        return self.numeroArtigos


class autor(usuario):
    def calcularPontos(self):
        return super().calcularPontos() * 10 + 20 

    
class editor(usuario):
    def calcularPontos(self):
        return super().calcularPontos() * 6 + 15 
    

autor1 = autor('Lucas', 'Souza', 0, 8)
editor1 = editor('João', 'Guilherme', 0, 15)
print(autor1.calcularPontos())
print(editor1.calcularPontos())