from conexao import get_connection

def verificar_login(email, senha):
    """Verifica o login do usuário no banco de dados.

    Args:
        email (str): O email do usuário.
        senha (str): A senha do usuário.

    Returns:
        tuple: Uma tupla contendo o id_usuario e nome_usuario se o login for bem-sucedido.
        None: Se o email não existir ou a senha estiver incorreta.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Consulta para verificar o e-mail
    cursor.execute("SELECT id_usuario, nome_usuario, senha_usuario FROM usuarios WHERE nome_usuario = ?", (email,))
    usuario = cursor.fetchone()

    conn.close()

    # Verifica se o usuário foi encontrado e se a senha está correta
    if usuario and usuario[2] == senha:
        # Retorna id_usuario e nome_usuario se a autenticação for bem-sucedida
        return usuario
    else:
        # Retorna None se o e-mail não existir ou a senha estiver incorreta
        return ['Usuário ou senha Incorretos']
