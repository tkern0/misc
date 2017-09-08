from tkinter import *

class MainWindow():
    def __init__(self, root):
        self.root = root
        self.canvases = [Canvas(root, width=100, height=100, bg="lightgrey" if i%2==0 else "grey") for i in range(9)]
        for i in range(len(self.canvases)):
            self.canvases[i].grid(row=i%3, column=int(i/3))
        self.label = Label(text="X's Turn")
        self.label.grid(column=1)
        self.button = Button(root, text="Reset", command=self.reset_board)
        self.button.grid(row=3, column=2, sticky="E")
        self.reset_board()

    def draw(self): self.root.mainloop()
    def hide(self): self.root.withdraw()

    def select_square(self, event):
        if not event.widget.contains:
            event.widget.contains = ("O", "X")[self.X_turn]
            event.widget.create_text(50, 50, text=("O", "X")[self.X_turn], font=("", 100))
            self.X_turn = not self.X_turn
            self.full_squares += 1
            self.update_text()

    def update_text(self):
        gameover = ""
        winlines = ((0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontal
                    (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertical
                    (0, 4, 8), (2, 4, 6))            # Diagonal
        for row in winlines:
            if self.canvases[row[0]].contains == self.canvases[row[1]].contains\
               and self.canvases[row[1]].contains == self.canvases[row[2]].contains\
               and self.canvases[row[0]].contains:
                gameover = self.canvases[row[0]].contains
                break
        if gameover:
            self.label.configure(text=gameover + " Wins!")
            for i in self.canvases:
                i.unbind("<Button-1>")
        elif self.full_squares == 9:
            self.label.configure(text="Draw")
        else:
          self.label.configure(text=("O's Turn", "X's Turn")[self.X_turn])

    def reset_board(self):
        self.X_turn = True
        self.full_squares = 0
        for i in self.canvases:
            i.delete("all")
            i.contains = ""
            i.bind("<Button-1>", self.select_square)
        self.label.configure(text="X's Turn")

a = MainWindow(Tk())
a.draw()