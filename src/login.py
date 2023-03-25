import tkinter as tk
from home import Home

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("500x400")

        self.label_usuario = tk.Label(self.master, text="Usuário:", font=("Arial", 16))
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(self.master)
        self.entry_usuario.pack()

        self.label_senha = tk.Label(self.master, text="Senha:")
        self.label_senha.pack()
        self.entry_senha = tk.Entry(self.master, show="*")
        self.entry_senha.pack()

        self.button_login = tk.Button(self.master, text="Login", command=self.fazer_login)
        self.button_login.pack()

        # centralizar a janela
        window_width = 400
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

    def fazer_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        if usuario == "admin" and senha == "admin":
            self.master.destroy()
            home = Home()

root = tk.Tk()
login = Login(root)
root.mainloop()
