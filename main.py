import tkinter as tk
from random import randint
from PIL import Image, ImageTk
import config
import character_main
import start
def timer():
    global iter, animation, label
    iter += 1
    if iter == 1:
        if config.fast_load == 1:
            time = root.after(750, timer)
        else:
            time = root.after(7500, timer)
    else:
        label = canvas.create_text(960, 180, text='Choose your character', font='Ubuntu 42', fill='#000')
        animation = start.Hello(root, canvas, label)
def timer_2():
    global iter, lines, hello, animation, photo
    iter += 1
    if iter == 1:
        if config.fast_load == 1:
            time = root.after(870, timer_2)
        else:
            time = root.after(8700, timer_2)
    else:
        del hello, animation
        lines.append(canvas.create_line(0, 220, 1920, 220))
        lines.append(canvas.create_line(960, 220, 960, 1080))
        lines.append(canvas.create_line(0, 650, 1920, 650))

        photo.create()

class Photo:
    def __init__(self):
        pass

    def create(self):
        self.pilImage1 = Image.open("character-1.png")
        self.image1 = ImageTk.PhotoImage(self.pilImage1)
        self.logo_1 = canvas.create_image(480, 435, image=self.image1)

        self.pilImage2 = Image.open("character-2.png")
        self.image2 = ImageTk.PhotoImage(self.pilImage2)
        self.logo_2 = canvas.create_image(1440, 435, image=self.image2)

        self.pilImage3 = Image.open("character-3.png")
        self.image3 = ImageTk.PhotoImage(self.pilImage3)
        self.logo_3 = canvas.create_image(480, 865, image=self.image3)

        self.pilImage4 = Image.open("character-4.png")
        self.image4 = ImageTk.PhotoImage(self.pilImage4)
        self.logo_4 = canvas.create_image(1440, 865 , image=self.image4)



    def click(self, event):
        global label, animation2, value, blocks
        value += 1
        if value < 2:
            animation2 = start.Hello(root, canvas, label, -1)
            for i in lines:
                canvas.delete(i)
            canvas.delete(self.logo_1)
            canvas.delete(self.logo_2)
            canvas.delete(self.logo_3)
            canvas.delete(self.logo_4)
            del self.logo_1, self.logo_2, self.logo_3, self.logo_4
            del self.pilImage4, self.pilImage3, self.pilImage2, self.pilImage1
            del self.image1, self.image2, self.image3, self.image4
            if (event.x >= 0 and event.x < 960) and (event.y >= 220 and event.y < 650):
                print('square 1')
                character = canvas.create_polygon(500, 500, 600, 500, 600, 700, 500, 700, outline='green', fill='#fff', width=3)
                blocks.append(canvas.create_polygon(0, 800, 800, 800, 800, 1080, 0, 1080, outline='red', fill='#fff'))
                blocks.append(canvas.create_polygon(800, 900, 1000, 900, 1000, 1080, 800, 1080, outline='red', fill='#fff'))
                blocks.append(canvas.create_polygon(1000, 1000, 1200, 1000, 1200, 1080, 1000, 1080, outline='red', fill='#fff'))
                blocks.append(canvas.create_polygon(1200, 1030, 1920, 1030, 1920, 1080, 1200, 1080, outline='red', fill='#fff'))
                blocks.append(canvas.create_polygon(1600, 800, 1920, 800, 1920, 1030, 1600, 1030, outline='red', fill='#fff'))
                blocks.append(canvas.create_polygon(0, 450, 1200, 450, 1200, 490, 0, 490, outline='red', fill='#fff'))
                physics = character_main.Physics(root, canvas, character, blocks)

                root.bind_all('<Key>', physics.handler)
            elif (event.x > 960 and event.x < 1920) and (event.y > 220 and event.y < 650):
                print('square 2')
            elif (event.x > 0 and event.x < 960) and (event.y > 650 and event.y < 1080):
                print('square 3')
            elif (event.x >= 960 and event.x <= 1920) and (event.y >= 650 and event.y <= 1080):
                print('square 4')

value = 0
iter = 0
lines = []
blocks = []

root = tk.Tk()
root.title("SprecheDeutschTeam")
root.configure(bg='#fff', width=1920, height=1080)
root.state('zoomed')
root.overrideredirect(config.fullsize_window)
canvas = tk.Canvas(root, bg='#fff', width=1920, height=1080)
canvas.pack()
blocks.append(canvas.create_polygon(0, 0, 1920, 0, 1920, 1, 1, 0, outline='red', fill='#fff'))
hello = start.Hello(root, canvas)
timer()
iter = 0
timer_2()
photo = Photo()

canvas.bind('<Button-1>', photo.click)

root.mainloop()
