
from microbit import *

class Mob:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.last_moved = running_time()

    def clear(self):
        display.set_pixel(self.x, self.y, 0)

    def show(self):
        display.set_pixel(self.x, self.y, 5)

    def input_move(self):
        if accelerometer.get_x() < -300:
            self.move("w")
        elif accelerometer.get_x() > 300:
            self.move("e")
        elif accelerometer.get_y() < -300:
            self.move("n")
        elif accelerometer.get_y() > 300:
            self.move("s")
        
    def move(self, dir):
        now = running_time()
        if now < self.last_moved + 500:
            return
        
        x0, y0 = x1, y1 = self.x, self.y
        if dir == "w" and x0 > 0:
            x1 = x0 - 1
        elif dir == "e" and x0 < 4:
            x1 = x0 + 1
        elif dir == "n" and y0 > 0:
            y1 = y0 - 1
        elif dir == "s" and y0 < 4:
            y1 = y0 + 1

        if x1 != x0 or y1 != y0:
            self.last_moved = now
            self.clear()
            self.x = x1
            self.y = y1
            self.show()
        

hero = Mob(2, 2)
hero.show()

while True:
    sleep(100)
    hero.input_move()
