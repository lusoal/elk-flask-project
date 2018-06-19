from model.usuario import Usuario

class UsuarioController():
    usuario = None

    def __init__(self, usuario):
        self.usuario = usuario
        

    def get_credentials(self):
        #acesso ao banco de dados
        login = self.usuario.login
        senha = self.usuario.senha

        #Fazer logica para verificar Login
        return True