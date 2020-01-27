import tkinter as tk
import time
class Hello:
    def __init__(self):
        label = canvas.create_text(300, 250, text='SprecheDeutsch Team', font="Verdana 30")
        label2 = canvas.create_text(300, 300, text='Presents', font="Verdana 30")
def timer():
    global iter
    iter += 1
    if iter >= 2:
        quit()
    root.after(2000, timer)
iter = 0
root = tk.Tk()
root.title("SprecheDeutschTeam")
root.configure(bg='#fff', width=600, height=600)

canvas = tk.Canvas(root, bg='#fff', width=600, height=600)
canvas.pack()
HELLO = Hello()
timer()

root.mainloop()
