from app import create_app
from services.bancodedados import verificar_conexao

# Garante que o site só rode na main
if __name__ == '__main__':

    # Verifica se o banco existe e se conecta
    verificar_conexao()

    # Mostra o link do site no terminal
    print("http://localhost:8080")

    # Cria o objeto da aplicação
    app = create_app()

    # Inicia o servidor web
    app.run()
