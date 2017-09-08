import random
from tkinter import *

class Cake:
    def __init__(self, canvas, x, y, w, h):
        self.canvas, self.x, self.y, self.w, self.h = canvas, x, y, w, h
        self.layers = random.randrange(2, 6)
        self.cakeColour = "#993322"
        self.fillColour = "#" + "".join(random.sample("0123456789abcdef", k=6))

    def draw(self):
        x = self.x + self.w / 10
        y = self.y + 3 * self.h / 4
        w = 4 * self.w / 5
        t = w / 10
        tf = c = w / 20
        h = 3 * w / 20

        for i in range(self.layers):
            # A bunch of magic
            self.canvas.create_oval(x, y + t, x + w, y + t + h, fill = self.cakeColour, outline = self.cakeColour)
            self.canvas.create_rectangle(x, y + h / 2, x + w, y + t + h /2, fill = self.cakeColour, outline = self.cakeColour)
            self.canvas.create_oval(x, y, x + w, y + h, fill = self.cakeColour, outline = self.cakeColour)
            y -= tf
            self.canvas.create_oval(x, y + tf, x + w, y + tf + h, fill = self.fillColour, outline = self.fillColour)
            self.canvas.create_rectangle(x, y + h / 2, x + w, y + tf + h / 2, fill = self.fillColour, outline = self.fillColour)
            self.canvas.create_oval(x, y, x + w, y + h, fill = self.fillColour)
            y -= t

        self.canvas.create_oval(x + w / 2 - c, y +c, x + w / 2 + c, y + 3 * c, fill = "red")

class Window:
    def __init__(self, root):
        self.root = root
        N_ROWS = 6
        N_COLS = 10
        W = 600
        H = 400
        self.root.title = "Cake"
        canvas = Canvas(self.root, width=W, height=H, bg="white")
        canvas.grid(column = 0, row = 0)

        cakes = []
        for i in range(N_ROWS):
            for j in range(N_COLS):
                cakes.append(Cake(canvas, j * W / N_COLS, i * H / N_ROWS, W / N_COLS, H / N_ROWS))
        for i in cakes: i.draw()

    def draw(self): self.root.mainloop()


w = Window(Tk())
w.draw()

