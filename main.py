from app import create_app
from services.bancodedados import verificar_conexao

if __name__ == '__main__':
    verificar_conexao()
    print("http://localhost:8080")
    app = create_app()
    app.run()
