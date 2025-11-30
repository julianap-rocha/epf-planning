from bottle import request
from controllers.base_controller import BaseController
from models.nota import Nota
from services.nota_service import NotaService


class NotaController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.service = NotaService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/notas', 'GET', self.listar)
        self.app.route('/notas/adicionar', ['GET', 'POST'], self.adicionar)
        self.app.route('/notas/editar/<id:int>', ['GET', 'POST'], self.editar)
        self.app.route('/notas/excluir/<id:int>',
                       ['GET', 'POST'], self.excluir)

    def get_user_id(self):
        uid = request.get_cookie("user_session", secret='minha_chave_secreta')
        return int(uid) if uid else None

    def listar(self):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')
        notas = self.service.listar_aluno(uid)
        return self.render('notas', notas=notas)

    def adicionar(self):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')

        if request.method == 'GET':
            return self.render('nota_form', nota=None, action='/notas/adicionar', erro=None)

        try:
            materia = request.forms.get('materia')
            prova = request.forms.get('nome_prova')
            valor = float(request.forms.get('valor'))
            nova_nota = Nota(materia, prova, valor, id_usuario=uid)
            self.service.cadastrar(nova_nota)
            return self.redirect('/notas')
        except ValueError as e:
            return self.render('nota_form', nota=None, action='/notas/adicionar', erro=f"Erro: {e}")

    def editar(self, id):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')
        nota = self.service.buscar_id(id)
        if not nota or nota.id_usuario != uid:
            return self.redirect('/notas')

        if request.method == 'GET':
            return self.render('nota_form', nota=nota, action=f'/notas/editar/{id}', erro=None)

        try:
            materia = request.forms.get('materia')
            prova = request.forms.get('nome_prova')
            valor = float(request.forms.get('valor'))
            nota_up = Nota(materia, prova, valor, id_usuario=uid, id=id)
            self.service.atualizar(nota_up)
            return self.redirect('/notas')
        except ValueError as e:
            return self.render('nota_form', nota=nota, action=f'/notas/editar/{id}', erro=f"Erro: {e}")

    def excluir(self, id):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')
        nota = self.service.buscar_id(id)
        if nota and nota.id_usuario == uid:
            self.service.excluir(id)
        return self.redirect('/notas')
