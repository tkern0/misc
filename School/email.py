import re
from tkinter import *

def check_valid_email(string):
    return not re.search("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", string) == None

class Window():
    def __init__(self, root):
        # There has to be a better way than this
        self.root = root
        self.root.resizable(width=False, height=False)
        self.root.geometry('140x140')
        self.output = {"Name": StringVar(), "Email": StringVar()}
        self.label_name = Label(self.root, text = "Name")
        self.label_name.pack()
        self.entry_name = Entry(self.root, textvariable=self.output["Name"])
        self.entry_name.pack()
        self.label_email = Label(self.root, text = "Email")
        self.label_email.pack()
        self.entry_email = Entry(self.root, textvariable=self.output["Email"])
        self.entry_email.pack()
        self.button = Button(self.root, text="Submit", command=self.submit)
        self.button.pack()
        self.label_error = Label(self.root, fg="red", text="")

    def submit(self):
        self.error_text = ""
        self.label_error.pack_forget()
        if not self.output["Name"].get():
            self.error_text += "\nPlease enter a Name"
        if not check_valid_email(self.output["Email"].get()):
            self.error_text += "\nPlease enter a valid Email"
        if not self.error_text == "":
            self.label_error = Label(self.root, fg="red", text=self.error_text[1:])
            self.label_error.pack()
        else:
            print("Name:", self.output["Name"].get())
            print("Email:", self.output["Email"].get())

    def draw(self): self.root.mainloop()


a = Window(Tk())
a.draw()