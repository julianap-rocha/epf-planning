from bottle import request
from controllers.base_controller import BaseController
from models.falta import Falta
from services.falta_service import FaltaService
from services.usuario_service import UsuarioService


class FaltaController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        # Instancia as services para comunicação com o banco de dados
        self.service = FaltaService()
        self.usuario_service = UsuarioService()
        self.setup_routes()

    def setup_routes(self):
        # Define as urls que o controller vai gerenciar
        self.app.route('/faltas', 'GET', self.listar)
        self.app.route('/faltas/adicionar', ['GET', 'POST'], self.adicionar)
        self.app.route('/faltas/editar/<id:int>', ['GET', 'POST'], self.editar)
        self.app.route('/faltas/excluir/<id:int>',
                       ['GET', 'POST'], self.excluir)

    def get_user_id(self):
        # Pega o id criptografado do cookie
        uid = request.get_cookie("user_session", secret='minha_chave_secreta')
        return int(uid) if uid else None

    # Função que lista as faltas cadastradas
    def listar(self):
        # Verifica se o usuário está logado
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')

        # Busca os dados no banco de dados
        faltas = self.service.listar_aluno(uid)
        usuario = self.usuario_service.buscar_id(uid)

        # Faz uma lista de um resumo as matérias comando as faltas
        resumo = {}

        for f in faltas:
            if f.materia not in resumo:
                resumo[f.materia] = 0
            resumo[f.materia] += f.quantidade

        return self.render('faltas', faltas=faltas, resumo=resumo, usuario=usuario)

    # Função pra adicionar faltas
    def adicionar(self):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')

        if request.method == 'GET':
            usuario = self.usuario_service.buscar_id(uid)
            return self.render('falta_form', falta=None, action='/faltas/adicionar', erro=None, usuario=usuario)

        try:
            # Pega os dados do formulário
            materia_raw = request.forms.get('materia')
            materia = materia_raw.encode('latin-1').decode('utf-8')

            data = request.forms.get('data')
            qtd = int(request.forms.get('quantidade'))

            # Cria o objeto
            nova_falta = Falta(materia, data, qtd, id_usuario=uid)

            # Manda para o service salvar no banco de dados
            self.service.cadastrar(nova_falta)
            return self.redirect('/faltas')
        except ValueError:
            return self.render('falta_form', falta=None, action='/faltas/adicionar', erro="Quantidade inválida")

    # Função pra editar faltas
    def editar(self, id):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')

        # Procura a falta existente
        falta = self.service.buscar_id(id)

        # Verifica se a falta pertence ao usuário logado
        if not falta or falta.id_usuario != uid:
            return self.redirect('/faltas')

        if request.method == 'GET':
            usuario = self.usuario_service.buscar_id(uid)
            return self.render('falta_form', falta=falta, action=f'/faltas/editar/{id}', erro=None, usuario=usuario)

        try:
            # Atualiza os dados
            materia_raw = request.forms.get('materia')
            materia = materia_raw.encode('latin-1').decode('utf-8')
            data = request.forms.get('data')
            qtd = int(request.forms.get('quantidade'))

            # Atualiza o objeto e mando pro service salvar as alterações
            falta_up = Falta(materia, data, qtd, id_usuario=uid, id=id)
            self.service.atualizar(falta_up)
            return self.redirect('/faltas')
        except ValueError:
            return self.render('falta_form', falta=falta, action=f'/faltas/editar/{id}', erro="Quantidade inválida")

    # Função pra excluir faltas
    def excluir(self, id):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')

        # Verifica se a falta é do usuário antes de deletar
        falta = self.service.buscar_id(id)
        if falta and falta.id_usuario == uid:
            self.service.excluir(id)
        return self.redirect('/faltas')
