import tkinter as tk
from data import screenBounds
from .objects import Paddle


class ObjManager:
    def __init__(self):
        self.objects = []
        self.objects.append(Paddle(50, (screenBounds[1] - Paddle.height)/2))
        self.objects.append(
            Paddle(screenBounds[0] - 50 - Paddle.width, (screenBounds[1] - Paddle.height)/2))

    def render(self, canvas: tk.Canvas):
        canvas.delete("all")

        for obj in self.objects:
            obj.render(canvas)

    def update(self):
        for obj in self.objects:
            obj.update()

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
