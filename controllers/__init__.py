from bottle import Bottle
# Importa todas as classes controller
from controllers.auth_controller import AuthController
from controllers.home_controller import HomeController
from controllers.nota_controller import NotaController
from controllers.falta_controller import FaltaController
from controllers.professor_controller import ProfessorController

# Função para iniciar todos os controllers de uma vez
def init_controllers(app: Bottle):
    AuthController(app)
    HomeController(app)
    NotaController(app)
    FaltaController(app)
    ProfessorController(app)
