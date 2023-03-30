import tkinter as tk
from tkinter import *

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

        self.img0 = tk.PhotoImage(file = f"img/tela_inicial/img0.png")
        self.b0 = tk.Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")
        
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
            relief = "flat")

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


