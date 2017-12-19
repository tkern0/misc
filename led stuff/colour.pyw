from wrapper import *
from tkinter import *

LED = LEDControler()

class ColourGui:
    def __init__(self, root):
        self.root = root
        self.elements = [Frame(root, width=300, height=300, bg="grey"),
                         Label(root, text="What colour would you like?"),
                         Entry(root, width=14),
                         Button(root, text="Go", command=self.set_colour),
                         Label(root, text="Red"),
                         Scale(root, orient=HORIZONTAL, to=255, length=255,
                               command=self.set_colour),
                         Label(root, text="Green"),
                         Scale(root, orient=HORIZONTAL, to=255, length=255,
                               command=self.set_colour),
                         Label(root, text="Blue"),
                         Scale(root, orient=HORIZONTAL, to=255, length=255,
                               command=self.set_colour)]
        self.elements[0].grid(columnspan=3)
        self.elements[1].grid()
        self.elements[2].grid(row=1, column=1)
        self.elements[3].grid(row=1, column=2)
        self.elements[4].grid(row=2, column=2)
        self.elements[5].grid(row=2, column=0, columnspan=2)
        self.elements[6].grid(row=3, column=2)
        self.elements[7].grid(row=3, column=0, columnspan=2)
        self.elements[8].grid(row=4, column=2)
        self.elements[9].grid(row=4, column=0, columnspan=2)

        self.elements[2].bind("<Return>", lambda x: self.set_colour())
        self.elements[5].set(192)
        self.elements[7].set(192)
        self.elements[9].set(192)

    def draw(self): self.root.mainloop()
    def hide(self): self.root.withdraw()

    def set_colour(self, *args):
        colour = self.elements[2].get()
        if args:
            colour = "#" + str(format(self.elements[5].get(), "x")).zfill(2)\
                         + str(format(self.elements[7].get(), "x")).zfill(2)\
                         + str(format(self.elements[9].get(), "x")).zfill(2)
            self.elements[2].delete(0, END)
            self.elements[2].insert(0, colour)
        try:
            self.elements[0].configure(bg=colour)
        except TclError:
            self.elements[0].configure(bg="#c0c0c0")
        self.fix_scale()
        self.colour_mouse()

    def get_colour(self): # breaks when bg = ""
        colour = self.elements[0]["bg"]
        if not colour: colour="#c0c0c0"
        rgb = self.root.winfo_rgb(colour)
        return rgb[0]>>8, rgb[1]>>8, rgb[2]>>8

    def fix_scale(self):
        r, b, g = self.get_colour()
        self.elements[5].set(r)
        self.elements[7].set(b)
        self.elements[9].set(g)

    def colour_mouse(self):
        r, b, g = self.get_colour()
        LED.set_colour("M", dec_to_percent(r),
                            dec_to_percent(b),
                            dec_to_percent(g))


ColourGui(Tk()).draw()