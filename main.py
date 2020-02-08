import tkinter as tk
from random import randint
import config
import character1
import start
root = tk.Tk()
root.title("SprecheDeutschTeam")
root.configure(bg='#fff', width=600, height=600)

canvas = tk.Canvas(root, bg='#fff', width=600, height=600)
canvas.pack()
start.Hello(root, canvas)
root.mainloop()
