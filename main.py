import tkinter as tk
import time
from data import screenBounds
from gameobjects.objectmanager import ObjManager


def main():
    window = tk.Tk(screenName="PONG")
    window.title("PONG")

    canvas = tk.Canvas(window, background="#000",
                       width=str(screenBounds[0]), height=str(screenBounds[1]))
    canvas.pack()

    mng = ObjManager()

    def handleEvent(e):
        mng.eventListener(e)

    window.bind("<KeyPress>", handleEvent)
    window.bind("<KeyRelease>", handleEvent)

    # Start game loop

    spf = 1/60
    lastLoop = time.time()

    while True:

        now = time.time()

        if now - lastLoop >= spf:

            mng.update()
            mng.render(canvas)

            now = lastLoop

        window.update()


if __name__ == "__main__":
    main()
