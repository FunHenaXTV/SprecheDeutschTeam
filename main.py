import tkinter as tk
from random import randint
import config
import character1
import start
def timer():
    global iter
    iter += 1
    if iter == 1:
        time = root.after(7500, timer)
    else:
        label = canvas.create_text(300, 100, text='Choose your character', font='Ubuntu 32', fill='#fff')
        animation = start.Hello(root, canvas, label)
def timer_2():
    global iter, lines
    iter += 1
    if iter == 1:
        time = root.after(8700, timer_2)
    else:
        lines.append(canvas.create_line(0, 150, 600, 150))
        lines.append(canvas.create_line(300, 150, 300, 600))
        lines.append(canvas.create_line(0, 375, 600, 375))
def click(event):
    print(event.x, event.y)
iter = 0
lines = []
root = tk.Tk()
root.title("SprecheDeutschTeam")
root.configure(bg='#fff', width=600, height=600)
canvas = tk.Canvas(root, bg='#fff', width=600, height=600)
canvas.pack()
hello = start.Hello(root, canvas)
timer()
iter = 0
timer_2()
canvas.bind('<Button-1>', click)
root.mainloop()
