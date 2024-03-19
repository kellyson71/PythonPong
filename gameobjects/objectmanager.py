# objectmanager.py
import tkinter as tk
from data import screenBounds
from .objects import Paddle, Ball, Scoreboard


class ObjManager:
    def __init__(self):
        self.objects = []
        self.objects.append(Paddle(50, (screenBounds[1] - Paddle.height) / 2))
        self.objects.append(
            Paddle(screenBounds[0] - 50 - Paddle.width, (screenBounds[1] - Paddle.height) / 2))
        self.objects.append(Ball(screenBounds[0] / 2, screenBounds[1] / 2))
        self.scoreboard = Scoreboard()

    def render(self, canvas: tk.Canvas):
        canvas.delete("all")

        for obj in self.objects:
            obj.render(canvas)

        canvas.create_text(screenBounds[0] / 4, 50, text=str(self.scoreboard.score_left), font=("Arial", 30), fill="white")
        canvas.create_text(3 * screenBounds[0] / 4, 50, text=str(self.scoreboard.score_right), font=("Arial", 30),
                           fill="white")

    def update(self):
        for obj in self.objects:
            obj.update()

        ball = self.objects[2]
        left_paddle = self.objects[0]
        right_paddle = self.objects[1]

        # Collision detection with paddles
        if (left_paddle.x + left_paddle.width >= ball.x >= left_paddle.x and
                left_paddle.y + left_paddle.height >= ball.y >= left_paddle.y) or \
                (right_paddle.x <= ball.x + ball.width <= right_paddle.x + right_paddle.width and
                 right_paddle.y + right_paddle.height >= ball.y >= right_paddle.y):
            ball.x_speed = -ball.x_speed

        # Ball out of bounds
        if ball.x <= 0:
            self.scoreboard.increase_score_right()
            ball.reset()
        elif ball.x + ball.width >= screenBounds[0]:
            self.scoreboard.increase_score_left()
            ball.reset()

    def eventListener(self, e):
        if e.type == "2":
            match (e.keysym):
                case "w":
                    self.objects[0].UP = True
                case "s":
                    self.objects[0].DOWN = True
                case "Up":
                    self.objects[1].UP = True
                case "Down":
                    self.objects[1].DOWN = True

        elif e.type == "3":

            match (e.keysym):
                case "w":
                    self.objects[0].UP = False
                case "s":
                    self.objects[0].DOWN = False
                case "Up":
                    self.objects[1].UP = False
                case "Down":
                    self.objects[1].DOWN = False
