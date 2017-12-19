from tkinter import *

SQUARE_SIZE = 25

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(self.root, width= 9 * SQUARE_SIZE, height= 9 * SQUARE_SIZE)
        self.boxes = {}
        for y in range(9):
            for x in range(9):
                self.boxes[(x, y)] = self.canvas.create_rectangle(x * SQUARE_SIZE, y * SQUARE_SIZE, (x * SQUARE_SIZE) + SQUARE_SIZE, (y * SQUARE_SIZE) + SQUARE_SIZE, fill="#e0e0e0")
        self.buttons = []
        self.frames = [Frame() for _ in range(4)]
        for i in range(9):
            self.buttons.append(Button(self.frames[0], text="v", command=lambda: self.shoot_grid(i, "v")))
        for i in range(9):
            self.buttons.append(Button(self.frames[1], text=">", command=lambda: self.shoot_grid(i, ">")))
        for i in range(9):
            self.buttons.append(Button(self.frames[2], text="^", command=lambda: self.shoot_grid(i, "^")))
        for i in range(9):
            self.buttons.append(Button(self.frames[3], text="<", command=lambda: self.shoot_grid(i, "<")))
        for i in range(9):
            self.buttons[i].grid(row=0, column=i)
        for i in range(9,18):
            self.buttons[i].grid(row=i-9, column=0)
        for i in range(18,27):
            self.buttons[i].grid(row=10, column=i-18)
        for i in range(27,36):
            self.buttons[i].grid(row=i-27, column=10)
        self.frames[0].grid(row=0, column=1)
        self.frames[1].grid(row=1, column=0)
        self.frames[2].grid(row=2, column=1)
        self.frames[3].grid(row=1, column=2)
        self.canvas.grid(row=1, column=1)

    def draw(self): self.root.mainloop()
    def hide(self): self.root.withdraw()

    def shoot_grid(self, button, b_type):
        pass

a = MainWindow(Tk())
a.draw()