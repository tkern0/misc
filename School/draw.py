from tkinter import *

GRID_SIZE = 51
SQUARE_SIZE = 15

class MainWindow():
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(self.root, width=GRID_SIZE * SQUARE_SIZE, height=GRID_SIZE * SQUARE_SIZE)
        self.boxes = {}
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                self.boxes[(x, y)] = self.canvas.create_rectangle(x * SQUARE_SIZE, y * SQUARE_SIZE, (x * SQUARE_SIZE) + SQUARE_SIZE, (y * SQUARE_SIZE) + SQUARE_SIZE, fill="#e0e0e0")
        self.x, self.y = GRID_SIZE>>1, GRID_SIZE>>1 # Middle of grid
        self.canvas.itemconfig(self.boxes[(self.x, self.y)], fill="red")
        self.root.bind("<Up>", self.move_square)
        self.root.bind("<Down>", self.move_square)
        self.root.bind("<Left>", self.move_square)
        self.root.bind("<Right>", self.move_square)
        self.root.bind("<Button-1>", self.move_square)
        self.canvas.pack()

    def draw(self): self.root.mainloop()
    def hide(self): self.root.withdraw()

    def move_square(self, event):
        if event.type == "2": # Keypress
            if event.keycode == 37: # L
                nx, ny = self.x - 1, self.y
            elif event.keycode == 38: # U
                nx, ny = self.x, self.y - 1
            elif event.keycode == 39: # R
                nx, ny = self.x + 1, self.y
            elif event.keycode == 40: # D
                nx, ny = self.x, self.y + 1
        elif event.type == "4": # Mouse
            nx, ny = int(int(event.x)/SQUARE_SIZE), int(int(event.y)/SQUARE_SIZE)
        if (nx, ny) not in self.boxes:
            nx, ny = self.x, self.y
        self.canvas.itemconfig(self.boxes[(self.x, self.y)], fill="darkgrey")
        self.canvas.itemconfig(self.boxes[(nx, ny)], fill="red")
        self.x, self.y = nx, ny

a = MainWindow(Tk())
a.draw()