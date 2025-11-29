from models.professor import Professor
from services.bancodedados import get_db_connection

class ProfessorService:
    
    # cadastra um novo professor
    def cadastrar(self, professor):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO professores (id_usuario, nome, email, materia, contato)
            VALUES (?, ?, ?, ?, ?)
        """, (professor.id_usuario, professor.nome, professor.email, professor.materia, professor.contato))
        conn.commit()
        conn.close()
        
    # busca o professor que um determinado aluno cadastrou
    def listar_aluno(self, id_usuario):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM professores WHERE id_usuario = ?", (id_usuario,))
        linhas = cursor.fetchall()
        conn.close()

        lista_profs = []
        for l in linhas:
            prof = Professor(
                nome=l[2], 
                email=l[3], 
                materia=l[4], 
                contato=l[5], 
                id_usuario=l[1], 
                id=l[0]
            )
            lista_profs.append(prof)
        return lista_profs
    
    # busca um professor por determinado id 
    def buscar_id(self, id_prof):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM professores WHERE id = ?", (id_prof,))
        l = cursor.fetchone()
        conn.close()
        
        if l:
            return Professor(nome=l[2], email=l[3], materia=l[4], contato=l[5], id_usuario=l[1], id=l[0])
        return None

    # atualiza as informações do professor
    def atualizar(self, professor):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE professores SET nome=?, email=?, materia=?, contato=? WHERE id=?
        """, (professor.nome, professor.email, professor.materia, professor.contato, professor.id))
        conn.commit()
        conn.close()
        
    # exclui um professor cadastrado   
    def excluir(self, id_prof):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM professores WHERE id=?", (id_prof,))
        conn.commit()
        conn.close()
       