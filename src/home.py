import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog as fd
#Importando view
from view import *
import pandas as pd
import sqlite3 as lite
import keyboard
from tkinter import messagebox

#----------------------cria a classe Home para a tela principal--------------------------------------
class Home:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1366x768")
        self.master.configure(bg = "#FFFFFF")
        self.master.title('Tela inicial')
        self.canvas = Canvas(
            master,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0) 

        self.background_img = tk.PhotoImage(file = f"img/tela_inicial/backgroundAtualizado.png")
        self.background = self.canvas.create_image(
        683.0, 383.5,
        image=self.background_img)

        #BOTÃO ESTOQUE
        self.img0 = tk.PhotoImage(file = f"img/tela_inicial/img0.png")
        self.b0 = tk.Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            command=self.open_estoque_window)
        #Botão estoque
        self.b0.place(
            x = 0, y = 114.69,
            width = 320,
            height = 117)
        
        self.canvas.create_window(0, 114.69, anchor=NW, window=self.b0)



        #Botão ALUNOS
        self.img3 = tk.PhotoImage(file = f"img/tela_inicial/alunos.png")
        self.b3 = Button(
            image = self.img3,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            command=self.open_aluno_window)

        self.b3.place(
            x = 0, y = 357,
            width = 320,
            height = 117)

        self.canvas.create_window(0, 357, anchor=NW, window=self.b3)


        #Botao EMPRESTIMOS
        self.img4 = PhotoImage(file = f"img/tela_inicial/img4.png")
        self.b4 = Button(
            image = self.img4,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            command= self.open_emprestimos_window)

        self.b4.place(
            x = 0, y = 236,
            width = 320,
            height = 117)
        self.canvas.create_window(0, 236, anchor=NW, window=self.b4)


        #Botão PROFESSORES
        self.img1 = tk.PhotoImage(file = f"img/tela_inicial/img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            command=self.open_professores_window)

        self.b1.place(
            x = 0, y = 478,
            width = 320,
            height = 117)

        self.canvas.create_window(0, 478, anchor=NW, window=self.b1)


        #Botão Saida
        self.img6 = tk.PhotoImage(file = f"img/tela_inicial/img6.png")
        self.b6 = Button(
            image = self.img6,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            command= self.open_saida_window)

        self.b6.place(
            x = 684, y = 298,
            width = 319,
            height = 207)
        self.canvas.create_window(684, 298, anchor=NW, window=self.b6)


        #Botão LABORATORIOS 
        self.img2 = tk.PhotoImage(file = f"img/tela_inicial/laboratorio.png")
        self.b2 = Button(
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            command= self.open_laboratorios_window)

        self.b2.place(
            x = 0, y = 599,
            width = 320,
            height = 117)

        self.canvas.create_window(0, 599, anchor=NW, window=self.b2)


        #chama a tela principal
        self.master.mainloop()


    #Função para abrir a tela de estoque
    def open_estoque_window(self):
        # Cria a janela de estoque
        self.estoque_window = Toplevel(self.master)
        estoque = Estoque(self.estoque_window)

    #Função para abrir a tela dos alunos
    def open_aluno_window(self):
        # Cria a janela de alunos
        self.aluno_window = Toplevel(self.master)
        aluno = Alunos(self.aluno_window)
    
    #Função para abrir a tela de saida
    def open_saida_window(self):
        self.saida_window = Toplevel(self.master)
        saida = Saida(self.saida_window)

     #Função para abrir a tela de professores
    def open_professores_window(self):
        self.professores_window = Toplevel(self.master)
        professores = Professores(self.professores_window)

    #Função para abrir a tela de emprestimos
    def open_emprestimos_window(self):
        self.emprestimos_window = Toplevel(self.master)
        emprestimos = Emprestimos(self.emprestimos_window)

    #Função para abrir a tela de laboratorios
    def open_laboratorios_window(self):
        self.laboratorios_window = Toplevel(self.master)
        laboratorios = Laboratorios(self.laboratorios_window)



class Estoque:
    
    def __init__(self, master):
        self.master = master
        self.master.geometry("1366x768")
        self.master.configure(bg="#000000")

        # cria um frame na parte superior da janela
        frame_topo = tk.Frame(self.master, bg="#2B2F4D", height=66)
        frame_topo.grid(row=0, column=0, sticky='we') 

        '''#adiciona um label ao topo do frame
        label_topo = tk.Label(frame_topo, text="Estoque", font=("Arial", 18), fg="#000000", bg="#2B2F4D")
        label_topo.pack(side="left", padx=10, pady=10)'''

        # cria um frame para o meio onde serão prenchidas as informações
        frame_meio = tk.Frame(self.master, bg="#D9D9D9", height=350)
        frame_meio.grid(row=1, column=0, padx=0, pady=1, sticky='we')

        # cria um frame na parte inferior onde sera mostrado o estoque
        frame_baixo = tk.Frame(self.master, bg="white", height=350)
        frame_baixo.grid(row=2, column=0, padx=0, pady=1, sticky='we')

        # cria um novo canvas para os widgets
        self.canvas = tk.Canvas(self.master, bg="#FFFFFF", height=768, width=1366, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.grid(row=3, column=0, sticky='nsew')


        '''#botao para carregar a planilha do excel
        b_carregar = tk.Button(frame_meio, width=29, text='Carregar planilha', compound=tk.CENTER, anchor=tk.CENTER, overrelief=tk.RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000', command=self.carregar_arquivo)
        b_carregar.place(x=130, y=161)
        
        def carregar_arquivo(self):
        # abre o explorador de arquivos e permite que o usuário selecione o arquivo desejado
        filename = fd.askopenfilename()

        # verifica se o usuário selecionou um arquivo
        if filename:
            # carrega o arquivo selecionado em um DataFrame do Pandas
            df = pd.read_excel(filename)

            # conecta-se ao banco de dados
            conn = lite.connect('estoque.db')

            # insere as informações dos alunos no banco de dados
            df.to_sql('estoque', conn, if_exists='replace', index=False)

            # fecha a conexão com o banco de dados
            conn.close()'''

        #-----------------------------------CRIANDO FUNÇOES PARA A TELA ESTOQUE-------------------------------------------------

        global tree

        #Função inserir
        def inserir ():
            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            localizacao = e_localizacao.get()
            descricacao = e_descricao.get()
            quantidade = e_quantidade.get()
            codigo_de_barras = e_codigo_de_barras.get()
            imagem = imagem_string

            lista_inserir = [nome, localizacao, descricacao, quantidade, codigo_de_barras, imagem]

            for i in lista_inserir:
                if i == '':
                    tk.messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
                
            inserir_form(lista_inserir)

            tk.messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

            e_nome.delete(0,'end')
            e_localizacao.delete(0,'end')
            e_descricao.delete(0,'end')
            e_quantidade.delete(0,'end')
            e_codigo_de_barras.delete(0,'end')


            mostrar( )

 
        #Função atualizar
        def atualizar():
            global imagem, imagem_string, l_imagem
            try:
                treev_dados = tree.focus()
                treev_dicionario = tree.item(treev_dados)
                treev_lista = treev_dicionario['values']
                
                valor = treev_lista[0]

                e_nome.delete(0,'end')
                e_localizacao.delete(0,'end')
                e_descricao.delete(0,'end')
                e_quantidade.delete(0,'end')
                e_codigo_de_barras.delete(0,'end')

                id = int(treev_lista[0])
                e_nome.insert(0, treev_lista[1])
                e_localizacao.insert(0, treev_lista[2])
                e_descricao.insert(0, treev_lista[3])
                e_quantidade.insert(0, treev_lista[4])
                e_codigo_de_barras.insert(0, treev_lista[5])
                imagem_string = treev_lista[6]


                def update():
                    global imagem, imagem_string, l_imagem

                    nome = e_nome.get()
                    localizacao = e_localizacao.get()
                    descricao = e_descricao.get()
                    quantidade = e_quantidade.get()
                    codigo_de_barras = e_codigo_de_barras.get()
                    imagem = imagem_string

                    if imagem == '':
                        imagem == e_codigo_de_barras.insert(0, treev_lista[5])

                    lista_atualizar = [nome, localizacao, descricao, quantidade, codigo_de_barras, imagem, id]

                    for i in lista_atualizar:
                        if i=='':
                            tk.messagebox.showerror('Erro', 'Preencha todos os campos')
                            return
                        
                    atualizar_form(lista_atualizar)
                    
                    tk.messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')
                    e_nome.delete(0,'end')
                    e_localizacao.delete(0,'end')
                    e_descricao.delete(0,'end')
                    e_quantidade.delete(0,'end')
                    e_codigo_de_barras.delete(0,'end')
            
                    b_confirmar.destroy()
                    mostrar()

                #Botão confirmar
                b_confirmar = Button(frame_meio, command=update, width=19, text= 'Confirmar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold'), bg='#3CB371', fg='#000000')
                b_confirmar.place(x=330, y=191)


            except IndexError:
                tk.messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

        #Função Deletar
        def deletar():
            try:
                treev_dados = tree.focus()
                treev_dicionario = tree.item(treev_dados)
                treev_lista = treev_dicionario['values']
                valor = treev_lista[0]

                deletar_form([valor])
                

                tk.messagebox.showinfo('Sucesso', 'Os dados foram Deletados com sucesso!')
                mostrar()

            except IndexError:
                tk.messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')
    

        #Função para escolher imagem
        global imagem, imagem_string, l_imagem

        def escolher_imagem():
            global imagem, imagem_string, l_imagem

            imagem = fd.askopenfilename()
            imagem_string = imagem


            # Abrindo imagem dos produtos do estoque
            imagem = Image.open(imagem)
            imagem = imagem.resize((170,170))
            imagem = ImageTk.PhotoImage(imagem)

            # Adiciona imagem dos produtos no frame
            l_imagem = Label(frame_meio, image=imagem, bg='#2B2F4D', fg='#FFFFFF')
            l_imagem.image = l_imagem
            l_imagem.place(x=1000, y=20)

                
        #Função para ver imagem
        def ver_imagem():
            global imagem, imagem_string, l_imagem

            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario['values']
            
            valor = [int(treev_lista[0])]

            iten = ver_item(valor)
            imagem = iten[0][6]

            imagem = Image.open(imagem)
            imagem = imagem.resize((170,170))
            imagem = ImageTk.PhotoImage(imagem)

            l_imagem = Label(frame_meio, image=imagem, bg='#2B2F4D', fg='#FFFFFF')
            l_imagem.image = l_imagem
            l_imagem.place(x=1000, y=20)



        #Trbalhando no frame de cima
        # Abrindo imagem do ícone da tela estoque
        self.img_tela_estoque = Image.open('img/icones/inventario.png')
        self.img_tela_estoque = self.img_tela_estoque.resize((45,45))
        self.img_tela_estoque = ImageTk.PhotoImage(self.img_tela_estoque)

        # Adiciona o ícone da tela no topo do frame
        self.img_logo_estoque = Label(frame_topo, image=self.img_tela_estoque, text='   Estoque', width=1366, compound=LEFT, anchor=NW, font=('Verdana 35 bold'), bg='#2B2F4D', fg='#FFFFFF')
        self.img_logo_estoque.image = self.img_tela_estoque
        self.img_logo_estoque.pack(side=LEFT, padx=15, pady=10)

        #Criando entradas 
        #Label e entrada para o nome
        l_nome = Label(frame_meio, text= 'Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_nome.place(x=10, y=10)
        e_nome = Entry(frame_meio, width=30, justify='left', relief=SOLID)
        e_nome.place(x=130, y=11)

        #Label e entrada para a localização
        l_localizacao = Label(frame_meio, text= 'Localização', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_localizacao.place(x=10, y=40)
        e_localizacao = Entry(frame_meio, width=30, justify='left', relief=SOLID)
        e_localizacao.place(x=130, y=41)

        #Label e entrada para a descrição
        l_descricao = Label(frame_meio, text= 'Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_descricao.place(x=10, y=70)
        e_descricao = Entry(frame_meio, width=30, justify='left', relief=SOLID)
        e_descricao.place(x=130, y=71)

        #Label e entrada para a quantidade
        l_quantidade = Label(frame_meio, text= 'Quantidade', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_quantidade.place(x=10, y=100)
        e_quantidade = Entry(frame_meio, width=30, justify='left', relief=SOLID)
        e_quantidade.place(x=130, y=101)

        #Label e entrada para o codigo de barras
        l_codigo_barras = Label(frame_meio, text= 'Codigo de Barras', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_codigo_barras.place(x=10, y=130)
        e_codigo_de_barras = Entry(frame_meio, width=30, justify='left', relief=SOLID)
        e_codigo_de_barras.place(x=130, y=131)


        #Criando botões---------------------------------------------------------------------------------------------------------

        #Label e entrada para imagem do botão carregar
        l_imagem = Label(frame_meio, text= 'Imagem do item', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_imagem.place(x=10, y=160)

        #botao para carregar a imagem
        b_carregar = Button(frame_meio, command=escolher_imagem,     width=29, text= 'carregar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_carregar.place(x=130, y=161)

    

        #Botão inserir
        b_inserir = Button(frame_meio, command=inserir,  width=20, text= 'Adicionar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_inserir.place(x=330, y=10)

        #Botão update
        b_update = Button(frame_meio,command=atualizar, width=20, text= 'Atualizar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_update.place(x=330, y=50)

        #Botão delete
        b_delete = Button(frame_meio, command=deletar, width=20, text= 'Delete'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_delete.place(x=330, y=90)

        #Botão ver imagem
        b_item = Button(frame_meio, command=ver_imagem, width=20, text= 'Ver item'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_item.place(x=330, y=161)



        #CRIANDO A TABELA PARA MOSTRAR O ESTOQUE ----------------------------------------------------------------


        def mostrar():

            global tree

            # creating a treeview with dual scrollbars
            tabela_head = ['#Item', 'Nome',  'localizacao','Descrição', 'quantidade', 'codigo_de_barras']
            lista_itens = ver_form()
            global tree

            tree = ttk.Treeview(frame_baixo, selectmode="extended",columns=tabela_head, show="headings")

            # vertical scrollbar
            vsb = ttk.Scrollbar(frame_baixo, orient=VERTICAL, command=tree.yview)

            # horizontal scrollbar
            hsb = ttk.Scrollbar(frame_baixo, orient=HORIZONTAL, command=tree.xview)

            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            tree.grid(column=0, row=0, sticky='nsew')
            vsb.grid(column=1, row=0, sticky='ns')
            hsb.grid(column=0, row=1, sticky='ew')

            # define o peso da linha e coluna do frame como 1
            frame_baixo.grid_rowconfigure(0, weight=1)
            frame_baixo.grid_columnconfigure(0, weight=1)

            hd=["center","center","center","center","center","center"]
            h=[10,150,10,400,10,100]
            n=0

            # define o tamanho da fonte do cabeçalho da tabela
            style = ttk.Style()
            style.configure("Treeview.Heading", font=('Helvetica', 14))

            for col in tabela_head:
                tree.heading(col, text=col.title(), anchor=tk.CENTER)

                # adjust the column's width to the header string
                tree.column(col, width=h[n],anchor=hd[n])

                n+=1

            for item in lista_itens:
                tree.insert('', 'end', values=item)


        mostrar()



#-----------------------CLASSE PARA A TELA DE ALUNOS------------------------------------

class Alunos:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1366x768")
        self.master.configure(bg="#000000")

        # cria um frame na parte superior da janela
        frame_topo_alunos = tk.Frame(self.master, bg="#2B2F4D", height=66)
        frame_topo_alunos.grid(row=0, column=0, sticky='we') 

        # cria um frame para o meio onde serão prenchidas as informações
        frame_meio_alunos = tk.Frame(self.master, bg="#D9D9D9", height=350)
        frame_meio_alunos.grid(row=1, column=0, padx=0, pady=1, sticky='we')

        # cria um frame na parte inferior onde sera mostrado o estoque
        frame_baixo_alunos = tk.Frame(self.master, bg="white", height=350)
        frame_baixo_alunos.grid(row=2, column=0, padx=0, pady=1, sticky='we')

        # cria um novo canvas para os widgets
        self.canvas = tk.Canvas(self.master, bg="#FFFFFF", height=768, width=1366, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.grid(row=3, column=0, sticky='nsew')

        '''#botao para carregar a planilha do excel
        b_carregar = tk.Button(frame_meio_alunos, width=29, text='Carregar planilha', compound=tk.CENTER, anchor=tk.CENTER, overrelief=tk.RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000', command=self.carregar_arquivo)
        b_carregar.place(x=130, y=161)
        
        def carregar_arquivo(self):
        # abre o explorador de arquivos e permite que o usuário selecione o arquivo desejado
        filename = fd.askopenfilename()

        # verifica se o usuário selecionou um arquivo
        if filename:
            # carrega o arquivo selecionado em um DataFrame do Pandas
            df = pd.read_excel(filename)

            # conecta-se ao banco de dados
            conn = lite.connect('estoque.db')

            # insere as informações dos alunos no banco de dados
            df.to_sql('alunos', conn, if_exists='replace', index=False)

            # fecha a conexão com o banco de dados
            conn.close()'''

    


        #-------------------------------------CRIANDO FUNÇOES PARA A TELA ALUNOS----------------------------------------------

        global tree

        #Função inserir
        def inserir ():
            
            Curso = e_Curso.get()
            RA = e_RA.get()
            Nome = e_Nome.get()
            Semestre = e_Semestre.get()
            Turma = e_Turma.get()
            Email = e_Email.get()

            lista_inserir = [Curso, RA, Nome, Semestre, Turma, Email]

            for i in lista_inserir:
                if i == '':
                    tk.messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
                
            inserir_form_alunos(lista_inserir)

            tk.messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

            e_Curso.delete(0,'end')
            e_RA.delete(0,'end')
            e_Nome.delete(0,'end')
            e_Semestre.delete(0,'end')
            e_Turma.delete(0,'end')
            e_Email.delete(0,'end')


            mostrar( )

 
        #Função atualizar
        def atualizar():
            
            try:
                treev_dados = tree.focus()
                treev_dicionario = tree.item(treev_dados)
                treev_lista = treev_dicionario['values']
                
                valor = treev_lista[0]

                e_Curso.delete(0,'end')
                e_RA.delete(0,'end')
                e_Nome.delete(0,'end')
                e_Semestre.delete(0,'end')
                e_Turma.delete(0,'end')
                e_Email.delete(0,'end')

                id = int(treev_lista[0])
                e_Curso.insert(0, treev_lista[1])
                e_RA.insert(0, treev_lista[2])
                e_Nome.insert(0, treev_lista[3])
                e_Semestre.insert(0, treev_lista[4])
                e_Turma.insert(0, treev_lista[5])
                e_Email.insert(0, treev_lista[6])


                def update():
                    
                    Curso = e_Curso.get()
                    RA = e_RA.get()
                    Nome = e_Nome.get()
                    Semestre = e_Semestre.get()
                    Turma = e_Turma.get()
                    Email = e_Email.get()


                    lista_atualizar = [Curso, RA, Nome, Semestre, Turma, Email, id]

                    for i in lista_atualizar:
                        if i=='':
                            tk.messagebox.showerror('Erro', 'Preencha todos os campos')
                            return
                        
                    atualizar_form_alunos(lista_atualizar)
                    
                    tk.messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')
                    e_Curso.delete(0,'end')
                    e_RA.delete(0,'end')
                    e_Nome.delete(0,'end')
                    e_Semestre.delete(0,'end')
                    e_Turma.delete(0,'end')
                    e_Email.delete(0, 'end')
            
                    b_confirmar.destroy()
                    mostrar()

                #Botão confirmar
                b_confirmar = Button(frame_meio_alunos, command=update, width=19, text= 'Confirmar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold'), bg='#3CB371', fg='#000000')
                b_confirmar.place(x=330, y=191)


            except IndexError:
                tk.messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

        #Função Deletar
        def deletar():
            try:
                treev_dados = tree.focus()
                treev_dicionario = tree.item(treev_dados)
                treev_lista = treev_dicionario['values']
                valor = treev_lista[0]

                deletar_form_alunos([valor])
                

                tk.messagebox.showinfo('Sucesso', 'Os dados foram Deletados com sucesso!')
                mostrar()

            except IndexError:
                tk.messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')
    



        #Trbalhando no frame de cima
        # Abrindo imagem do ícone da tela alunos
        self.img_tela_alunos = Image.open('img/icones/aluno.png')
        self.img_tela_alunos = self.img_tela_alunos.resize((60,60))
        self.img_tela_alunos = ImageTk.PhotoImage(self.img_tela_alunos)

        # Adiciona o ícone da tela no topo do frame
        self.img_logo_alunos = Label(frame_topo_alunos, image=self.img_tela_alunos, text='   Alunos', width=1366, compound=LEFT, anchor=NW, font=('Verdana 35 bold'), bg='#2B2F4D', fg='#FFFFFF')
        self.img_logo_alunos.image = self.img_tela_alunos
        self.img_logo_alunos.pack(side=LEFT, padx=15, pady=10)

        #Criando entradas 
        #Label e entrada para o nome
        l_Curso = Label(frame_meio_alunos, text= 'Curso', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_Curso.place(x=10, y=10)
        e_Curso = Entry(frame_meio_alunos, width=30, justify='left', relief=SOLID)
        e_Curso.place(x=130, y=11)

        #Label e entrada para a localização
        l_RA = Label(frame_meio_alunos, text= 'RA', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_RA.place(x=10, y=40)
        e_RA = Entry(frame_meio_alunos, width=30, justify='left', relief=SOLID)
        e_RA.place(x=130, y=41)

        #Label e entrada para a descrição
        l_Nome = Label(frame_meio_alunos, text= 'Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_Nome.place(x=10, y=70)
        e_Nome = Entry(frame_meio_alunos, width=30, justify='left', relief=SOLID)
        e_Nome.place(x=130, y=71)

        #Label e entrada para a quantidade
        l_Semestre = Label(frame_meio_alunos, text= 'Semestre', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_Semestre.place(x=10, y=100)
        e_Semestre = Entry(frame_meio_alunos, width=30, justify='left', relief=SOLID)
        e_Semestre.place(x=130, y=101)

        #Label e entrada para o codigo de barras
        l_Turma = Label(frame_meio_alunos, text= 'Turma', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_Turma.place(x=10, y=130)
        e_Turma = Entry(frame_meio_alunos, width=30, justify='left', relief=SOLID)
        e_Turma.place(x=130, y=131)


        #Label e entrada para imagem do botão carregar
        l_Email = Label(frame_meio_alunos, text= 'Email', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_Email.place(x=10, y=160)

        e_Email = Entry(frame_meio_alunos, width=30, justify='left', relief=SOLID)
        e_Email.place(x=130, y=161)

        #---------------------------------------CRIANDO BOTÕES-----------------------------------------------------

        #Botão inserir
        b_inserir = Button(frame_meio_alunos, command=inserir,  width=20, text= 'Adicionar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_inserir.place(x=330, y=10)

        #Botão update
        b_update = Button(frame_meio_alunos,command=atualizar, width=20, text= 'Atualizar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_update.place(x=330, y=50)

        #Botão delete
        b_delete = Button(frame_meio_alunos, command=deletar, width=20, text= 'Delete'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_delete.place(x=330, y=90)



        #CRIANDO A TABELA PARA MOSTRAR O ESTOQUE ----------------------------------------------------------------


        def mostrar():

            global tree

            # creating a treeview with dual scrollbars
            tabela_head = ['#Item', 'Curso',  'RA','Nome', 'Semestre', 'Turma', 'Email']
            lista_itens = ver_form_alunos()
            global tree

            tree = ttk.Treeview(frame_baixo_alunos, selectmode="extended",columns=tabela_head, show="headings")

            # vertical scrollbar
            vsb = ttk.Scrollbar(frame_baixo_alunos, orient=VERTICAL, command=tree.yview)

            # horizontal scrollbar
            hsb = ttk.Scrollbar(frame_baixo_alunos, orient=HORIZONTAL, command=tree.xview)

            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            tree.grid(column=0, row=0, sticky='nsew')
            vsb.grid(column=1, row=0, sticky='ns')
            hsb.grid(column=0, row=1, sticky='ew')

            # define o peso da linha e coluna do frame como 1
            frame_baixo_alunos.grid_rowconfigure(0, weight=1)
            frame_baixo_alunos.grid_columnconfigure(0, weight=1)

            hd=["center","center","center","center","center","center", "center"]
            h=[20,40,40,120,40,100, 150]
            n=0

            # define o tamanho da fonte do cabeçalho da tabela
            style = ttk.Style()
            style.configure("Treeview.Heading", font=('Helvetica', 14))

            for col in tabela_head:
                tree.heading(col, text=col.title(), anchor=tk.CENTER)

                # adjust the column's width to the header string
                tree.column(col, width=h[n],anchor=hd[n])

                n+=1

            for item in lista_itens:
                tree.insert('', 'end', values=item)


        mostrar()



#-----------------------------CLASSE PARA A TELA DE SAIDA------------------------------

from tkinter import Text

class Saida:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1366x768")
        self.master.configure(bg="#000000")

        frame_topo_saida = tk.Frame(self.master, bg="#2B2F4D", height=66)
        frame_topo_saida.grid(row=0, column=0, sticky='we') 

        frame_meio_saida = tk.Frame(self.master, bg="#D9D9D9", height=350)
        frame_meio_saida.grid(row=1, column=0, padx=0, pady=1, sticky='we')

        frame_baixo_saida = tk.Frame(self.master, bg="white", height=350)
        frame_baixo_saida.grid(row=2, column=0, padx=0, pady=1, sticky='we')

        self.canvas = tk.Canvas(self.master, bg="#FFFFFF", height=768, width=1366, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.grid(row=3, column=0, sticky='nsew')

        self.img_tela_alunos = Image.open('img/icones/saida.png.png')
        self.img_tela_alunos = self.img_tela_alunos.resize((60,60))
        self.img_tela_alunos = ImageTk.PhotoImage(self.img_tela_alunos)

        self.img_logo_alunos = Label(frame_topo_saida, image=self.img_tela_alunos, text='   Saida de Materiais', width=1366, compound=LEFT, anchor=NW, font=('Verdana 35 bold'), bg='#2B2F4D', fg='#FFFFFF')
        self.img_logo_alunos.image = self.img_tela_alunos
        self.img_logo_alunos.pack(side=LEFT, padx=15, pady=10)

        l_codigo_barras_saida = Label(frame_meio_saida, text= 'Codigo de Barras', height=1, anchor=NW, font=('Ivy 15 bold'), bg='#D9D9D9', fg='#000000')
        l_codigo_barras_saida.place(x=10, y=10)
        e_codigo_barras_saida = Entry(frame_meio_saida, width=30, justify='left', relief=SOLID)
        e_codigo_barras_saida.place(x=200, y=14)

        l_alunos_saida = Label(frame_meio_saida, text= 'RA', height=1, anchor=NW, font=('Ivy 15 bold'), bg='#D9D9D9', fg='#000000')
        l_alunos_saida.place(x=10, y=30)
        e_alunos_saida = Entry(frame_meio_saida, width=30, justify='left', relief=SOLID)
        e_alunos_saida.place(x=200, y=34)

        t_produtos_lidos = Text(frame_meio_saida, width=42, height=4, font=('Ivy 12'))
        t_produtos_lidos.place(x=400, y=10)

        t_alunos_lidos = Text(frame_meio_saida, width=42, height=4, font=('Ivy 12'))
        t_alunos_lidos.place(x=400, y=150)


        self.produtos_lidos = []  # lista para armazenar os produtos lidos
        
        self.alunos_lidos = []
        
        
        #----------------funcao para a caixa de produtos--------------------------------
        def atualizar_caixa_texto(produtos_lidos):
            t_produtos_lidos.delete("1.0", END)  # Limpa o conteúdo da caixa de texto
        
            produtos_texto = ""
            for produto in produtos_lidos:
                codigo_barras = produto[0]
                quantidade = 1
                nome_produto = produto[1]#buscar_produto(codigo_barras)
                if nome_produto is not None:
                    produtos_texto += f'Código de Barras: {codigo_barras}, Quantidade: {quantidade}, Nome do Produto: {nome_produto}\n'
                else:
                    produtos_texto += f'Código de Barras: {codigo_barras}, Quantidade: {quantidade}, Produto não encontrado\n'
        
            t_produtos_lidos.insert("1.0", produtos_texto)  # Insere o texto na caixa de texto

        def ler_codigo_barras(event):
            codigo_barras = e_codigo_barras_saida.get()

            resultado_busca = self.buscar_produto(codigo_barras)
            if resultado_busca:
                self.produtos_lidos.append(resultado_busca)

                e_codigo_barras_saida.delete(0, END)
                atualizar_caixa_texto(self.produtos_lidos)

        e_codigo_barras_saida.bind('<Return>', ler_codigo_barras)        



                #------------------------------------funcoes para os alunos----------------------------
        def atualizar_caixa_texto_aluno(alunos_lidos):
            t_alunos_lidos.delete("1.0", END)  # Limpa o conteúdo da caixa de texto
        
            alunos_texto = ""
            for aluno in alunos_lidos:
                nome = aluno[0]
                ra = aluno[1]
                semestre =aluno[2]
                if ra is not None:
                    alunos_texto += f'RA: {ra}, Nome: {nome}, Semestre: {semestre}\n'
                else:
                    alunos_texto += f'Código de Barras: {ra}, Quantidade: {nome}, Produto não encontrado\n'
        
            t_alunos_lidos.insert("1.0", alunos_texto)  # Insere o texto na caixa de texto

        def ler_ra(event):
            ra = e_alunos_saida.get()

            resultado_busca = self.buscar_aluno(ra)
            if resultado_busca:
                self.alunos_lidos.append(resultado_busca)


                e_alunos_saida.delete(0, END)
                atualizar_caixa_texto_aluno(self.alunos_lidos)

        e_alunos_saida.bind('<Return>', ler_ra)     


        def limpar_caixa():
            self.produtos_lidos.clear()
            t_produtos_lidos.delete("1.0", END)
            self.alunos_lidos.clear()
            t_alunos_lidos.delete("1.0", END)


        def confirmar_saida(t_alunos_lidos, t_produtos_lidos):

            # Obtenha o conteúdo das caixas de texto
            alunos_lidos_texto = t_alunos_lidos.get("1.0", "end-1c").split("\n")
            produtos_lidos_texto = t_produtos_lidos.get("1.0", "end-1c").split("\n")

            # Converte o conteúdo em listas
            t_alunos_lidos = [aluno.split(", ") for aluno in alunos_lidos_texto]
            t_produtos_lidos = [produto.split(", ") for produto in produtos_lidos_texto]


            # Verifica se as listas estão preenchidas corretamente
            if not t_produtos_lidos or not t_alunos_lidos:
                messagebox.showwarning('Confirmação de Saída', 'Nenhum aluno ou produto selecionado.')
                return

            for aluno in t_alunos_lidos:
                nome_aluno = aluno[0]
                ra_aluno = aluno[1]
                semestre_aluno = aluno[2]

            for produto in t_produtos_lidos:
                codigo_barras_produto = produto[0]
                quantidade = 1
                nome_produto = produto[1]

                # Subtrai 1 da quantidade do produto
                quantidade -= 1

                # Verifica se a quantidade ficou menor ou igual a zero
                if quantidade <= 0:
                    messagebox.showwarning('Quantidade insuficiente', f'A quantidade do produto {nome_produto} é insuficiente.')
                    return

                # Chama a função para inserir o empréstimo para o produto atual
                inserir_emprestimo(nome_aluno, ra_aluno, semestre_aluno, codigo_barras_produto, quantidade, nome_produto)

 
            # Limpa as listas
            t_produtos_lidos.clear()
            t_alunos_lidos.clear()



            

        b_limpar = Button(frame_meio_saida, text='Limpar', command=limpar_caixa, font=('Ivy 12 bold'), width=10, relief=RAISED, bg='#FF0000', fg='#FFFFFF')
        b_limpar.place(x=450, y=300)

        button_confirmar_saida = Button(frame_meio_saida, text='Confirmar Saída', command=lambda: confirmar_saida(t_alunos_lidos, t_produtos_lidos), font=('Ivy 12 bold'), width=str(10), relief=RAISED, bg='#008000', fg='#FFFFFF')
        button_confirmar_saida.place(x=650, y=300)


    def buscar_produto(self, codigo_barras):

        produto = buscar_produto(codigo_barras)

        if produto is not None:
            return codigo_barras, produto[1], produto[2]
        else:
            messagebox.showwarning('Produto não encontrado', 'O produto correspondente ao código de barras não foi encontrado.')
            return None
        


    def buscar_aluno(self, ra):

        aluno = buscar_alunos(ra)

        if aluno is not None:
            return aluno[0], aluno[1], aluno[2]
        else:
            messagebox.showwarning('RA não encontrado', 'O RA correspondente ao aluno não foi encontrado.')
            return None

        




'''import tkinter as tk
import sqlite3

class EstoqueApp(tk.Tk):
    def _init_(self):
        super()._init_()    
        self.title("Estoque App")
        self.geometry("400x300")
        
        # Conexão com o banco de dados
        self.conn = sqlite3.connect("estoque.db")
        self.c = self.conn.cursor()

        # Campos do formulário
        self.codigo_entry = tk.Entry(self)
        self.produto_entry = tk.Entry(self)
        self.preco_entry = tk.Entry(self)
        self.quantidade_entry = tk.Entry(self)
        self.aluno_entry = tk.Entry(self)

        # Posicionando os campos no formulário
        self.codigo_entry.grid(row=0, column=1)
        self.produto_entry.grid(row=1, column=1)
        self.preco_entry.grid(row=2, column=1)
        self.quantidade_entry.grid(row=3, column=1)
        self.aluno_entry.grid(row=4, column=1)

        # Labels do formulário
        tk.Label(self, text="Código de barras:").grid(row=0, column=0)
        tk.Label(self, text="Produto:").grid(row=1, column=0)
        tk.Label(self, text="Preço:").grid(row=2, column=0)
        tk.Label(self, text="Quantidade:").grid(row=3, column=0)
        tk.Label(self, text="Nome do aluno:").grid(row=4, column=0)

        # Evento KeyPress para o campo de código de barras
        self.codigo_entry.bind("<KeyPress>", self.handle_keypress)

        # Focus no primeiro campo
        self.codigo_entry.focus()

    def handle_keypress(self, event):
        codigo = self.codigo_entry.get()
        
        # Busca no banco de dados pelo código de barras
        self.c.execute("SELECT * FROM produtos WHERE codigo=?", (codigo,))
        produto = self.c.fetchone()

        if produto:
            # Preenche os campos com as informações do produto
            self.produto_entry.delete(0, tk.END)
            self.produto_entry.insert(0, produto[1])
            self.preco_entry.delete(0, tk.END)
            self.preco_entry.insert(0, produto[2])
            self.quantidade_entry.delete(0, tk.END)
            self.quantidade_entry.insert(0, produto[3])

            # Move o foco para o próximo campo
            self.aluno_entry.focus()

app = EstoqueApp()
app.mainloop()'''





#----------------------------------CLASSE PARA A TELA DE PROFESSORES--------------------------------------------------
class Professores:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1366x768")
        self.master.configure(bg="#000000")

        # cria um frame na parte superior da janela
        frame_topo_Professores = tk.Frame(self.master, bg="#2B2F4D", height=66)
        frame_topo_Professores.grid(row=0, column=0, sticky='we') 

        # cria um frame para o meio onde serão prenchidas as informações
        frame_meio_professores = tk.Frame(self.master, bg="#D9D9D9", height=350)
        frame_meio_professores.grid(row=1, column=0, padx=0, pady=1, sticky='we')

        # cria um frame na parte inferior onde sera mostrado o estoque
        frame_baixo_professores = tk.Frame(self.master, bg="white", height=350)
        frame_baixo_professores.grid(row=2, column=0, padx=0, pady=1, sticky='we')

        # cria um novo canvas para os widgets
        self.canvas = tk.Canvas(self.master, bg="#FFFFFF", height=768, width=1366, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.grid(row=3, column=0, sticky='nsew')


        #-------------------------------------CRIANDO FUNÇOES PARA A TELA DOS PROFESSORES----------------------------------------------

        global tree

        #Função inserir
        def inserir ():
            
            nome = e_nome.get()
            email = e_email.get()

            lista_inserir = [nome, email]

            for i in lista_inserir:
                if i == '':
                    tk.messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
                
            inserir_form_professores(lista_inserir)

            tk.messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

            e_nome.delete(0,'end')
            e_email.delete(0,'end')



            mostrar( )

 
        #Função atualizar
        def atualizar():
            
            try:
                treev_dados = tree.focus()
                treev_dicionario = tree.item(treev_dados)
                treev_lista = treev_dicionario['values']
                
                valor = treev_lista[0]

                e_nome.delete(0,'end')
                e_email.delete(0,'end')

                id = int(treev_lista[0])
                e_nome.insert(0, treev_lista[1])
                e_email.insert(0, treev_lista[2])


                def update():
                    
                    nome = e_nome.get()
                    email = e_email.get()



                    lista_atualizar = [nome, email, id]

                    for i in lista_atualizar:
                        if i=='':
                            tk.messagebox.showerror('Erro', 'Preencha todos os campos')
                            return
                        
                    atualizar_form_professores(lista_atualizar)
                    
                    tk.messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')
                    e_nome.delete(0,'end')
                    e_email.delete(0,'end')

            
                    b_confirmar.destroy()
                    mostrar()

                #Botão confirmar
                b_confirmar = Button(frame_meio_professores, command=update, width=19, text= 'Confirmar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold'), bg='#3CB371', fg='#000000')
                b_confirmar.place(x=330, y=191)


            except IndexError:
                tk.messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

        #Função Deletar
        def deletar():
            try:
                treev_dados = tree.focus()
                treev_dicionario = tree.item(treev_dados)
                treev_lista = treev_dicionario['values']
                valor = treev_lista[0]

                deletar_form_professores([valor])
                

                tk.messagebox.showinfo('Sucesso', 'Os dados foram Deletados com sucesso!')
                mostrar()

            except IndexError:
                tk.messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')
    



        #Trbalhando no frame de cima
        # Abrindo imagem do ícone da tela alunos
        self.img_tela_professores = Image.open('img/icones/aluno.png')
        self.img_tela_professores = self.img_tela_professores.resize((60,60))
        self.img_tela_professores = ImageTk.PhotoImage(self.img_tela_professores)

        # Adiciona o ícone da tela no topo do frame
        self.img_logo_professores = Label(frame_topo_Professores, image=self.img_tela_professores, text='   Professores', width=1366, compound=LEFT, anchor=NW, font=('Verdana 35 bold'), bg='#2B2F4D', fg='#FFFFFF')
        self.img_logo_professores.image = self.img_tela_professores
        self.img_logo_professores.pack(side=LEFT, padx=15, pady=10)

        #Criando entradas 
        #Label e entrada para o nome
        l_nome = Label(frame_meio_professores, text= 'Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_nome.place(x=10, y=10)
        e_nome = Entry(frame_meio_professores, width=30, justify='left', relief=SOLID)
        e_nome.place(x=130, y=11)

        #Label e entrada para o email
        l_email = Label(frame_meio_professores, text= 'Email', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_email.place(x=10, y=40)
        e_email = Entry(frame_meio_professores, width=30, justify='left', relief=SOLID)
        e_email.place(x=130, y=41)


        #---------------------------------------CRIANDO BOTÕES-----------------------------------------------------

        #Botão inserir
        b_inserir = Button(frame_meio_professores, command=inserir,  width=20, text= 'Adicionar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_inserir.place(x=330, y=10)

        #Botão update
        b_update = Button(frame_meio_professores,command=atualizar, width=20, text= 'Atualizar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_update.place(x=330, y=50)

        #Botão delete
        b_delete = Button(frame_meio_professores, command=deletar, width=20, text= 'Delete'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_delete.place(x=330, y=90)



        #CRIANDO A TABELA PARA MOSTRAR O ESTOQUE ----------------------------------------------------------------


        def mostrar():

            global tree

            # creating a treeview with dual scrollbars
            tabela_head = ['#Item', 'Nome',  'Email']
            lista_itens = ver_form_alunos()
            global tree

            tree = ttk.Treeview(frame_baixo_professores, selectmode="extended",columns=tabela_head, show="headings")

            # vertical scrollbar
            vsb = ttk.Scrollbar(frame_baixo_professores, orient=VERTICAL, command=tree.yview)

            # horizontal scrollbar
            hsb = ttk.Scrollbar(frame_baixo_professores, orient=HORIZONTAL, command=tree.xview)

            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            tree.grid(column=0, row=0, sticky='nsew')
            vsb.grid(column=1, row=0, sticky='ns')
            hsb.grid(column=0, row=1, sticky='ew')

            # define o peso da linha e coluna do frame como 1
            frame_baixo_professores.grid_rowconfigure(0, weight=1)
            frame_baixo_professores.grid_columnconfigure(0, weight=1)

            hd=["center","center","center"]
            h=[20,120,150]
            n=0

            # define o tamanho da fonte do cabeçalho da tabela
            style = ttk.Style()
            style.configure("Treeview.Heading", font=('Helvetica', 14))

            for col in tabela_head:
                tree.heading(col, text=col.title(), anchor=tk.CENTER)

                # adjust the column's width to the header string
                tree.column(col, width=h[n],anchor=hd[n])

                n+=1

            for item in lista_itens:
                tree.insert('', 'end', values=item)


        mostrar()




#----------------------------------CLASSE PARA A TELA DE EMPRESTIMOS--------------------------------------------------
class Emprestimos:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1366x768")
        self.master.configure(bg="#000000")

        # cria um frame na parte superior da janela
        frame_topo_emprestimos = tk.Frame(self.master, bg="#2B2F4D", height=66)
        frame_topo_emprestimos.grid(row=0, column=0, sticky='we') 

        # cria um frame para o meio onde serão prenchidas as informações
        frame_meio_emprestimos = tk.Frame(self.master, bg="#D9D9D9", height=350)
        frame_meio_emprestimos.grid(row=1, column=0, padx=0, pady=1, sticky='we')

        # cria um frame na parte inferior onde sera mostrado o estoque
        frame_baixo_emprestimos = tk.Frame(self.master, bg="white", height=350)
        frame_baixo_emprestimos.grid(row=2, column=0, padx=0, pady=1, sticky='we')

        # cria um novo canvas para os widgets
        self.canvas = tk.Canvas(self.master, bg="#FFFFFF", height=768, width=1366, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.grid(row=3, column=0, sticky='nsew')




        '''#-------------------------------------CRIANDO FUNÇOES PARA A TELA DOS PROFESSORES----------------------------------------------

        global tree

        #Função inserir
        def inserir ():
            
            Curso = e_Curso.get()
            RA = e_RA.get()
            Nome = e_Nome.get()
            Semestre = e_Semestre.get()
            Turma = e_Turma.get()
            Email = e_Email.get()

            lista_inserir = [Curso, RA, Nome, Semestre, Turma, Email]

            for i in lista_inserir:
                if i == '':
                    tk.messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
                
            inserir_form_alunos(lista_inserir)

            tk.messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

            e_Curso.delete(0,'end')
            e_RA.delete(0,'end')
            e_Nome.delete(0,'end')
            e_Semestre.delete(0,'end')
            e_Turma.delete(0,'end')
            e_Email.delete(0,'end')


            mostrar( )

 
        #Função atualizar
        def atualizar():
            
            try:
                treev_dados = tree.focus()
                treev_dicionario = tree.item(treev_dados)
                treev_lista = treev_dicionario['values']
                
                valor = treev_lista[0]

                e_Curso.delete(0,'end')
                e_RA.delete(0,'end')
                e_Nome.delete(0,'end')
                e_Semestre.delete(0,'end')
                e_Turma.delete(0,'end')
                e_Email.delete(0,'end')

                id = int(treev_lista[0])
                e_Curso.insert(0, treev_lista[1])
                e_RA.insert(0, treev_lista[2])
                e_Nome.insert(0, treev_lista[3])
                e_Semestre.insert(0, treev_lista[4])
                e_Turma.insert(0, treev_lista[5])
                e_Email.insert(0, treev_lista[6])


                def update():
                    
                    Curso = e_Curso.get()
                    RA = e_RA.get()
                    Nome = e_Nome.get()
                    Semestre = e_Semestre.get()
                    Turma = e_Turma.get()
                    Email = e_Email.get()


                    lista_atualizar = [Curso, RA, Nome, Semestre, Turma, Email, id]

                    for i in lista_atualizar:
                        if i=='':
                            tk.messagebox.showerror('Erro', 'Preencha todos os campos')
                            return
                        
                    atualizar_form_alunos(lista_atualizar)
                    
                    tk.messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')
                    e_Curso.delete(0,'end')
                    e_RA.delete(0,'end')
                    e_Nome.delete(0,'end')
                    e_Semestre.delete(0,'end')
                    e_Turma.delete(0,'end')
                    e_Email.delete(0, 'end')
            
                    b_confirmar.destroy()
                    mostrar()

                #Botão confirmar
                b_confirmar = Button(frame_meio_alunos, command=update, width=19, text= 'Confirmar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold'), bg='#3CB371', fg='#000000')
                b_confirmar.place(x=330, y=191)


            except IndexError:
                tk.messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

        #Função Deletar
        def deletar():
            try:
                treev_dados = tree.focus()
                treev_dicionario = tree.item(treev_dados)
                treev_lista = treev_dicionario['values']
                valor = treev_lista[0]

                deletar_form_alunos([valor])
                

                tk.messagebox.showinfo('Sucesso', 'Os dados foram Deletados com sucesso!')
                mostrar()

            except IndexError:
                tk.messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')'''
    



        #Trbalhando no frame de cima
        # Abrindo imagem do ícone da tela alunos
        self.img_tela_emprestimos = Image.open('img/icones/aluno.png')
        self.img_tela_emprestimos = self.img_tela_emprestimos.resize((60,60))
        self.img_tela_emprestimos = ImageTk.PhotoImage(self.img_tela_emprestimos)

        # Adiciona o ícone da tela no topo do frame
        self.img_logo_emprestimos = Label(frame_topo_emprestimos, image=self.img_tela_emprestimos, text='   Emprestimos', width=1366, compound=LEFT, anchor=NW, font=('Verdana 35 bold'), bg='#2B2F4D', fg='#FFFFFF')
        self.img_logo_emprestimos.image = self.img_tela_emprestimos
        self.img_logo_emprestimos.pack(side=LEFT, padx=15, pady=10)

        '''#Criando entradas 
        #Label e entrada para o nome
        l_Curso = Label(frame_meio_alunos, text= 'Curso', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_Curso.place(x=10, y=10)
        e_Curso = Entry(frame_meio_alunos, width=30, justify='left', relief=SOLID)
        e_Curso.place(x=130, y=11)

        #Label e entrada para a localização
        l_RA = Label(frame_meio_alunos, text= 'RA', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_RA.place(x=10, y=40)
        e_RA = Entry(frame_meio_alunos, width=30, justify='left', relief=SOLID)
        e_RA.place(x=130, y=41)

        #Label e entrada para a descrição
        l_Nome = Label(frame_meio_alunos, text= 'Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_Nome.place(x=10, y=70)
        e_Nome = Entry(frame_meio_alunos, width=30, justify='left', relief=SOLID)
        e_Nome.place(x=130, y=71)

        #Label e entrada para a quantidade
        l_Semestre = Label(frame_meio_alunos, text= 'Semestre', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_Semestre.place(x=10, y=100)
        e_Semestre = Entry(frame_meio_alunos, width=30, justify='left', relief=SOLID)
        e_Semestre.place(x=130, y=101)

        #Label e entrada para o codigo de barras
        l_Turma = Label(frame_meio_alunos, text= 'Turma', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_Turma.place(x=10, y=130)
        e_Turma = Entry(frame_meio_alunos, width=30, justify='left', relief=SOLID)
        e_Turma.place(x=130, y=131)


        #Label e entrada para imagem do botão carregar
        l_Email = Label(frame_meio_alunos, text= 'Email', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_Email.place(x=10, y=160)

        e_Email = Entry(frame_meio_alunos, width=30, justify='left', relief=SOLID)
        e_Email.place(x=130, y=161)

        #---------------------------------------CRIANDO BOTÕES-----------------------------------------------------

        #Botão inserir
        b_inserir = Button(frame_meio_alunos, command=inserir,  width=20, text= 'Adicionar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_inserir.place(x=330, y=10)

        #Botão update
        b_update = Button(frame_meio_alunos,command=atualizar, width=20, text= 'Atualizar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_update.place(x=330, y=50)

        #Botão delete
        b_delete = Button(frame_meio_alunos, command=deletar, width=20, text= 'Delete'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_delete.place(x=330, y=90)



        #CRIANDO A TABELA PARA MOSTRAR O ESTOQUE ----------------------------------------------------------------


        def mostrar():

            global tree

            # creating a treeview with dual scrollbars
            tabela_head = ['#Item', 'Curso',  'RA','Nome', 'Semestre', 'Turma', 'Email']
            lista_itens = ver_form_alunos()
            global tree

            tree = ttk.Treeview(frame_baixo_alunos, selectmode="extended",columns=tabela_head, show="headings")

            # vertical scrollbar
            vsb = ttk.Scrollbar(frame_baixo_alunos, orient=VERTICAL, command=tree.yview)

            # horizontal scrollbar
            hsb = ttk.Scrollbar(frame_baixo_alunos, orient=HORIZONTAL, command=tree.xview)

            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            tree.grid(column=0, row=0, sticky='nsew')
            vsb.grid(column=1, row=0, sticky='ns')
            hsb.grid(column=0, row=1, sticky='ew')

            # define o peso da linha e coluna do frame como 1
            frame_baixo_alunos.grid_rowconfigure(0, weight=1)
            frame_baixo_alunos.grid_columnconfigure(0, weight=1)

            hd=["center","center","center","center","center","center", "center"]
            h=[20,40,40,120,40,100, 150]
            n=0

            # define o tamanho da fonte do cabeçalho da tabela
            style = ttk.Style()
            style.configure("Treeview.Heading", font=('Helvetica', 14))

            for col in tabela_head:
                tree.heading(col, text=col.title(), anchor=tk.CENTER)

                # adjust the column's width to the header string
                tree.column(col, width=h[n],anchor=hd[n])

                n+=1

            for item in lista_itens:
                tree.insert('', 'end', values=item)


        mostrar()'''


#----------------------------------CLASSE PARA A TELA DE LABORATORIOS-------------------------------------------------
class Laboratorios:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1366x768")
        self.master.configure(bg="#000000")

        # cria um frame na parte superior da janela
        frame_topo_laboratorios = tk.Frame(self.master, bg="#2B2F4D", height=66)
        frame_topo_laboratorios.grid(row=0, column=0, sticky='we') 

        # cria um frame para o meio onde serão prenchidas as informações
        frame_meio_laboratorios = tk.Frame(self.master, bg="#D9D9D9", height=350)
        frame_meio_laboratorios.grid(row=1, column=0, padx=0, pady=1, sticky='we')

        # cria um frame na parte inferior onde sera mostrado o estoque
        frame_baixo_laboratorios = tk.Frame(self.master, bg="white", height=350)
        frame_baixo_laboratorios.grid(row=2, column=0, padx=0, pady=1, sticky='we')

        # cria um novo canvas para os widgets
        self.canvas = tk.Canvas(self.master, bg="#FFFFFF", height=768, width=1366, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.grid(row=3, column=0, sticky='nsew')




        #-------------------------------------CRIANDO FUNÇOES PARA A TELA DOS PROFESSORES----------------------------------------------
        global tree

        #Função inserir
        def inserir ():            
            nome = e_nome.get()
            lista_inserir = [nome]

            for i in lista_inserir:
                if i == '':
                    tk.messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
                
            inserir_form_laboratorios(lista_inserir)
            tk.messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

            e_nome.delete(0,'end')
            mostrar( )

 
        #Função atualizar
        def atualizar():
            
            try:
                treev_dados = tree.focus()
                treev_dicionario = tree.item(treev_dados)
                treev_lista = treev_dicionario['values']
                
                valor = treev_lista[0]
                e_nome.delete(0,'end')
                id = int(treev_lista[0])
                e_nome.insert(0, treev_lista[1])


                def update():                    
                    nome = e_nome.get()
                    lista_atualizar = [nome, id]
                    for i in lista_atualizar:
                        if i=='':
                            tk.messagebox.showerror('Erro', 'Preencha todos os campos')
                            return
                        
                    atualizar_form_laboratorios(lista_atualizar)
                    
                    tk.messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')
                    e_nome.delete(0,'end')
            
                    b_confirmar.destroy()
                    mostrar()

                #Botão confirmar
                b_confirmar = Button(frame_meio_laboratorios, command=update, width=19, text= 'Confirmar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold'), bg='#3CB371', fg='#000000')
                b_confirmar.place(x=330, y=191)


            except IndexError:
                tk.messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

        #Função Deletar
        def deletar():
            try:
                treev_dados = tree.focus()
                treev_dicionario = tree.item(treev_dados)
                treev_lista = treev_dicionario['values']
                valor = treev_lista[0]

                deletar_form_laboratorios([valor])
                

                tk.messagebox.showinfo('Sucesso', 'Os dados foram Deletados com sucesso!')
                mostrar()

            except IndexError:
                tk.messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')
    


        #Trbalhando no frame de cima
        # Abrindo imagem do ícone da tela alunos
        self.img_tela_laboratorios = Image.open('img/icones/aluno.png')
        self.img_tela_laboratorios = self.img_tela_laboratorios.resize((60,60))
        self.img_tela_laboratorios = ImageTk.PhotoImage(self.img_tela_laboratorios)

        # Adiciona o ícone da tela no topo do frame
        self.img_logo_laboratorios = Label(frame_topo_laboratorios, image=self.img_tela_laboratorios, text='   Laboratorios', width=1366, compound=LEFT, anchor=NW, font=('Verdana 35 bold'), bg='#2B2F4D', fg='#FFFFFF')
        self.img_logo_laboratorios.image = self.img_tela_laboratorios
        self.img_logo_laboratorios.pack(side=LEFT, padx=15, pady=10)

        #Criando entradas 
        #Label e entrada para o nome
        l_nome = Label(frame_meio_laboratorios, text= 'Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_nome.place(x=10, y=10)
        e_nome = Entry(frame_meio_laboratorios, width=30, justify='left', relief=SOLID)
        e_nome.place(x=130, y=11)


        #---------------------------------------CRIANDO BOTÕES-----------------------------------------------------

        #Botão inserir
        b_inserir = Button(frame_meio_laboratorios, command=inserir,  width=20, text= 'Adicionar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_inserir.place(x=330, y=10)

        #Botão update
        b_update = Button(frame_meio_laboratorios,command=atualizar, width=20, text= 'Atualizar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_update.place(x=330, y=50)

        #Botão delete
        b_delete = Button(frame_meio_laboratorios, command=deletar, width=20, text= 'Delete'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_delete.place(x=330, y=90)



        #CRIANDO A TABELA PARA MOSTRAR OS LABORATORIOS ----------------------------------------------------------------


        def mostrar():

            global tree

            # creating a treeview with dual scrollbars
            tabela_head = ['#Item', 'nome']
            lista_itens = ver_form_laboratorios()
            global tree

            tree = ttk.Treeview(frame_baixo_laboratorios, selectmode="extended",columns=tabela_head, show="headings")

            # vertical scrollbar
            vsb = ttk.Scrollbar(frame_baixo_laboratorios, orient=VERTICAL, command=tree.yview)

            # horizontal scrollbar
            hsb = ttk.Scrollbar(frame_baixo_laboratorios, orient=HORIZONTAL, command=tree.xview)

            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            tree.grid(column=0, row=0, sticky='nsew')
            vsb.grid(column=1, row=0, sticky='ns')
            hsb.grid(column=0, row=1, sticky='ew')

            # define o peso da linha e coluna do frame como 1
            frame_baixo_laboratorios.grid_rowconfigure(0, weight=1)
            frame_baixo_laboratorios.grid_columnconfigure(0, weight=1)

            hd=["center","center"]
            h=[20,150]
            n=0

            # define o tamanho da fonte do cabeçalho da tabela
            style = ttk.Style()
            style.configure("Treeview.Heading", font=('Helvetica', 14))

            for col in tabela_head:
                tree.heading(col, text=col.title(), anchor=tk.CENTER)

                # adjust the column's width to the header string
                tree.column(col, width=h[n],anchor=hd[n])

                n+=1

            for item in lista_itens:
                tree.insert('', 'end', values=item)


        mostrar()

