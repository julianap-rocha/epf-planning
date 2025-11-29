from models.pessoa import Pessoa


class Usuario(Pessoa):
    def __init__(self, nome, email, senha, id=None):
        super().__init__(nome, email)

        # Atributos
        self._id = id
        self._senha = senha
        self._notas = []
        self._faltas = []
        self._professores = []

    # Método
    def exibir_dados(self):
        return f"Aluno: {self.nome} | Email: {self.email}"

    # Gettes e Setters
    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def notas(self):
        return self._notas

    @property
    def faltas(self):
        return self._faltas

    @property
    def professores(self):
        return self._professores
