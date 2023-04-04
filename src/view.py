#importando sqlite
import sqlite3 as lite


#Criando conexão
con = lite.connect("estoque.db")


#Inserir dados
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO estoque(nome, localizacao, descricao, quantidade, codigo_de_barras, imagem) VALUES(?,?,?,?,?,?)"
        cur.execute(query, i)


#Atualizar dados
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE estoque SET nome=?, localizacao=?, descricao=?, quantidade=?, codigo_de_barras=?, imagem=? WHERE id =?"
        cur.execute(query, id)


#Deletar dados
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM estoque WHERE id=?"
        cur.execute(query, i)


#Ver dados
def ver_form(i):
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM estoque"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados


#Ver dados individuais
def ver_item(id):
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM estoque WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)
