from os import path
from tkinter import filedialog
# from PIL import Image
# from PIL import ImageTk
# from PIL import ExifTags
import tkinter as tk

def get_EXIF(path):
    img = Image.open(path)
    exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
    # return exif
    return {"DateTime": "2009:03:12 13:47:43",
            "Rating": 3,
            "Copyright": "Microsoft Corporation",
            "RatingPercent": 50,
            "Artist": "Corbis",
            "XPAuthor": b"MM\x00*\x00\x00\x00\x08\x00\x06\x12\x00\x02",
            "ExifOffset": 106,
            "SubsecTimeOrignal": 54,
            "SubsecTimeDigitized": 54,
            "DateTimeOriginal": "2008:03:14 13:59:26",
            "DateTimeDigitized": "2008:03:14 13:59:26"}


class MainWindow():
    def __init__(self, root):
        self.img_path = StringVar()
        self.csv_path = StringVar()
        self.img_path.set("No File Selected")
        self.csv_path.set("No File Selected")
        frame = Frame()
        widgets = [tk.Label(frame, text=self.img_path.get()),
                   tk.Button(frame, text="Select New Image", command=self._get_img_path),
                   tk.Label(frame, text=self.csv_path.get()),
                   tk.Button(frame, text="Select New CSV File", command=self._get_csv_path)]
        self.text =tk.Text(frame, height=30, width=40, relief="sunken", wrap="none")
        self.text.insert("end", "No data")
        self.text.configure(state="disabled")
        widgets[0].grid(row=0, column=0)
        widgets[1].grid(row=0, column=1)
        self.text.grid(row=1, column=0, columnspan=2)
        widgets[2].grid(row=2, column=0)
        widgets[3].grid(row=2, column=1)
        frame.grid(row=0, column=0)
        # self.img = ImageTk.PhotoImage()
        # self.img = PhotoImage(file="\\\\DataServer2\\TKern$\\2017\\Python\\image_reader\\Chrysanthemum.gif")
        self.img = None
        self.img_label = Label(root, text="Unable to read image", image=self.img) #, width=536, height=536)
        self.img_label.grid(row=0, column=1)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.resizable(width=False, height=False)
        root.geometry("860x536")
        self.root = root
        self.frame = frame
        self.widgets = widgets


    def draw(self): self.root.mainloop()
    def hide(self): self.root.withdraw()

    def _get_img_path(self):
        p = filedialog.askopenfilename()
        if path.isfile(p):
            self.img_path.set(p)
        else:
            self.img_path.set("Invalid path")

    def _get_csv_path(self):
        p = filedialog.askopenfilename()
        if path.isfile(p) and p[-4:]==".csv":
            self.csv_path.set(p)
        else:
            self.csv_path.set("Invalid path")
a = MainWindow(tk.Tk())
a.draw()