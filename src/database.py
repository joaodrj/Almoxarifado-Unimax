import sqlite3 as lite

#Criando conexão
con = lite.connect('estoque.db')

#Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE estoque(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEX, localizacao TEXT, descricao TEXT, quantidade DECIMAL , codigo_de_barras TEXT, imagem TEXT)")

    
