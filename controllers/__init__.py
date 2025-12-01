from bottle import Bottle
from controllers.auth_controller import AuthController
from controllers.home_controller import HomeController
from controllers.nota_controller import NotaController
from controllers.falta_controller import FaltaController
from controllers.professor_controller import ProfessorController


def init_controllers(app: Bottle):
    AuthController(app)
    HomeController(app)
    NotaController(app)
    FaltaController(app)
    ProfessorController(app)
