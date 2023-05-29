import sqlite3 as lite

# Criando conexão
con = lite.connect('estoque.db')



'''# Criando tabela de estoque
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS estoque(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, localizacao TEXT, descricao TEXT, quantidade DECIMAL , codigo_de_barras TEXT, imagem TEXT)")'''

'''#Deletando tabela antiga
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE estoque")'''
    



'''# Criando tabela alunos
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS alunos(id INTEGER PRIMARY KEY AUTOINCREMENT, Curso TEXT, RA TEXT, Nome TEXT, Semestre TEXT, Turma TEXT, Email TEXT )")'''


'''# Criando nova tabela alunos com id como chave primária
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS alunos_new(id INTEGER PRIMARY KEY AUTOINCREMENT, Curso TEXT, RA TEXT, nome TEXT, Semestre TEXT, Turma TEXT, Email TEXT )")

# Transferindo dados da tabela antiga para a nova tabela
with con:
    cur = con.cursor()
    cur.execute("INSERT INTO alunos_new (Curso, RA, nome, Semestre, Turma, Email) SELECT Curso, RA, nome, Semestre, Turma, Email FROM alunos")

#Deletando tabela antiga
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE alunos")

# Renomeando nova tabela para o nome da tabela antiga
with con:
    cur = con.cursor()
    cur.execute("ALTER TABLE alunos_new RENAME TO alunos")'''






'''# Criando tabela LABORATORIOS
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS laboratorios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")'''









'''# Criando tabela professores
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS professores(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT )")


# Criando nova tabela professores com id como chave primária
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS professores_new(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT )")

# Transferindo dados da tabela antiga para a nova tabela
with con:
    cur = con.cursor()
    cur.execute("INSERT INTO professores_new (nome, email) SELECT nome, email FROM professores")

# Deletando tabela antiga
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE professores")

# Renomeando nova tabela para o nome da tabela antiga
with con:
    cur = con.cursor()
    cur.execute("ALTER TABLE professores_new RENAME TO professores")'''



'''# Criar nova tabela sem as colunas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS novo_estoque(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, localizacao TEXT, descricao TEXT, quantidade DECIMAL , codigo_de_barras TEXT, imagem TEXT)")'''

'''# Transferindo dados da tabela antiga para a nova tabela
with con:
    cur = con.cursor()
    cur.execute("INSERT INTO novo_estoque (nome, localizacao, descricao, quantidade, codigo_de_barras, imagem) SELECT nome, localizacao, descricao, quantidade, codigo_de_barras, imagem FROM estoque")


# Excluir tabela antiga
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS estoque")

# Renomear nova tabela para o nome original
with con:
    cur = con.cursor()
    cur.execute("ALTER TABLE novo_estoque RENAME TO estoque")'''


#Criando tabela de estoque
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS emprestimos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome_aluno TEXT, ra TEXT, semestre TEXT, produto TEXT, quantidade DECIMAL , codigo_de_barras TEXT)")