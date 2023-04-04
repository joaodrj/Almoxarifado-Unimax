import tkinter as tk
from home import Home

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("600x400")
        self.master.configure(bg = "#ffffff")
        

        self.canvas = tk.Canvas(
            master,
            bg = "#ffffff",
            height = 400,
            width = 600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.pack()

        self.background_img = tk.PhotoImage(file = "img/background.png")
        self.canvas.create_image(
            290, 200,
            image=self.background_img)

        self.entry0_img = tk.PhotoImage(file = "img/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            157.5, -49.0,
            image = self.entry0_img)

        self.username_entry = tk.Entry(
            bd=0,
            bg="#ffffff",
            highlightthickness=0)

        self.username_entry.place(
            x=361, y=151,
            width=203,
            height=34)

        self.entry1_img = tk.PhotoImage(file = "img/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            157.5, -49.0,
            image = self.entry1_img)

        self.password_entry = tk.Entry(
            bd=0,
            bg="#ffffff",
            highlightthickness=0,
            show="*")

        self.password_entry.place(
            x=361, y=238,
            width=203,
            height=34)

        self.img0 = tk.PhotoImage(file="img/img0.png")
        self.login_button = tk.Button(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=self.login,
            relief="flat")

        self.login_button.place(
            x=414, y=302,
            width=97,
            height=34)

        self.master.resizable(False, False)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            self.master.destroy()
            home = Home()
        else:
            print("Invalid username or password.")
    
root = tk.Tk()
login = Login(root)
root.mainloop()
