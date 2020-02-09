class Physics:
    def __init__(self, root, canvas, character_id):
        self.speed_x = 0
        self.speed_y = 0
        self.character_id = character_id
        self.root = root
        self.canvas = canvas
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
            if self.speed_y == 0:
                self.speed_y -= 1
    def phys(self):
        if self.speed_y <= 0.00001 and self.speed_y >= -0.000001:
            if self.speed_x <= 0.000001 and self.speed_x >= -0.000001:
                pass
            elif self.speed_x > 0:
                self.speed_x -= 0.01
            elif self.speed_x < 0:
                self.speed_x += 0.01

        if self.speed_y <= 0.0000001 and self.speed_y >= -0.000000001:
            pass
        else:
            self.speed_y += 0.0098

    def move(self):
        self.canvas.move(self.character_id, self.speed_x, self.speed_y)
        self.phys()
        self.root.after(10, self.move)





