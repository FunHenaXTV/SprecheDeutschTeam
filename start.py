class Hello:
    def __init__(self, root, canvas, label_change='', value=1):
        self.root = root
        self.canvas = canvas
        self.label_change = label_change
        self.iter = 0
        self.kof = 1
        self.k = 0
        self.timer = 0
        self.value = value
        if self.label_change == '':
            self.label = canvas.create_text(300, 250, text='SprecheDeutsch Team', font="Verdana 30", fill='#fff')
            self.label2 = canvas.create_text(300, 300, text='Presents', font="Verdana 30", fill='#fff')
            self.color()
        else:
            if self.value == -1:
                self.kof = -1
                self.iter = 15
            self.change_color_animation()

        

    def color(self):
        self.timer += 1
        self.iter += self.kof*1
        if self.iter == 0:
            self.canvas.itemconfig(self.label, fill='#FFF')
            self.canvas.itemconfig(self.label2, fill='#FFF')
        elif self.iter == 1:
            self.canvas.itemconfig(self.label, fill='#FAFAFA')
            self.canvas.itemconfig(self.label2, fill='#FAFAFA')
        elif self.iter == 2:
            self.canvas.itemconfig(self.label, fill='#F2F2F2')
            self.canvas.itemconfig(self.label2, fill='#F2F2F2')
        elif self.iter == 3:
            self.canvas.itemconfig(self.label, fill='#E6E6E6')
            self.canvas.itemconfig(self.label2, fill='#E6E6E6')
        elif self.iter == 4:
            self.canvas.itemconfig(self.label, fill='#D8D8D8')
            self.canvas.itemconfig(self.label2, fill='#D8D8D8')
        elif self.iter == 5:
            self.canvas.itemconfig(self.label, fill='#BDBDBD')
            self.canvas.itemconfig(self.label2, fill='#BDBDBD')
        elif self.iter == 6:
            self.canvas.itemconfig(self.label, fill='#A4A4A4')
            self.canvas.itemconfig(self.label2, fill='#A4A4A4')
        elif self.iter == 7:
            self.canvas.itemconfig(self.label, fill='#848484')
            self.canvas.itemconfig(self.label2, fill='#848484')
        elif self.iter == 8:
            self.canvas.itemconfig(self.label, fill='#6E6E6E')
            self.canvas.itemconfig(self.label2, fill='#6E6E6E')
        elif self.iter == 9:
            self.canvas.itemconfig(self.label, fill='#585858')
            self.canvas.itemconfig(self.label2, fill='#585858')
        elif self.iter == 10:
            self.canvas.itemconfig(self.label, fill='#424242')
            self.canvas.itemconfig(self.label2, fill='#424242')
        elif self.iter == 11:
            self.canvas.itemconfig(self.label, fill='#2E2E2E')
            self.canvas.itemconfig(self.label2, fill='#2E2E2E')
        elif self.iter == 12:
            self.canvas.itemconfig(self.label, fill='#1C1C1C')
            self.canvas.itemconfig(self.label2, fill='#1C1C1C')
        elif self.iter == 13:
            self.canvas.itemconfig(self.label, fill='#151515')
            self.canvas.itemconfig(self.label2, fill='#151515')
        elif self.iter == 14:
            self.canvas.itemconfig(self.label, fill='#000')
            self.canvas.itemconfig(self.label2, fill='#000')
        elif self.iter == 15:
            self.kof = -1
            self.k += 1
        elif self.iter == -1:
            self.kof = 1
            self.k += 1
        if self.k < 4:
            self.loop = self.root.after(100, self.color)
        else:
            self.canvas.delete(self.label, self.label2)
            del self.label, self.label2
            self.root.after_cancel(self.loop)

    def change_color_animation(self):
        self.iter += self.kof*1
        if self.iter == 0:
            self.canvas.itemconfig(self.label_change, fill='#FFF')
        elif self.iter == 1:
            self.canvas.itemconfig(self.label_change, fill='#FAFAFA')
        elif self.iter == 2:
            self.canvas.itemconfig(self.label_change, fill='#F2F2F2')
        elif self.iter == 3:
            self.canvas.itemconfig(self.label_change, fill='#E6E6E6')
        elif self.iter == 4:
            self.canvas.itemconfig(self.label_change, fill='#D8D8D8')
        elif self.iter == 5:
            self.canvas.itemconfig(self.label_change, fill='#BDBDBD')
        elif self.iter == 6:
            self.canvas.itemconfig(self.label_change, fill='#A4A4A4')
        elif self.iter == 7:
            self.canvas.itemconfig(self.label_change, fill='#848484')
        elif self.iter == 8:
            self.canvas.itemconfig(self.label_change, fill='#6E6E6E')
        elif self.iter == 9:
            self.canvas.itemconfig(self.label_change, fill='#585858')
        elif self.iter == 10:
            self.canvas.itemconfig(self.label_change, fill='#424242')
        elif self.iter == 11:
            self.canvas.itemconfig(self.label_change, fill='#2E2E2E')
        elif self.iter == 12:
            self.canvas.itemconfig(self.label_change, fill='#1C1C1C')
        elif self.iter == 13:
            self.canvas.itemconfig(self.label_change, fill='#151515')
        elif self.iter == 14:
            self.canvas.itemconfig(self.label_change, fill='#000')
        if self.iter == 15 or self.iter == 0:
            self.k += 1
        if self.k < 1:
            self.loop = self.root.after(100, self.change_color_animation)


iter = 0
kof = 1
k = 0
# root = tk.Tk()
# root.title("SprecheDeutschTeam")
# root.configure(bg='#fff', width=600, height=600)

# canvas = tk.Canvas(root, bg='#fff', width=600, height=600)
# canvas.pack()
# hello = Hello()

# root.mainloop()
