import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

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



        #Abrindo imagem do icone da tela estoque
        img_tela_estoque = Image.open('img/icones/inventario.png')
        img_tela_estoque = img_tela_estoque.resize((45,45))
        img_tela_estoque = ImageTk.PhotoImage(img_tela_estoque)

        img_logo_estoque = Label(frame_topo, image= img_tela_estoque, text= 'Estoque', width= 1366, compound=LEFT, relief= RAISED, anchor= NW, font=('Verdana 20 bold'), bg='#2B2F4D', fg='#000000')
        img_logo_estoque.place(x=0, y=0)