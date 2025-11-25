class Nota:
    def __init__(self, materia, nome_prova, valor, id_usuario=None, id=None):
        
        # Atributos
        self._id = id
        self._id_usuario = id_usuario
        self._materia = materia
        self._nome_prova = nome_prova
        self._valor = valor

# Getters e Setters
    @property
    def materia(self):
        return self._materia

    @materia.setter
    def materia(self, nova_materia):
        self._materia = nova_materia
        
    @property
    def nome_prova(self):
        return self._nome_prova

    @nome_prova.setter
    def nome_prova(self, novo_nome):
        self._nome_prova = novo_nome

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, novo_valor):
        self._valor = novo_valor
    
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