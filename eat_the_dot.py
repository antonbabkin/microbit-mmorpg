
from random import randint

from microbit import *
import music

FF_FANFARE = ["c5:1", "c5:1", "c5:1", "c5:3", "ab4:3", "bb4:3", "c5:2", "bb4:1", "c5:9"]

class Sprite:
    def __init__(self, x, y, brightness=9):
        self.x = x
        self.y = y
        self.brightness = brightness

    def clear(self):
        display.set_pixel(self.x, self.y, 0)

    def show(self):
        display.set_pixel(self.x, self.y, self.brightness)

class Mob(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, 1)
        self.last_moved = running_time()

    def input_move(self):
        tilt_threshold = 250
        if accelerometer.get_x() < -tilt_threshold:
            self.move("w")
        elif accelerometer.get_x() > tilt_threshold:
            self.move("e")
        elif accelerometer.get_y() < -tilt_threshold:
            self.move("n")
        elif accelerometer.get_y() > tilt_threshold:
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
            if x1 == food.x and y1 == food.y:
                audio.play(Sound.HAPPY, wait=True)
                self.brightness = min(9, self.brightness + 1)
                while food.x == x1 and food.y == y1:
                    food.jump()
                food.show()
            
            self.last_moved = now
            self.clear()
            self.x = x1
            self.y = y1
            self.show()


class Food(Sprite):
    def __init__(self):
        super().__init__(randint(0, 4), randint(0, 4), 1)
        self.brighten = True

    def jump(self):
        self.x = randint(0, 4)
        self.y = randint(0, 4)

    def update(self):
        if self.brighten:
            self.brightness += 1
            if self.brightness >= 5:
                self.brighten = False
        else:
            self.brightness -= 1
            if self.brightness <= 1:
                self.brighten = True
        self.show()


hero = Mob(2, 2)
hero.show()

food = Food()
while food.x == hero.x and food.y == hero.y:
    food.jump()
food.show()

while True:
    sleep(100)
    hero.input_move()
    food.update()
    if hero.brightness >= 9:
        music.play(FF_FANFARE, wait=False)
        display.show(Image.HAPPY, loop=True)

