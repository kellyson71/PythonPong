import tkinter as tk
from data import screenBounds


class GameObject:

    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, canvas: tk.Canvas):
        canvas.create_rectangle(self.x, self.y,
                                self.x + self.width, self.y + self.height,
                                fill="#ffffff")

    def update(self):
        pass


class Paddle(GameObject):
    width = 10
    height = 70

    def __init__(self, x: float, y: float):
        super().__init__(x, y, Paddle.width, Paddle.height)

        self.speed = 0.25

        self.UP = False
        self.DOWN = False

    def update(self):
        speed = 0

        if self.UP:
            speed = -self.speed

        elif self.DOWN:
            speed = self.speed

        if self.y + speed <= 0:
            self.y = 0
            speed = 0
        elif self.y + self.height + speed >= screenBounds[1]:
            self.y = screenBounds[1] - self.height
            speed = 0

        self.y += speed
