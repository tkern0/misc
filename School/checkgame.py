from random import randrange
from tkinter import *

class MainWindow():
    def __init__(self, root, W=10, H=16):
        self.W, self.H = W, H
        self.root = root
        self.root.title = "Game"
        self.canvas = Canvas(root, width=self.W*30, height=self.H*30, bg="white")
        self.canvas.grid(column = 0, row = 0)
        self.boxes = {}
        self.box_vars = {(x, y):IntVar(0) for x in range(self.W) for y in range(self.H)}
        self.trace_vars = {}
        for y in range(self.H):
            for x in range(self.W):
                self.boxes[(x, y)] = Checkbutton(self.canvas, variable=self.box_vars[(x, y)])
                self.boxes[(x, y)].grid(column=x, row=y)
        self.reset_button = Button(self.root, text="Reset", command=self.randomize_board)
        self.reset_button.grid()
        self.randomize_board()

    def randomize_board(self):
        for box in self.trace_vars:
            self.box_vars[box].trace_vdelete("w", self.trace_vars[box])
        for _ in range(self.W * self.H * 2):
            x, y = randrange(self.W), randrange(self.H)
            if (x, y) not in self.box_vars:
                print(x, y)
            for coord in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y -1)):
                if coord in self.box_vars:
                    self.box_vars[coord].set(1 - self.box_vars[coord].get())
        for box in self.box_vars:
            self.trace_vars[box] = self.box_vars[box].trace("w",
                                    lambda a,b,c, box=box: self.update_squares(box))

    def draw(self): self.root.mainloop()

    def update_squares(self, coords):
        x, y = coords
        l_coords = ((x, y), (x + 1, y), (x - 1, y), (x, y + 1), (x, y -1))
        for coord in l_coords:
            if coord in self.box_vars:
                self.box_vars[coord].trace_vdelete("w", self.trace_vars[coord])
                self.box_vars[coord].set(1 - self.box_vars[coord].get())
                self.trace_vars[coord] = self.box_vars[coord].trace("w",
                                    lambda a,b,c, coord=coord: self.update_squares(coord))
        all_on, all_off = True, True
        for coord in self.box_vars:
            if self.box_vars[coord].get() == 0: all_on= False
            elif self.box_vars[coord].get() == 1: all_off = False
        if all_on or all_off:
            self.child = WinWindow(Tk())
            self.child.draw()

class WinWindow():
    def __init__(self, root):
        self.root = root
        self.root.title = "You Win!"
        self.label = Label(self.root, text = "You Win!")
        self.label.pack()
        self.button = Button(self.root, text="Close", command=self.root.destroy)
        self.button.pack()

    def draw(self): self.root.mainloop()


a = MainWindow(Tk())
a.draw()