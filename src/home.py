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
    

        self.master.mainloop()
