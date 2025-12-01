from bottle import request
from controllers.base_controller import BaseController
from models.falta import Falta
from services.falta_service import FaltaService
from services.usuario_service import UsuarioService


class FaltaController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.service = FaltaService()
        self.usuario_service = UsuarioService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/faltas', 'GET', self.listar)
        self.app.route('/faltas/adicionar', ['GET', 'POST'], self.adicionar)
        self.app.route('/faltas/editar/<id:int>', ['GET', 'POST'], self.editar)
        self.app.route('/faltas/excluir/<id:int>',
                       ['GET', 'POST'], self.excluir)

    def get_user_id(self):
        uid = request.get_cookie("user_session", secret='minha_chave_secreta')
        return int(uid) if uid else None

    def listar(self):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')

        faltas = self.service.listar_aluno(uid)
        usuario = self.usuario_service.buscar_id(uid)
        resumo = {}

        for f in faltas:
            if f.materia not in resumo:
                resumo[f.materia] = 0
            resumo[f.materia] += f.quantidade

        return self.render('faltas', faltas=faltas, resumo=resumo, usuario=usuario)

    def adicionar(self):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')

        if request.method == 'GET':
            usuario = self.usuario_service.buscar_id(uid)
            return self.render('falta_form', falta=None, action='/faltas/adicionar', erro=None, usuario=usuario)

        try:
            materia_raw = request.forms.get('materia')
            materia = materia_raw.encode('latin-1').decode('utf-8')
            data = request.forms.get('data')
            qtd = int(request.forms.get('quantidade'))
            nova_falta = Falta(materia, data, qtd, id_usuario=uid)
            self.service.cadastrar(nova_falta)
            return self.redirect('/faltas')
        except ValueError:
            return self.render('falta_form', falta=None, action='/faltas/adicionar', erro="Quantidade inválida")

    def editar(self, id):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')
        falta = self.service.buscar_id(id)
        if not falta or falta.id_usuario != uid:
            return self.redirect('/faltas')

        if request.method == 'GET':
            usuario = self.usuario_service.buscar_id(uid)
            return self.render('falta_form', falta=falta, action=f'/faltas/editar/{id}', erro=None, usuario=usuario)

        try:
            materia_raw = request.forms.get('materia')
            materia = materia_raw.encode('latin-1').decode('utf-8')
            data = request.forms.get('data')
            qtd = int(request.forms.get('quantidade'))
            falta_up = Falta(materia, data, qtd, id_usuario=uid, id=id)
            self.service.atualizar(falta_up)
            return self.redirect('/faltas')
        except ValueError:
            return self.render('falta_form', falta=falta, action=f'/faltas/editar/{id}', erro="Quantidade inválida")

    def excluir(self, id):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')
        falta = self.service.buscar_id(id)
        if falta and falta.id_usuario == uid:
            self.service.excluir(id)
        return self.redirect('/faltas')
