f#importando sqlite
import sqlite3 as lite

#Criando conexão
con = lite.connect("estoque.db")

dados = []

#Inserir dados
with con:
    cur = con.cursor()
    query = "INSERT INTO estoque(nome, localizacao, descricao, quantidade, codigo_de_barras, imagem) VALUES(?,?,?,?,?,?)"
    cur.execute(query, dados)
