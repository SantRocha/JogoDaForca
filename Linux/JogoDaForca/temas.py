from conexao import get_connection

def ver_todos_temas():
    """Retorna todos os temas da tabela temas."""
    conn = get_connection()
    cursor = conn.cursor()

    # Consulta para selecionar todos os temas
    cursor.execute("SELECT * FROM temas")
    temas = cursor.fetchall()

    conn.close()
    return temas
