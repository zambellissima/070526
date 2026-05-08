from database.connection import get_connection

class SessaoRepository:

    def create_table(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            horario TEXT,
            publico INTEGER,
            cinema_id INTEGER,
            filme_id INTEGER
        )
        """)

        connection.commit()
        connection.close()

    def insert(self, sessao):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO sessoes(data, horario, publico, cinema_id, filme_id)
        VALUES (?, ?, ?, ?, ?)
        """, (
            sessao.data,
            sessao.horario,
            sessao.publico,
            sessao.cinema_id,
            sessao.filme_id
        ))

        connection.commit()
        connection.close()
