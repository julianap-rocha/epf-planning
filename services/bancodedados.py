import sqlite3

db_path = 'data/planning.db'

# Função para conectar no banco de dados
def get_db_connection():
    conn = sqlite3.connect(db_path)
    return conn

#Função para testar a conexão
def verificar_conexao():
    try:
        conn = get_db_connection()
        conn.close()
        print("Banco de dados conectado")
    except sqlite3.Error as e:
        print(f"Erro ao conectar no banco: {e}")