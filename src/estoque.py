import sqlite3

class EstoqueDB:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()

        self.c.execute("""CREATE TABLE IF NOT EXISTS estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cod_barras INTEGER,
            quantidade INTEGER,
            secao TEXT
        )""")
        self.conn.commit()

    def insert(self, nome, cod_barras, quantidade, secao):
        self.c.execute("INSERT INTO estoque (nome, cod_barras, quantidade, secao) VALUES (?, ?, ?, ?)",
                       (nome, cod_barras, quantidade, secao))
        self.conn.commit()

    def fetch(self):
        self.c.execute("SELECT * FROM estoque")
        return self.c.fetchall()
