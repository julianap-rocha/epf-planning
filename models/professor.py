from models.pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, email, materia, contato, id_usuario=None, id=None):
        super().__init__(nome, email)

        # Atributos
        self._id = id
        self._id_usuario = id_usuario
        self._materia = materia
        self._contato = contato

    # Método
    def exibir_dados(self):
        return f"Professor: {self.nome} | Matéria: {self.materia}"

    # Getters e Setters
    @property
    def materia(self):
        return self._materia

    @materia.setter
    def materia(self, nova_materia):
        self._materia = nova_materia

    @property
    def contato(self):
        return self._contato

    @contato.setter
    def contato(self, novo_contato):
        self._contato = novo_contato

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, novo_id_usuario):
        self._id_usuario = novo_id_usuario
