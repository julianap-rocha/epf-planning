from bottle import request
from controllers.base_controller import BaseController
from models.professor import Professor
from services.professor_service import ProfessorService
from services.usuario_service import UsuarioService


class ProfessorController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.service = ProfessorService()
        self.usuario_service = UsuarioService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/professores', 'GET', self.listar)
        self.app.route('/professores/adicionar',
                       ['GET', 'POST'], self.adicionar)
        self.app.route('/professores/editar/<id:int>',
                       ['GET', 'POST'], self.editar)
        self.app.route('/professores/excluir/<id:int>',
                       ['GET', 'POST'], self.excluir)

    def get_user_id(self):
        uid = request.get_cookie("user_session", secret='minha_chave_secreta')
        return int(uid) if uid else None

    def get_usuario_logado(self, uid):
        return self.usuario_service.buscar_id(uid)

    def listar(self):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')
        profs = self.service.listar_aluno(uid)
        usuario = self.get_usuario_logado(uid)
        return self.render('professores', professores=profs, usuario=usuario)

    def adicionar(self):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')

        if request.method == 'GET':
            usuario = self.usuario_service.buscar_id(uid)
            return self.render('professor_form', professor=None, action='/professores/adicionar', erro=None, usuario=usuario)

        nome = request.forms.get('nome').encode('latin-1').decode('utf-8')
        email = request.forms.get('email')
        materia = request.forms.get('materia').encode(
            'latin-1').decode('utf-8')
        contato = request.forms.get('contato').encode(
            'latin-1').decode('utf-8')

        novo_prof = Professor(nome, email, materia, contato, id_usuario=uid)
        self.service.cadastrar(novo_prof)
        return self.redirect('/professores')

    def editar(self, id):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')
        prof = self.service.buscar_id(id)
        if not prof or prof.id_usuario != uid:
            return self.redirect('/professores')

        if request.method == 'GET':
            usuario = self.usuario_service.buscar_id(uid)
            return self.render('professor_form', professor=prof, action=f'/professores/editar/{id}', erro=None, usuario=usuario)

        nome = request.forms.get('nome').encode('latin-1').decode('utf-8')
        email = request.forms.get('email')
        materia = request.forms.get('materia').encode(
            'latin-1').decode('utf-8')
        contato = request.forms.get('contato').encode(
            'latin-1').decode('utf-8')

        prof_up = Professor(nome, email, materia, contato,
                            id_usuario=uid, id=id)
        self.service.atualizar(prof_up)
        return self.redirect('/professores')

    def excluir(self, id):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')
        prof = self.service.buscar_id(id)
        if prof and prof.id_usuario == uid:
            self.service.excluir(id)
        return self.redirect('/professores')
