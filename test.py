from graphics import *
import time
import random

# --- classes ---

class Player:
    def __init__(self, window, char, color):
        self.win = window
        self.rect = char
        self.color = color

        self.rect.setFill(self.color)
        self.rect.draw(self.win)

    def movement(self):
        # use `keys.get("d")` instead of `keys["d"]` because `"d"` may not exists in dictionary `key`
        if self.win.keys.get("d"):
            self.rect.move(10, 0)
        if self.win.keys.get("a"):
            self.rect.move(-10, 0)
        if self.win.keys.get("s"):
            self.rect.move(0, 10)
        if self.win.keys.get("w"):
            self.rect.move(0, -10)

class Enemy:
    def __init__(self, window, rect, color):
        self.win = window
        self.rect = rect
        self.color = color

        self.rect.setFill(self.color)
        self.rect.draw(self.win)

    def movement(self):
        dx = random.randint(-30, 30)
        dy = random.randint(-30, 30)
        self.rect.move(dx, dy)

# --- main ---

point1 = Point(680, 420)
point2 = Point(720, 380)

point3 = Point(180, 420)
point4 = Point(220, 380)

win = GraphWin("mini graphic game", 1400, 800)

player = Player(win, Rectangle(point1, point2), color_rgb(0, 255, 0))
enemies = [Enemy(win, Rectangle(point3, point4), color_rgb(255, 0, 0)) for _ in range(10)]

while not win.isClosed():
    player.movement()
    for e in enemies:
        e.movement()

    win.update()
    time.sleep(.1)

win.close()