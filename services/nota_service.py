from models.nota import Nota
from services.bancodedados import get_db_connection


class NotaService:
    def cadastrar(self, nota):

        # Verificar se a nota está entre 0 e 10
        if nota.valor < 0 or nota.valor > 10:
            print("Erro: A nota deve estar entre 0 e 10")
            return

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO notas (id_usuario, materia, nome_prova, valor)
            VALUES (?,?,?,?)
        """, (nota.id_usuario, nota.materia, nota.nome_prova, nota.valor))
        conn.commit()
        conn.close()

    # Função pra listar as notas do aluno específico
    def listar_por_aluno(self, id_usuario):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM notas WHERE id_usuario = ?", (id_usuario,))
        linhas = cursor.fetchall()
        conn.close()

        lista_notas = []
        for l in linhas:
            nota = Nota(materia=l[2], nome_prova=l[3],
                        valor=l[4], id_usuario=l[1], id=l[0])
            lista_notas.append(nota)

        return lista_notas

    # Função pra buscar uma nota específica
    def buscar_por_id(self, id_nota):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notas WHERE id = ?", (id_nota,))
        l = cursor.fetchone()
        conn.close()

        if l:
            return Nota(materia=l[2], nome_prova=l[3], valor=l[4], id_usuario=l[1], id=l[0])
        return None

    # Função pra editar a nota
    def atualizar(self, nota):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE notas SET materia=?, nome_prova=?, valor=? WHERE id=?
        """, (nota.materia, nota.nome_prova, nota.valor, nota.id))
        conn.commit()
        conn.close()

    # Função pra deletar a nota
    def excluir(self, id_nota):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notas WHERE id=?", (id_nota,))
        conn.commit()
        conn.close()
