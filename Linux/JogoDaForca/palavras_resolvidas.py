from conexao import get_connection

def get_palavras_resolvidas(id_usuario):
    """Retorna todas as palavras que o usuário já resolveu, independentemente do tema.

    Args:
        id_usuario (int): O ID do usuário.

    Returns:
        list: Uma lista de tuplas contendo o ID da palavra, o nome da palavra, e o nome do tema.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Consulta para buscar todas as palavras que o usuário já resolveu, com o nome do tema
    query = """
    SELECT p.id_palavra, p.nome_palavra, t.nome
    FROM palavras p
    INNER JOIN palavras_resolvidas pr ON p.id_palavra = pr.id_palavra_fk
    INNER JOIN temas t ON p.id_tema_fk = t.id_temas
    WHERE pr.id_usuario_fk = ?
    """
    cursor.execute(query, (id_usuario,))
    palavras_resolvidas = cursor.fetchall()

    conn.close()
    return palavras_resolvidas
