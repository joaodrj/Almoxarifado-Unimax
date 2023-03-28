import tkinter as tk
from home import Home
from tkinter import *

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        

        self.master.geometry("600x400")
        self.master.configure(bg = "#ffffff")
        self.canvas = Canvas(
            master,
            bg = "#ffffff",
            height = 400,
            width = 600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"img/background.png")
        background = self.canvas.create_image(
            290, 200,
            image=background_img)


        entry0_img = PhotoImage(file = f"img/img_textBox0.png")
        entry0_bg = self.canvas.create_image(
            157.5, -49.0,
            image = entry0_img)

        self.username_entry = Entry(
            bd=0,
            bg="#ffffff",
            highlightthickness=0)

        self.username_entry.place(
            x=361, y=151,
            width=203,
            height=34)

        entry1_img = PhotoImage(file = f"img/img_textBox1.png")
        entry1_bg = self.canvas.create_image(
            157.5, -49.0,
            image = entry1_img)

        self.password_entry = Entry(
            bd=0,
            bg="#ffffff",
            highlightthickness=0,
            show="*")

        self.password_entry.place(
            x=361, y=238,
            width=203,
            height=34)

        img0 = PhotoImage(file="img/img0.png")
        self.login_button = Button(
            image=img0,
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
            Home = Home()
        else:
            print("Invalid username or password.")
    
root = tk.Tk()
login = Login(root)
root.mainloop()
