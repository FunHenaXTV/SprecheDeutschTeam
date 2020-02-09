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
            self.speed_x += .1
            if self.speed_x > 1:
                self.speed_x = 1
        elif key == 'Left':
            self.speed_x -= .1
            if self.speed_x < -1:
                self.speed_x = -1
        elif key == 'space' or key == 'Up':
            if self.speed_y <= 0.00000001 and self.speed_y >= -0.00000001:
                self.speed_y -= 2
    def phys(self):
        if self.speed_y <= 0.00001 and self.speed_y >= -0.000001:
            if self.speed_x <= 0.000001 and self.speed_x >= -0.000001:
                pass
            elif self.speed_x > 0:
                self.speed_x -= 0.01/2
            elif self.speed_x < 0:
                self.speed_x += 0.01/2
        if self.speed_y <= 0.0000001 and self.speed_y >= -0.000000001:
            pass
        else:
            self.speed_y += 0.0098
    def collision_x(self):
        pass
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
                blocks.append(block)
                blocks_y_coords.append(self.canvas.coords(block)[1])
        if self.canvas.coords(self.character_id)[5] < min(blocks_y_coords):
            self.speed_y += 0.01
        else:
            self.speed_y = 0


    def move(self):
        self.canvas.move(self.character_id, self.speed_x, self.speed_y)
        self.phys()
        self.collision_x()
        self.collision_y()
        self.root.after(10, self.move)





