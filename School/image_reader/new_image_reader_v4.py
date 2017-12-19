import csv
from os import path
from PIL import Image
from PIL import ImageTk
from PIL import ExifTags
from tkinter import filedialog
import tkinter as tk

# Gets EXIF metadata in .jpg or .tiff images
def get_EXIF(img):
    return {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
    # This bit will never run, it's just an example of what gets output
    # If you comment out the first line you can then test without PIL using this
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


# Main Gui Class
class MainWindow():
    def __init__(self, root):
        # Define a bunch of elements
        # Using frame to make sure the image will be as big as everything else,
        #  just using grid wasn't working
        frame = tk.Frame(width=404, height=722)
        self.img_path = tk.Entry(frame, width=47) # Entry so it can scroll
        self.img_path.insert("end", "No Image File Selected")
        self.img_path.configure(state="disabled")
        self.img_button = tk.Button(frame, text="Select New Image", command=self._get_img_path)
        self.text = tk.Text(frame, height=40, width=50, relief="sunken", wrap="none")
        self.text.insert("end", "No data")
        self.text.configure(state="disabled")
        self.csv_path = tk.Entry(frame, width=47) # Entry so it can scroll
        self.csv_path.insert("end", "No CSV File Selected")
        self.csv_path.configure(state="disabled")
        self.csv_button = tk.Button(frame, text="Select New CSV File", command=self._get_csv_path)
        self.write_button = tk.Button(frame, text="Write Current Image Data to CSV File")
        # Make those elements show up
        self.img_path.grid(row=0, column=0, sticky="w")
        self.img_button.grid(row=0, column=1, sticky="e")
        self.text.grid(row=1, column=0, columnspan=2)
        self.csv_path.grid(row=2, column=0, sticky="w")
        self.csv_button.grid(row=2, column=1, sticky="e")
        self.write_button.grid(row=3, column=0, columnspan=2)
        frame.grid(row=0, column=0)
        # Define some more elements and place them
        self.img_label = tk.Label(root, text="Unable to read image")
        self.img_label.grid(row=0, column=1)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        # I know I could use just use "resizeable()", but I don't get to point
        #  out tkinter's inconsistentcies that way
        root.geometry("1126x722") # WWHHYYY is this a string
        root.minsize(1126, 722)   # See this one gets it right
        root.maxsize(1126, 722)
        # And move these to global vars now, just more conviennt not needing to
        #  type "self." for all the definitions
        self.root = root
        self.frame = frame
        self.csv = None
        self.draw()

    # I like having these as seperate functions, though it has no use here
    def draw(self): self.root.mainloop()
    def hide(self): self.root.withdraw()

    # Gets the path to the image file
    # I might have been able to get away with a single function for both files,
    #  but working out which button activates it is hard, and I need to do
    #  different things for each
    def _get_img_path(self):
        p = filedialog.askopenfilename()
        if path.isfile(p) and (p.endswith(".jpg") or p.endswith(".tiff")):
            # This bit is a great example of why tkinter is a mess
            # It's not hard to re-order inputs
            # And allowing the program to make changes when an widget is
            #  disabled is probably pretty easy too
            # But nope let's do it this way ¯\_(ツ)_/¯
            self.img_path.configure(state="normal")
            self.img_path.delete(0, "end")
            self.img_path.insert("end", p)
            self.img_path.configure(state="disabled")
            # Want to re-size the image so it fits properly
            self.img = Image.open(p)
            img = Image.open(p)
            w, h = img.size
            MAX_SIZE = 722 # It's square
            if w > h:
                h = int((h * MAX_SIZE) / w)
                w = MAX_SIZE
            elif w < h:
                w = int((w * MAX_SIZE) / h)
                h = MAX_SIZE
            elif w == h:
                w = h = MAX_SIZE
            # And actually displaying the image now
            img = ImageTk.PhotoImage(img.resize((w, h), Image.ANTIALIAS))
            self.img_label.configure(image=img)
            self.img_label.image = img # To prevent garbage collection eating it
            self._update_data()
        else:
            self.img_path.configure(state="normal")
            self.img_path.delete(0, "end")
            self.img_path.insert("end", "Invalid Path")
            self.img_path.configure(state="disabled")
            # Couldn't get the text to display again here, so I'll just leave
            #  the old image, it looks nicer than a massive empty square

    # Updates the text widget with current image data
    def _update_data(self):
        BLACKLIST = set(("XPAuthor", "ExifOffset"))
        data = ""
        exif = get_EXIF(self.img)
        # Want this in alphabetical order
        for key in sorted(list(exif.keys())):
            # Don't want anything on the blacklist, and anything that returns
            #  bytes is probably pretty useless too
            if key in BLACKLIST:
                continue
            if type(exif[key]) == bytes():
                continue
            data += str(key) + ": " + str(exif[key]) + "\n"
        self.text.configure(state="normal")
        # This needs "1.0" rather than "0" like entries or even just "1" WWHHYYY
        self.text.delete(1.0, "end")
        self.text.insert("end", data)
        self.text.configure(state="disabled")
        self.data = data

    def _get_csv_path(self):
        p = filedialog.askopenfilename()
        if path.isfile(p) and p.endswith(".csv"):
            self.csv_path.configure(state="normal")
            self.csv_path.delete(0, "end")
            self.csv_path.insert("end", p)
            self.csv_path.configure(state="disabled")
            self.csv = p
        else:
            self.csv_path.configure(state="normal")
            self.csv_path.delete(0, "end")
            self.csv_path.insert("end", "Invalid Path")
            self.csv_path.configure(state="disabled")

    # TODO: Convert to DictReader
    def _write_to_csv(): # TODO: Make this not break horribly on an empty file
        # First get some data from the file
        with csv.reader(open(self.csv, "r")) as csv_file:
            header = next(csv_file)
            new_entries = 0
            for i in self.data:
                if not i in header:
                    header.append(i)
                    new_entries += 1
            # If we have a new entry we need to re-create the whole file, so we
            #  need to get all current data first
            if new_entries > 0:
                csv_data = []
                for row in csv_file:
                    # Add empty strings so that we have the right amount of data
                    csv_data.append(row + ["" for _ in range(new_entries)])
        if new_entries > 0:
            with csv.writer(open(self.csv, "w"), fieldname=header) as csv_file:
                 csv_file.writeheader()
                 
        else:
            # Here we can just append the new entry
            with csv.DictWriter(open(self.csv, "a"), fieldname=header) as csv_file:
                csv_file.writerow(self.data)

a = MainWindow(tk.Tk())
a.draw()