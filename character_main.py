import time

class Physics:
    def __init__(self, root, canvas, character_id, blocks):
        self.speed_x = 0
        self.speed_y = 0
        self.character_id = character_id
        self.root = root
        self.canvas = canvas
        self.blocks = blocks
        self.move()
    def handler(self, event):
        key = event.keysym
        if key == 'Right':
            self.right()
        elif key == 'Left':
            self.left()
        elif key == 'space' or key == 'Up':
            self.jump()
    
    def right(self):
        self.speed_x += .3
        if self.speed_x > 2.5:
            self.speed_x = 2.5

    def left(self):
        self.speed_x -= .3
        if self.speed_x < -2.5:
            self.speed_x = -2.5

    def jump(self):
        if self.speed_y <= 0.00000001 and self.speed_y >= -0.00000001:
            self.speed_y -= 2.5


    def phys(self):
        if self.speed_y <= 0.00001 and self.speed_y >= -0.000001:
            if self.speed_x <= 0.000001 and self.speed_x >= -0.000001:
                pass
            elif self.speed_x > 0:
                self.speed_x -= 0.01*3/2
            elif self.speed_x < 0:
                self.speed_x += 0.01*3/2
        if self.speed_y <= 0.0000001 and self.speed_y >= -0.000000001:
            pass
        else:
            self.speed_y += 0.0098 * 2
    def collision_x(self):
        for block in self.blocks:

            s = self.canvas.coords(self.character_id)[4] - self.canvas.coords(block)[0] > 2.6 and self.canvas.coords(block)[2] - self.canvas.coords(self.character_id)[4] > 2.6
            s1 = self.canvas.coords(self.character_id)[5] - self.canvas.coords(block)[1] > 5 and self.canvas.coords(block)[7] - self.canvas.coords(self.character_id)[5] > 5

            if s and s1:
                self.canvas.move(self.character_id, -(self.canvas.coords(self.character_id)[4] - self.canvas.coords(block)[0]) - 2, 0)
                self.speed_x = -0.7

            s = self.canvas.coords(self.character_id)[6] - self.canvas.coords(block)[0] > 2.6 and self.canvas.coords(block)[2] - self.canvas.coords(self.character_id)[6] > 2.6
            s1 = self.canvas.coords(self.character_id)[7] - self.canvas.coords(block)[1] > 2 and self.canvas.coords(block)[7] - self.canvas.coords(self.character_id)[7] > 2
            if s and s1:
                self.canvas.move(self.character_id, -(self.canvas.coords(self.character_id)[6] - self.canvas.coords(block)[2]) + 2, 0)
                self.speed_x = 0.7



    def collision_y(self):
        blocks = [] # local blocks
        blocks_y_coords = []
        for block in self.blocks:
            statement = self.canvas.coords(self.character_id)[6] < self.canvas.coords(block)[0]
            statement *= self.canvas.coords(self.character_id)[4] > self.canvas.coords(block)[0]

            statement1 = self.canvas.coords(self.character_id)[4] > self.canvas.coords(block)[2]
            statement1 *= self.canvas.coords(self.character_id)[6] < self.canvas.coords(block)[2]

            statement2 = self.canvas.coords(self.character_id)[6] < self.canvas.coords(block)[2]
            statement2 *= self.canvas.coords(self.character_id)[6] > self.canvas.coords(block)[0]

            statement3 = self.canvas.coords(self.character_id)[4] < self.canvas.coords(block)[2]
            statement3 *= self.canvas.coords(self.character_id)[4] > self.canvas.coords(block)[0]

            statement4 = self.canvas.coords(self.character_id)[6] < self.canvas.coords(block)[0]
            statement4 *= self.canvas.coords(self.character_id)[4] > self.canvas.coords(block)[2]

            if statement or statement1 or statement2 or statement3 or statement4:
                if self.canvas.coords(self.character_id)[1] < self.canvas.coords(block)[5]:
                    blocks.append(block) 
                    blocks_y_coords.append(self.canvas.coords(block)[1])
        try:
            if self.canvas.coords(self.character_id)[5] < min(blocks_y_coords):
                self.speed_y += 0.01
            else:
                self.speed_y = 0
        except:
            pass
            s = self.canvas.coords(self.character_id)[6] - self.canvas.coords(block)[0] > 2 and self.canvas.coords(block)[2] - self.canvas.coords(self.character_id)[6] > 2
            s1 = self.canvas.coords(self.character_id)[7] - self.canvas.coords(block)[1] > 5 and self.canvas.coords(block)[7] - self.canvas.coords(self.character_id)[7] > 5

            s2 = self.canvas.coords(self.character_id)[6] - self.canvas.coords(block)[0] > 2 and self.canvas.coords(block)[2] - self.canvas.coords(self.character_id)[6] > 2
            s3 = self.canvas.coords(self.character_id)[7] - self.canvas.coords(block)[1] > 5 and self.canvas.coords(block)[7] - self.canvas.coords(self.character_id)[7] > 5

            if (s and s1) or (s2 and s3):
                self.canvas.move(self.canvas.character_id, 0, -self.canvas.coords(self.character_id)[7] + self.canvas.coords(block)[3] - 2)


        for block in self.blocks:
            statement = self.canvas.coords(self.character_id)[6] < self.canvas.coords(block)[0]
            statement *= self.canvas.coords(self.character_id)[4] > self.canvas.coords(block)[0]

            statement1 = self.canvas.coords(self.character_id)[4] > self.canvas.coords(block)[2]
            statement1 *= self.canvas.coords(self.character_id)[6] < self.canvas.coords(block)[2]

            statement2 = self.canvas.coords(self.character_id)[6] < self.canvas.coords(block)[2]
            statement2 *= self.canvas.coords(self.character_id)[6] > self.canvas.coords(block)[0]

            statement3 = self.canvas.coords(self.character_id)[4] < self.canvas.coords(block)[2]
            statement3 *= self.canvas.coords(self.character_id)[4] > self.canvas.coords(block)[0]

            statement4 = self.canvas.coords(self.character_id)[6] < self.canvas.coords(block)[0]
            statement4 *= self.canvas.coords(self.character_id)[4] > self.canvas.coords(block)[2]

            if statement or statement1 or statement2 or statement3 or statement4:
                if abs(self.canvas.coords(self.character_id)[1] - self.canvas.coords(block)[5]) < 1:
                    self.speed_y = 0.1




    def move(self):
        #self.canvas.xview_scroll(int(self.speed_x*2), 'units')
        #self.canvas.yview_scroll(int(self.speed_y*2), 'units')
        self.phys()
        self.canvas.move(self.character_id, self.speed_x, self.speed_y)
        self.collision_y()
        self.collision_x()
        self.root.after(10, self.move)





