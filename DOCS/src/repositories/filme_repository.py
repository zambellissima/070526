from database.connection import get_connection

class FilmeRepository:

    def create_table(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            genero TEXT,
            classificacao TEXT,
            duracao INTEGER,
            diretor TEXT
        )
        """)

        connection.commit()
        connection.close()

    def insert(self, filme):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO filmes(titulo, genero, classificacao, duracao, diretor)
        VALUES (?, ?, ?, ?, ?)
        """, (
            filme.titulo,
            filme.genero,
            filme.classificacao,
            filme.duracao,
            filme.diretor
        ))

        connection.commit()
        connection.close()
