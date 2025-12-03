from bottle import request
from controllers.base_controller import BaseController
from services.usuario_service import UsuarioService


class HomeController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        # Instancia o service usuário pra comunicação com o banco de dados
        self.service = UsuarioService()
        self.setup_routes()

    def setup_routes(self):
        # Define as urls que o controller vai gerenciar
        self.app.route('/dashboard', 'GET', self.dashboard)

    def dashboard(self):
        # Lê o cookie do usuário e verifica se é válido
        uid = request.get_cookie("user_session", secret='minha_chave_secreta')
        if not uid:
            return self.redirect('/login')

        # Busca os dados do usuário logado
        usuario = self.service.buscar_id(int(uid))

        # Renderiza na tela principal
        return self.render('dashboard', usuario=usuario)
