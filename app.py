from bottle import Bottle, response
from config import Config


class App:
    def __init__(self):
        # Inicializa o bottle
        self.bottle = Bottle()

        # Carrega as configurações do bottle
        self.config = Config()

    def setup_routes(self):

        # Importa os init_controllers
        from controllers import init_controllers

        print('🚀 Inicializa rotas!')

        # Passa a instância do bottle para os controllers
        init_controllers(self.bottle)

    def run(self):
        # Configura todas as rotas antes de começar
        self.setup_routes()

        # Inicia o servidor web
        self.bottle.run(
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )


def create_app():
    return App()
