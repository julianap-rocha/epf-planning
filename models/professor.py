from models.pessoa.py import Pessoa

def Professor(Pessoa):
    def __init__(self, nome, email):
        super().__init__(nome, email)
        self._materia = materia
        self._contato = contato
        
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