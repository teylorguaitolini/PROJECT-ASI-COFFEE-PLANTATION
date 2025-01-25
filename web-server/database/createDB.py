import sqlite3
from os import path
from sys import path as sys_path

def createDB():
    """
    # createDB
    Cria o banco de dados e as tabelas necessárias para o projeto.
    """
    DIR = path.join(sys_path[0], "database")
    DB_PATH = path.join(DIR, "sensors.db")
    SQL_PATH = path.join(DIR, "create_tables.sql")
    
    # Verifica se o arquivo do banco já existe
    if path.exists(DB_PATH):
        print("O arquivo do banco de dados já existe.")
        return DB_PATH

    try:
        # Conecta ao arquivo do banco (cria se não existir)
        conn = sqlite3.connect(DB_PATH)
        # Ativa chaves estrangeiras se quiser garantir no lado Python
        conn.execute("PRAGMA foreign_keys = ON;")

        # Lê o arquivo SQL
        with open(SQL_PATH, 'r', encoding='utf-8') as f:
            sql_script = f.read()

        # Executa o script SQL
        conn.executescript(sql_script)

        print("Banco de dados criado e tabelas definidas com sucesso.")

        return DB_PATH

    except sqlite3.Error as e:
        print(f"Erro ao criar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()
