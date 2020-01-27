import tkinter as tk
import time
class Hello:
    def __init__(self):
        self.label = canvas.create_text(300, 250, text='SprecheDeutsch Team', font="Verdana 30", fill='#fff')
        self.label2 = canvas.create_text(300, 300, text='Presents', font="Verdana 30", fill='#fff')
        self.iter = 0
        self.kof = 1
        self.k = 0
        self.color()
    def color(self):
        self.iter += self.kof*1
        if self.iter == 1:
            canvas.itemconfig(self.label, fill='#FAFAFA')
            canvas.itemconfig(self.label2, fill='#FAFAFA')
        elif self.iter == 2:
            canvas.itemconfig(self.label, fill='#F2F2F2')
            canvas.itemconfig(self.label2, fill='#F2F2F2')
        elif self.iter == 3:
            canvas.itemconfig(self.label, fill='#E6E6E6')
            canvas.itemconfig(self.label2, fill='#E6E6E6')
        elif self.iter == 4:
            canvas.itemconfig(self.label, fill='#D8D8D8')
            canvas.itemconfig(self.label2, fill='#D8D8D8')
        elif self.iter == 5:
            canvas.itemconfig(self.label, fill='#BDBDBD')
            canvas.itemconfig(self.label2, fill='#BDBDBD')
        elif self.iter == 6:
            canvas.itemconfig(self.label, fill='#A4A4A4')
            canvas.itemconfig(self.label2, fill='#A4A4A4')
        elif self.iter == 7:
            canvas.itemconfig(self.label, fill='#848484')
            canvas.itemconfig(self.label2, fill='#848484')
        elif self.iter == 8:
            canvas.itemconfig(self.label, fill='#6E6E6E')
            canvas.itemconfig(self.label2, fill='#6E6E6E')
        elif self.iter == 9:
            canvas.itemconfig(self.label, fill='#585858')
            canvas.itemconfig(self.label2, fill='#585858')
        elif self.iter == 10:
            canvas.itemconfig(self.label, fill='#424242')
            canvas.itemconfig(self.label2, fill='#424242')
        elif self.iter == 11:
            canvas.itemconfig(self.label, fill='#2E2E2E')
            canvas.itemconfig(self.label2, fill='#2E2E2E')
        elif self.iter == 12:
            canvas.itemconfig(self.label, fill='#1C1C1C')
            canvas.itemconfig(self.label2, fill='#1C1C1C')
        elif self.iter == 13:
            canvas.itemconfig(self.label, fill='#151515')
            canvas.itemconfig(self.label2, fill='#151515')
        elif self.iter == 14:
            canvas.itemconfig(self.label, fill='#000')
            canvas.itemconfig(self.label2, fill='#000')
        elif self.iter == 15:
            self.kof = -1
            self.k += 1
        elif self.iter == 0:
            self.kof = 1
            self.k += 1
        if self.k == 3:
            timer()
        root.after(100, self.color)
def timer():
    global iter
    iter += 1
    if iter >= 2:
        root.destroy()
    root.after(5000, timer)
iter = 0
root = tk.Tk()
root.title("SprecheDeutschTeam")
root.configure(bg='#fff', width=600, height=600)

canvas = tk.Canvas(root, bg='#fff', width=600, height=600)
canvas.pack()
hello = Hello()

root.mainloop()
