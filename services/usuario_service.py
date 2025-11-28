import sqlite3
from models.usuario import Usuario
from services.bancodedados import get_db_connection


class UsuarioService:

    # Cadastra o usuário no banco
    def cadastrar(self, usuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                           INSERT INTO usuarios (nome, email, senha)
                           VALUES (?,?,?)""", (usuario.nome, usuario.email, usuario.senha))
            conn.commit()
            conn.close()
            print("O Usuário foi cadastrado com sucesso!")
        except sqlite3.IntegrityError:
            print("Erro: Esse email já está sendo utilizado.")

    # Busca o email para verificar se está correto os dados
    def buscar_email(self, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        l = cursor.fetchone()
        conn.close()

        if l:
            return Usuario(nome=l[1], email=l[2], senha=l[3], id=l[0])
        return None

    # Confirma se o cookie é válido
    def buscar_id(self, id_usuario):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,))
        l = cursor.fetchone()
        conn.close()

        if l:
            return Usuario(nome=l[1], email=l[2], senha=l[3], id=l[0])
        return None
