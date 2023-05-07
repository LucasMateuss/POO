class usuario():
    def __init__(self, nome_usuario):
        self.__nome_usuario = nome_usuario

    @property
    def nome_usuario(self):
        return self.__nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, novo_nome):
        self.__nome_usuario = novo_nome


class admin(usuario):
    def escrevaNome(self):
        return "Admin"

    def digaOla(self):
        return f"Olá admin, {self.nome_usuario}"


admin1 = admin("Baltazar")
print(admin1.digaOla())