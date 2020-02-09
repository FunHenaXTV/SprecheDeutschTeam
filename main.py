import tkinter as tk
from random import randint
import config
import character1
import start
def timer():
    global iter, animation, label
    iter += 1
    if iter == 1:
        time = root.after(7500, timer)
    else:
        label = canvas.create_text(300, 100, text='Choose your character', font='Ubuntu 32', fill='#000')
        animation = start.Hello(root, canvas, label)
def timer_2():
    global iter, lines, hello, animation
    iter += 1
    if iter == 1:
        time = root.after(8700, timer_2)
    else:
        del hello, animation
        lines.append(canvas.create_line(0, 150, 600, 150))
        lines.append(canvas.create_line(300, 150, 300, 600))
        lines.append(canvas.create_line(0, 375, 600, 375))
def click(event):
    global label, animation2
    animation2 = start.Hello(root, canvas, label, -1)
    for i in lines:
        canvas.delete(i)
    if (event.x >= 0 and event.x < 300) and (event.y >= 150 and event.y < 375):
        print('square 1')
    elif (event.x > 300 and event.x < 600) and (event.y > 150 and event.y < 375):
        print('square 2')
    elif (event.x > 0 and event.x < 300) and (event.y > 375 and event.y < 600):
        print('square 3')
    elif (event.x >= 300 and event.x <= 600) and (event.y >= 375 and event.y <= 600):
        print('square 4')

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
