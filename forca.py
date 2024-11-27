import sqlite3
import os

def criaBanco():
    # Caminho para o diretório e o banco de dados no diretório do usuário
    diretorio = os.path.join(os.path.expanduser("~"), "JogoDaForca")
    caminho_banco = os.path.join(diretorio, 'forca.db')

    # Cria o diretório se ele não existir
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    # Conecta ao banco de dados no diretório especificado
    conn = sqlite3.connect(caminho_banco)
    cursor = conn.cursor()

    # Criação das tabelas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "temas" (
        id_temas INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "usuarios" (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_usuario TEXT NOT NULL UNIQUE,
        senha_usuario TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "palavras" (
        id_palavra INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_palavra TEXT NOT NULL UNIQUE,
        id_tema_fk INTEGER,
        FOREIGN KEY (id_tema_fk) REFERENCES temas (id_temas)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "palavras_resolvidas" (
        id_usuario_fk INTEGER,
        id_palavra_fk INTEGER,
        FOREIGN KEY (id_usuario_fk) REFERENCES usuarios (id_usuario),
        FOREIGN KEY (id_palavra_fk) REFERENCES palavras (id_palavra),
        PRIMARY KEY (id_usuario_fk, id_palavra_fk)
        )
    ''')

    # Inserts de temas
    temas = ['Animais', 'Frutas', 'Cores', 'Países', 'Objetos', 'Profissões', 'Tecnologia']
    for tema in temas:
        cursor.execute("INSERT OR IGNORE INTO temas (nome) VALUES (?)", (tema,))

    # Inserts de usuários
    usuarios = [
        ('usuario1', 'senha123'),
        ('usuario2', 'senha456'),
        ('usuario3', 'senha789'),
        ('usuario4', 'senha101'),
        ('usuario5', 'senha202')
    ]
    for nome, senha in usuarios:
        cursor.execute("INSERT OR IGNORE INTO usuarios (nome_usuario, senha_usuario) VALUES (?, ?)", (nome, senha))

    # Inserts de palavras para cada tema
    palavras = [
        ('Cachorro', 1), ('Gato', 1), ('Elefante', 1), ('Papagaio', 1), ('Leão', 1),
        ('Maçã', 2), ('Banana', 2), ('Laranja', 2), ('Abacaxi', 2), ('Uva', 2),
        ('Vermelho', 3), ('Azul', 3), ('Verde', 3), ('Amarelo', 3), ('Preto', 3),
        ('Brasil', 4), ('Argentina', 4), ('Espanha', 4), ('Japão', 4), ('França', 4),
        ('Mesa', 5), ('Cadeira', 5), ('Computador', 5), ('Lápis', 5), ('Celular', 5),
        ('Médico', 6), ('Professor', 6), ('Engenheiro', 6), ('Arquiteto', 6), ('Dentista', 6),
        ('Internet', 7), ('Computador', 7), ('Smartphone', 7), ('Inteligência Artificial', 7), ('Robô', 7)
    ]
    for nome_palavra, id_tema in palavras:
        cursor.execute("INSERT OR IGNORE INTO palavras (nome_palavra, id_tema_fk) VALUES (?, ?)", (nome_palavra, id_tema))

    # Inserts de palavras resolvidas
    palavras_resolvidas = [
        (1, 1), (1, 6), (1, 11), (2, 2), (2, 7), (2, 12),
        (3, 3), (3, 8), (3, 13), (4, 4), (4, 9), (4, 14),
        (5, 5), (5, 10), (5, 15)
    ]
    for id_usuario, id_palavra in palavras_resolvidas:
        cursor.execute("INSERT OR IGNORE INTO palavras_resolvidas (id_usuario_fk, id_palavra_fk) VALUES (?, ?)", (id_usuario, id_palavra))

    # Confirma as mudanças e fecha a conexão
    conn.commit()
    conn.close()

# Chame a função para criar o banco de dados e o diretório
criaBanco()
