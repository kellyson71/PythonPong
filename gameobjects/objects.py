# objects.py
import tkinter as tk
from data import screenBounds
import random


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

        self.speed = 3

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


class Ball(GameObject):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, 10, 10)
        self.x_speed = random.choice([-1, 1])
        self.y_speed = random.choice([-1, 1])

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed

        if self.y <= 0 or self.y + self.height >= screenBounds[1]:
            self.y_speed = -self.y_speed

    def reset(self):
        self.x = screenBounds[0] / 2
        self.y = screenBounds[1] / 2
        self.x_speed = random.choice([-1, 1])
        self.y_speed = random.choice([-1, 1])


class Scoreboard:
    def __init__(self):
        self.score_left = 0
        self.score_right = 0

    def increase_score_left(self):
        self.score_left += 1

    def increase_score_right(self):
        self.score_right += 1

    def reset_scores(self):
        self.score_left = 0
        self.score_right = 0
