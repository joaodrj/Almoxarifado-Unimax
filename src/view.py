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


def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE estoque SET nome=?, localizacao=?, descricao=?, quantidade=?, codigo_de_barras=?, imagem=? WHERE id =?"
        cur.execute(query, (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))



#Deletar dados
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM estoque WHERE id=?"
        cur.execute(query, i)


#Ver dados do estoque
def ver_form():
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
            
        return ver_dados_individual
def buscar_dados(coluna, valor):
    buscar_dados = []
    with con:
        cur = con.cursor()
        query = f"SELECT * FROM estoque WHERE {coluna} LIKE ?"
        cur.execute(query, (f"%{valor}%",))

        rows = cur.fetchall()
        for row in rows:
            buscar_dados.append(row)
    return buscar_dados


#--------------------------FUNÇÕES PARA A TELA ALUNOS-------------------------------------------------------------
#Inserir dados dos alunos
def inserir_form_alunos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO alunos(Curso, RA, Nome, Semestre, Turma, Email) VALUES(?,?,?,?,?,?)"
        cur.execute(query, i)

#Atualiza dados sobre alunos existentes
def atualizar_form_alunos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE alunos SET Curso=?, RA=?, Nome=?, Semestre=?, Turma=?, Email=? WHERE id =?"
        cur.execute(query, (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))


#Deletar aluno
def deletar_form_alunos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM alunos WHERE id=?"
        cur.execute(query, i)


#Ver dados dos alunos
def ver_form_alunos():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM alunos"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados


#--------------------------FUNÇÕES PARA A TELA LABORATORIOS-------------------------------------------------------------
#Inserir dados dos alunos
def inserir_form_laboratorios(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO laboratorios(nome) VALUES(?)"
        cur.execute(query, i)

#Atualiza dados sobre alunos existentes
def atualizar_form_laboratorios(i):
    with con:
        cur = con.cursor()
        query = "UPDATE laboratorios SET nome=? WHERE id =?"
        cur.execute(query, (i[0], i[1]))


#Deletar aluno
def deletar_form_laboratorios(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM laboratorios WHERE id=?"
        cur.execute(query, i)


#Ver dados dos alunos
def ver_form_laboratorios():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM laboratorios"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados



#--------------------------FUNÇÕES PARA A TELA DE PROFESSORES-------------------------------------------------------------
#Inserir dados dos alunos
def inserir_form_professores(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO laboratorios(nome, email) VALUES(?, ?)"
        cur.execute(query, i)

#Atualiza dados sobre alunos existentes
def atualizar_form_professores(i):
    with con:
        cur = con.cursor()
        query = "UPDATE  SET nome=?, email=? WHERE id =?"
        cur.execute(query, (i[0], i[1], i[2]))


#Deletar aluno
def deletar_form_professores(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM professores WHERE id=?"
        cur.execute(query, i)


#Ver dados dos alunos
def ver_form_professores():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM professores"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados


#---------------------------FUNCOES PARA A TELA DE SAIDA-------------------------------------------------

# Função para buscar produto no banco de dados
def buscar_produto(codigo_barras):
    # Realize a conexão com o banco de dados
    conexao = lite.connect('estoque.db')

    # Crie um cursor para executar as consultas
    cursor = conexao.cursor()

    # Execute a consulta para buscar o produto pelo código de barras
    consulta = "SELECT nome, quantidade FROM estoque WHERE codigo_de_barras = ?"
    valores = (codigo_barras,)
    cursor.execute(consulta, valores)

    # Obtenha o resultado da consulta
    resultado = cursor.fetchone()

    # Feche o cursor e a conexão com o banco de dados
    cursor.close()
    conexao.close()

    # Verifique se o produto foi encontrado
    if resultado is not None:
        nome_produto, quantidade = resultado
        return (codigo_barras, nome_produto, quantidade)
    else:
        return None


# Função para buscar alunos no banco de dados
def buscar_alunos(RA):
    # Realize a conexão com o banco de dados
    conexao = lite.connect('estoque.db')

    # Crie um cursor para executar as consultas
    cursor = conexao.cursor()

    # Execute a consulta para buscar o aluno pelo ra
    consulta = "SELECT nome, RA, Semestre FROM alunos WHERE RA = ?"
    valores = (RA,)
    cursor.execute(consulta, valores)

    # Obtenha o resultado da consulta
    resultado = cursor.fetchone()

    # Feche o cursor e a conexão com o banco de dados
    cursor.close()
    conexao.close()

    # Verifique se o produto foi encontrado
    if resultado is not None:
        nome, ra, Semestre = resultado
        return (nome, ra, Semestre)
    else:
        return None
    

def inserir_emprestimo(alunos_lidos, produtos_lidos):
    
    for aluno in alunos_lidos:
                nome_aluno = aluno[0]
                ra_aluno = aluno[1]
                semestre_aluno =aluno[2]
    
    for produto in produtos_lidos:
                codigo_barras_produto = produto[0]
                quantidade = 1
                nome_produto = produto[1]
    # Realize a conexão com o banco de dados
    conexao = lite.connect('estoque.db')

    # Crie um cursor para executar as consultas
    cursor = conexao.cursor()

    # Insira os registros na tabela de empréstimos
    for aluno in alunos_lidos:
        nome_aluno = aluno[0]
        ra_aluno = aluno[1]
        semestre_aluno = aluno[2]

        for produto in produtos_lidos:
            codigo_barras_produto = produto[0]
            nome_produto = produto[1]

            # Execute a consulta para inserir o empréstimo
            consulta = '''INSERT INTO emprestimos (nome_aluno, ra, semestre, produto, quantidade, codigo_de_barras)
                          VALUES (?, ?, ?, ?, ?, ?)'''
            valores = (nome_aluno, ra_aluno, semestre_aluno, nome_produto, 1, codigo_barras_produto)
            cursor.execute(consulta, valores)

    # Salve as alterações no banco de dados
    conexao.commit()

    # Feche o cursor e a conexão com o banco de dados
    cursor.close()
    conexao.close()






