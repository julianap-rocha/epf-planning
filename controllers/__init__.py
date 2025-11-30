from bottle import Bottle
from controllers.auth_controller import AuthController
from controllers.home_controller import HomeController
from controllers.professor_controller import ProfessorController

def init_controllers(app: Bottle):
    AuthController(app)
    HomeController(app)
    ProfessorController(app)