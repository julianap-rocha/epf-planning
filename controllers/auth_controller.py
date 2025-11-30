from bottle import request, response
from controllers.base_controller import BaseController
from models.usuario import Usuario
from services.usuario_service import UsuarioService


class AuthController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.service = UsuarioService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/login', ['GET', 'POST'], self.login)
        self.app.route('/cadastro', ['GET', 'POST'], self.cadastro)
        self.app.route('/logout', 'GET', self.logout)

    def login(self):
        if request.method == 'GET':
            return self.render('login', erro=None)

        email = request.forms.get('email')
        senha = request.forms.get('senha')

        usuario = self.service.buscar_email(email)

        if usuario and usuario.senha == senha:
            response.set_cookie("user_session", str(
                usuario.id), secret='minha_chave_secreta')
            return self.redirect('/dashboard')

        return self.render('login', erro="E-mail ou senha incorretos.")

    def cadastro(self):
        if request.method == 'GET':
            return self.render('cadastro', erro=None)

        nome = request.forms.get('nome')
        email = request.forms.get('email')
        senha = request.forms.get('senha')

        novo_user = Usuario(nome, email, senha)
        self.service.cadastrar(novo_user)
        return self.redirect('/login')

    def logout(self):
        response.delete_cookie("user_session")
        return self.redirect('/login')
