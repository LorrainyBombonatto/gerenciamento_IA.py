import sqlite3


def connect_db():
    """Conecta ao banco de dados SQLite."""
    conn = sqlite3.connect('gerenciamento_ia.db')
    return conn


def create_tables():
    """Cria as tabelas no banco de dados."""
    conn = connect_db()
    cursor = conn.cursor()
    # Criar tabela para armazenar custos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS custos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            material TEXT NOT NULL,
            mao_de_obra REAL NOT NULL,
            custo_entrega REAL NOT NULL,
            custo_total REAL NOT NULL
        )
    ''')

    # Criar tabela para armazenar margem de lucro
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS margem_lucro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            margem REAL NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
