from bottle import request
from controllers.base_controller import BaseController
from models.nota import Nota
from services.nota_service import NotaService
from services.usuario_service import UsuarioService


class NotaController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        # Instancia as services para comunicação com o banco de dados
        self.service = NotaService()
        self.usuario_service = UsuarioService()
        self.setup_routes()

    def setup_routes(self):

        # Define as urls que o controller vai gerenciar
        self.app.route('/notas', 'GET', self.listar)
        self.app.route('/notas/adicionar', ['GET', 'POST'], self.adicionar)
        self.app.route('/notas/editar/<id:int>', ['GET', 'POST'], self.editar)
        self.app.route('/notas/excluir/<id:int>',
                       ['GET', 'POST'], self.excluir)

    def get_user_id(self):
        # Pega o id criptografado do cookie
        uid = request.get_cookie("user_session", secret='minha_chave_secreta')
        return int(uid) if uid else None

    # Função pra listar as notas
    def listar(self):
        # Verifica se está logado
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')

        # Busca as notas do aluno
        notas = self.service.listar_aluno(uid)
        usuario = self.usuario_service.buscar_id(uid)
        return self.render('notas', notas=notas, usuario=usuario)

    # Função pra adicionar as notas
    def adicionar(self):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')

        if request.method == 'GET':
            usuario = self.usuario_service.buscar_id(uid)
            return self.render('nota_form', nota=None, action='/notas/adicionar', erro=None, usuario=usuario)

        try:
            # Pega os dados do formulário
            materia = request.forms.get('materia').encode(
                'latin-1').decode('utf-8')
            prova = request.forms.get('nome_prova').encode(
                'latin-1').decode('utf-8')
            valor = float(request.forms.get('valor'))

            # Cria o objeto
            nova_nota = Nota(materia, prova, valor, id_usuario=uid)

            # Manda para o service salvar no banco de dados
            self.service.cadastrar(nova_nota)
            return self.redirect('/notas')
        except ValueError as e:
            return self.render('nota_form', nota=None, action='/notas/adicionar', erro=f"Erro: {e}")

    # Função pra editar as notas
    def editar(self, id):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')

        # Procura a falta existente
        nota = self.service.buscar_id(id)

        # Verifica se a nota pertence ao usuário logado
        if not nota or nota.id_usuario != uid:
            return self.redirect('/notas')

        if request.method == 'GET':
            usuario = self.usuario_service.buscar_id(uid)
            return self.render('nota_form', nota=nota, action=f'/notas/editar/{id}', erro=None, usuario=usuario)

        try:
            # Atualiza os dados
            materia = request.forms.get('materia').encode(
                'latin-1').decode('utf-8')
            prova = request.forms.get('nome_prova').encode(
                'latin-1').decode('utf-8')
            valor = float(request.forms.get('valor'))

            # Atualiza o objeto e mando pro service salvar as alterações
            nota_up = Nota(materia, prova, valor, id_usuario=uid, id=id)
            self.service.atualizar(nota_up)
            return self.redirect('/notas')
        except ValueError as e:
            return self.render('nota_form', nota=nota, action=f'/notas/editar/{id}', erro=f"Erro: {e}")

    # Função pra excluir as notas
    def excluir(self, id):
        uid = self.get_user_id()
        if not uid:
            return self.redirect('/login')

        # Verifica se a nota é do usuário antes de deletar
        nota = self.service.buscar_id(id)
        if nota and nota.id_usuario == uid:
            self.service.excluir(id)
        return self.redirect('/notas')
