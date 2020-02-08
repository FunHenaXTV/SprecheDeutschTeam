import tkinter as tk
from random import randint
import config
import character1
import start
def timer():
    global iter
    iter += 1
    print(iter)
    if iter == 1:
        time = root.after(5000, timer)
    else:
        canvas.create_text(20, 20, text='test')

iter = 0
root = tk.Tk()
root.title("SprecheDeutschTeam")
root.configure(bg='#fff', width=600, height=600)
canvas = tk.Canvas(root, bg='#fff', width=600, height=600)
canvas.pack()
hello = start.Hello(root, canvas)
timer()
root.mainloop()
