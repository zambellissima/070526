from database.connection import get_connection

class CinemaRepository:

    def create_table(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cinemas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cidade TEXT,
            estado TEXT,
            endereco TEXT,
            capacidade INTEGER
        )
        """)

        connection.commit()
        connection.close()

    def insert(self, cinema):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO cinemas(nome, cidade, estado, endereco, capacidade)
        VALUES (?, ?, ?, ?, ?)
        """, (
            cinema.nome,
            cinema.cidade,
            cinema.estado,
            cinema.endereco,
            cinema.capacidade
        ))

        connection.commit()
        connection.close()
