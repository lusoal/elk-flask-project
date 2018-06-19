class Usuario():
    login = ""
    senha = ""
    cliente = ""

    def __init__(self, login, senha, cliente):
        self.login = login
        self.senha = senha
        self.cliente = cliente