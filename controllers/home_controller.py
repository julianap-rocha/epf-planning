from bottle import request
from controllers.base_controller import BaseController
from services.usuario_service import UsuarioService


class HomeController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.service = UsuarioService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/dashboard', 'GET', self.dashboard)

    def dashboard(self):
        uid = request.get_cookie("user_session", secret='minha_chave_secreta')
        if not uid:
            return self.redirect('/login')

        usuario = self.service.buscar_id(int(uid))
        return self.render('dashboard', usuario=usuario)
