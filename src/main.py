import tkinter as tk
from home import Home
from login import Login

root = tk.Tk()
login = Login(root)
home = Home(root)
root.mainloop()

