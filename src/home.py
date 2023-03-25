import tkinter as tk

class Home:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Home")

        # Cria uma barra de menus
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        # Adiciona um item "Arquivo" com um submenu "Sair"
        arquivo_menu = tk.Menu(menu_bar, tearoff=0)
        arquivo_menu.add_command(label="Sair", command=self.master.quit)
        menu_bar.add_cascade(label="Arquivo", menu=arquivo_menu)

        self.label_bem_vindo = tk.Label(self.master, text="Controle de Estoque Unimax", font=("Arial", 16))
        self.label_bem_vindo.pack()

        self.master.mainloop()
