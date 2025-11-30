from models.falta import Falta
from services.bancodedados import get_db_connection


class FaltaService:

    # Função pra cadastrar faltas
    def cadastrar(self, falta):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO faltas (id_usuario, materia, data, quantidade)
            VALUES (?, ?, ?, ?)
        """, (falta.id_usuario, falta.materia, falta.data, falta.quantidade))
        conn.commit()
        conn.close()

    # Função pra listar as faltas do aluno específico
    def listar_aluno(self, id_usuario):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM faltas WHERE id_usuario = ?", (id_usuario,))
        linhas = cursor.fetchall()
        conn.close()

        lista_faltas = []
        for l in linhas:
            nova_falta = Falta(
                materia=l[2],
                data=l[3],
                quantidade=l[4],
                id_usuario=l[1],
                id=l[0]
            )
            lista_faltas.append(nova_falta)

        return lista_faltas

    # Função pra buscar falta específica
    def buscar_id(self, id_falta):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM faltas WHERE id = ?", (id_falta,))
        l = cursor.fetchone()
        conn.close()

        if l:
            return Falta(materia=l[2], data=l[3], quantidade=l[4], id_usuario=l[1], id=l[0])
        return None

    # Função pra atualizar a falta
    def atualizar(self, falta):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE faltas SET materia=?, data=?, quantidade=? WHERE id=?
        """, (falta.materia, falta.data, falta.quantidade, falta.id))
        conn.commit()
        conn.close()

    # Função pra excluir a falta
    def excluir(self, id_falta):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM faltas WHERE id=?", (id_falta,))
        conn.commit()
        conn.close()
