import os
from bottle import static_file, redirect, request
from services.usuario_service import UsuarioService


class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()
        self.usuario_service = UsuarioService()

    def _setup_base_routes(self):
        """Configura rotas básicas comuns a todos os controllers"""
        self.app.route('/', method='GET', callback=self.home_redirect)

        # Rota Genérica para CSS, JS e Imagens
        self.app.route('/static/<filename:path>', callback=self.serve_static)

    def home_redirect(self):
        """Gerencia a Landing PAge"""
        uid = request.get_cookie("user_session", secret='minha_chave_secreta')
        usuario = None

        if uid:
            usuario = self.usuario_service.buscar_id(int(uid))

        # Renderiza a Landing Page
        return self.render('landing', usuario=usuario)

    def serve_static(self, filename):
        """Serve arquivos estáticos da pasta static/"""
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        static_dir = os.path.join(base_path, 'static')

        return static_file(filename, root=static_dir)

    def render(self, template, **context):
        """Método auxiliar para renderizar templates"""
        from bottle import template as render_template
        return render_template(template, **context)

    def redirect(self, path):
        """Redirecionamento robusto"""
        return redirect(path)
