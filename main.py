from app import create_app
from services.bancodedados import verificar_conexao

if __name__ == '__main__':
    verificar_conexao()
    app = create_app()
    app.run()
