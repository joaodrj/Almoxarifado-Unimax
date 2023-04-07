import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

#cria a classe Home para a tela principal
class Home:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1366x768")
        self.master.configure(bg = "#FFFFFF")
        self.canvas = Canvas(
            master,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0) 

        self.background_img = tk.PhotoImage(file = f"img/tela_inicial/background.png")
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
        
        self.b0.place(
            x = 0, y = 236,
            width = 320,
            height = 117)
        
        self.canvas.create_window(0, 236, anchor=NW, window=self.b0)




        self.img1 = tk.PhotoImage(file = f"img/tela_inicial/img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",)

        self.b1.place(
            x = 0, y = 478,
            width = 320,
            height = 117)

        self.canvas.create_window(0, 478, anchor=NW, window=self.b1)

        

        self.img2 = tk.PhotoImage(file = f"img/tela_inicial/img2.png")
        self.b2 = Button(
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")

        self.b2.place(
            x = 0, y = 599,
            width = 320,
            height = 117)
        self.canvas.create_window(0, 599, anchor=NW, window=self.b2)



        self.img3 = tk.PhotoImage(file = f"img/tela_inicial/img3.png")
        self.b3 = Button(
            image = self.img3,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")
        
        self.b3.place(
            x = 0, y = 114.69,
            width = 320,
            height = 117)
        self.canvas.create_window(0, 114.69, anchor=NW, window=self.b3)



        self.img4 = PhotoImage(file = f"img/tela_inicial/img4.png")
        self.b4 = Button(
            image = self.img4,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")

        self.b4.place(
            x = 0, y = 357,
            width = 320,
            height = 117)
        self.canvas.create_window(0, 357, anchor=NW, window=self.b4)



        self.img5 = PhotoImage(file = f"img/tela_inicial/img5.png")
        self.b5 = Button(
            image = self.img5,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")

        self.b5.place(
            x = 451, y = 298,
            width = 319,
            height = 207)
        self.canvas.create_window(451, 298, anchor=NW, window=self.b5)



        self.img6 = tk.PhotoImage(file = f"img/tela_inicial/img6.png")
        self.b6 = Button(
            image = self.img6,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")

        self.b6.place(
            x = 925, y = 298,
            width = 319,
            height = 207)
        self.canvas.create_window(925, 298, anchor=NW, window=self.b6)

        self.master.mainloop()

    def open_estoque_window(self):
        # Cria a janela de estoque
        self.estoque_window = Toplevel(self.master)
        estoque = Estoque(self.estoque_window)


class Estoque:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1366x768")
        self.master.configure(bg="#000000")

        # cria um frame na parte superior da janela
        frame_topo = tk.Frame(self.master, bg="#2B2F4D", height=66)
        frame_topo.grid(row=0, column=0, sticky='we') 

        '''# adiciona um label ao topo do frame
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
        e_codigo_barras = Entry(frame_meio, width=30, justify='left', relief=SOLID)
        e_codigo_barras.place(x=130, y=131)


        #Criando botões---------------------------------------------------------------------------------------------------------

        #Label e entrada para imagem do botão carregar
        l_imagem = Label(frame_meio, text= 'Imagem do item', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#D9D9D9', fg='#000000')
        l_imagem.place(x=10, y=160)
        #botao para carregar a imagem
        b_carregar = Button(frame_meio, width=29, text= 'carregar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_carregar.place(x=130, y=161)

    

        #Botão inserir
        b_inserir = Button(frame_meio, width=20, text= 'Adicionar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_inserir.place(x=330, y=10)

        #Botão update
        b_update = Button(frame_meio, width=20, text= 'Update'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_update.place(x=330, y=50)

        #Botão delete
        b_delete = Button(frame_meio, width=20, text= 'Update'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_delete.place(x=330, y=90)

        #Botão ver imagem
        b_item = Button(frame_meio, width=20, text= 'Ver item'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#D9D9D9', fg='#000000')
        b_item.place(x=330, y=161)



        #CRIANDO A TABELA PARA MOSTRAR O ESTOQUE ----------------------------------------------------------------


        def mostrar():

            # creating a treeview with dual scrollbars
            tabela_head = ['#Item','Nome',  'Sala/Área','Descrição', 'Marca/Modelo', 'Número de série']
            lista_itens = []
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
            h=[40,150,100,160,130,100]
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


