class Falta:
    def __init__(self, materia, data, quantidade, id_usuario=None, id=None):
        
        # Atributos
        self._id = id
        self._id_usuario = id_usuario
        self._materia = materia
        self._data = data
        self._quantidade = quantidade

    # Getters e Setters
    @property
    def materia(self):
        return self._materia
    
    @materia.setter
    def materia(self, nova_materia):
        self._materia = nova_materia

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, nova_data):
        self._data = nova_data

    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, nova_quantidade):
        self._quantidade = nova_quantidade
    
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