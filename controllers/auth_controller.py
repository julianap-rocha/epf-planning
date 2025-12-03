from bottle import request, response
from controllers.base_controller import BaseController
from models.usuario import Usuario
from services.usuario_service import UsuarioService


class AuthController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        # Instancia o service usuário pra comunicação com o banco de dados
        self.service = UsuarioService()
        self.setup_routes()

    def setup_routes(self):
        # Define as urls que o controller vai gerenciar
        self.app.route('/login', ['GET', 'POST'], self.login)
        self.app.route('/cadastro', ['GET', 'POST'], self.cadastro)
        self.app.route('/logout', 'GET', self.logout)

    # Função para logar
    def login(self):
        if request.method == 'GET':
            return self.render('login', erro=None)

        email = request.forms.get('email')
        senha = request.forms.get('senha')

        # Verifica se existe um usuário com esse email
        usuario = self.service.buscar_email(email)

        # Verifica se as informações de login estão certas
        if usuario and usuario.senha == senha:
            # Gera o cookie para identificar a sessão
            response.set_cookie("user_session", str(
                usuario.id), secret='minha_chave_secreta')
            return self.redirect('/dashboard')

        return self.render('login', erro="E-mail ou senha incorretos.")

    # Função pra cadastrar
    def cadastro(self):
        if request.method == 'GET':
            return self.render('cadastro', erro=None)

        # Pega os dados do formulário
        nome = request.forms.get('nome')
        email = request.forms.get('email')
        senha = request.forms.get('senha')

        # Cria um objeto com os dados
        novo_user = Usuario(nome, email, senha)

        # Manda para o service salvar no banco de dados
        self.service.cadastrar(novo_user)
        return self.redirect('/login')

    # Função pra deslogar
    def logout(self):
        # Deleta o cookie da sessão
        response.delete_cookie("user_session")
        return self.redirect('/login')
