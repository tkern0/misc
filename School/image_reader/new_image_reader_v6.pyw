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
        # Using frame because the save/write csv file buttons shouldn't resize
        #  this set of widgets
        frame = tk.Frame(width=404, height=722)
        self.img_path = tk.Entry(frame, width=47) # Entry so it can scroll
        self.img_path.insert("end", "No image selected")
        self.img_path.configure(state="disabled")
        self.img_button = tk.Button(frame, text="Select new image", command=self._get_img_path)
        self.text = tk.Text(frame, height=40, width=50, relief="sunken", wrap="none")
        self.text.insert("end", "No data")
        self.text.configure(state="disabled")
        self.csv_path = tk.Entry(frame, width=47) # Entry so it can scroll
        self.csv_path.insert("end", "No CSV file selected")
        self.csv_path.configure(state="disabled")
        self.csv_button = tk.Button(frame, text="Select new CSV file", command=self._get_csv_path)
        # Make those elements show up
        self.img_path.grid(row=0, column=0, sticky="w")
        self.img_button.grid(row=0, column=1, sticky="e")
        self.text.grid(row=1, column=0, columnspan=2)
        self.csv_path.grid(row=2, column=0, sticky="w")
        self.csv_button.grid(row=2, column=1, sticky="e")
        # Define some more elements
        self.save_as_button = tk.Button(root, text="Save as new CSV file", command=self._write_to_new_csv)
        self.write_button = tk.Button(root, text="Write to current CSV file", command=self._write_to_existing_csv)
        self.img_label = tk.Label(root, text="No image selected")
        self.img = None
        # Place everything
        frame.grid(row=0, column=0, columnspan=2)
        self.save_as_button.grid(row=1, column=0)
        self.write_button.grid(row=1, column=1)
        self.img_label.grid(row=0, column=2, rowspan=2)
        root.grid_columnconfigure(2, weight=1)
        root.geometry("1126x722") # WWHHYYY is this a string
        root.resizable(width=False, height=False)
        # And move these to global vars now, just more conviennt not needing to
        #  type "self." for all the definitions above
        self.root = root
        self.frame = frame
        self.csv = None
        self.draw()

    # I like having these as seperate functions, though it has no use here
    def draw(self): self.root.mainloop()
    def hide(self): self.root.withdraw()

    # Gets the path to the image file
    def _get_img_path(self):
        i_path = filedialog.askopenfilename(filetypes=(("jpeg files", "*.jpg"), ("tiff files","*.tiff")), defaultextension=".jpg")
        if not path.isfile(i_path):
            return
        # This bit is a great example of why tkinter is a mess
        # It's not hard to re-order inputs
        # And allowing the program to make changes when an widget is
        #  disabled is probably pretty easy too
        # But nope let's do it this way ¯\_(ツ)_/¯
        self.img_path.configure(state="normal")
        self.img_path.delete(0, "end")
        self.img_path.insert("end", i_path)
        self.img_path.configure(state="disabled")
        # Want to re-size the image so it fits properly
        self.img = Image.open(i_path)
        img = Image.open(i_path)
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

    # Updates the text widget with current image data
    def _update_data(self):
        BLACKLIST = set(("XPAuthor", "ExifOffset"))
        data = ""
        exif = get_EXIF(self.img)
        clean_exif = {}
        # Want this in alphabetical order
        for key in sorted(list(exif.keys())):
            # Don't want anything on the blacklist, and anything that returns
            #  bytes is probably pretty useless too
            if key in BLACKLIST:
                continue
            if type(exif[key]) == bytes():
                continue
            data += str(key) + ": " + str(exif[key]) + "\n"
            clean_exif[key] = exif[key]
        self.text.configure(state="normal")
        # This needs "1.0" rather than "0" like entries or even just "1" WWHHYYY
        self.text.delete(1.0, "end")
        self.text.insert("end", data)
        self.text.configure(state="disabled")
        # Finally add the filename to "clean_exif" and make it global
        clean_exif["Filename"] = path.basename(self.img_path.get())
        self.exif = clean_exif

    # Gets the path to the csv file
    def _get_csv_path(self, save_file=False):
        # This function gets run for both opening and saving a file, so we need
        #  to differentiate between them and run the relevant file dialouge
        if save_file:
            c_path = filedialog.asksaveasfilename(filetypes=(("csv files", "*.csv"),), defaultextension=".csv")
        else:
            c_path = filedialog.askopenfilename(filetypes=(("csv files", "*.csv"),), defaultextension=".csv")
        self.csv_path.configure(state="normal")
        self.csv_path.delete(0, "end")
        self.csv_path.insert("end", c_path)
        self.csv_path.configure(state="disabled")
        self.csv = c_path

    # Pretty easy when the file doesn't exist yet
    def _write_to_new_csv(self, get_path=True):
        # If there is no image defined we don't want this to do anything
        if not self.img:
            return
        # If we come here from the other button we don't need to ask for a file
        #  path, the user already selected it
        if get_path:
            self._get_csv_path(save_file=True)
        self._update_data() # Just in case
        # We want filename first in the header, but the rest should be in
        #  alphabetical order
        header = ["Filename"]
        entries = list(self.exif.keys())
        entries.remove("Filename")
        header += sorted(entries)
        if not path.isfile(self.csv):
            return
        # Setting newline here just prevents blanks in the raw csv file
        # Shouldn't really matter if you import into excel or similar, but it's
        #  a simple fix anyway
        w_file = open(self.csv, "w", newline='')
        csv_file = csv.DictWriter(w_file, fieldnames=header)
        csv_file.writeheader()
        csv_file.writerow(self.exif)
        w_file.close()

    # This one's a bit more complex
    def _write_to_existing_csv(self):
        # If there is no image defined we don't want this to do anything
        if not self.img:
            return
        # If we don't have a csv file selected we don't want to do anything
        if not self.csv:
            return
        # Check if the csv file should be handled by the other function
        # If the file does not exist 'path.getsize()' errors
        # We want both an empty file and a non-existant one to get treated the
        #  same, so if we catch the error we set size to 0
        try:
            size = path.getsize(self.csv)
        except OSError:
            size = 0
        if size == 0:
            # User already selected the path, no need to do it again
            self._write_to_new_csv(get_path=False)
            return
        # Get the header
        r_file = open(self.csv, "r", newline='')
        for row in csv.reader(r_file): # This is really messy
            header = row
            break
        # Now we check if the header covers all entries we have data for
        new_entries = 0
        new_header = []
        for i in self.exif:
            if not i in header:
                new_header.append(i)
                new_entries += 1
        # We don't want to change the order of what already exists in the
        #  header, but we can alphabeticalise the new stuff
        header += sorted(new_header)
        r_file.seek(0) # Idk if this is necessary, but to be safe
        csv_file = csv.DictReader(r_file)
        csv_data = []
        for row in csv_file:
            csv_data.append(row)
        # Now we wipe the file and re-create it
        r_file.close()
        w_file = open(self.csv, "w", newline='')
        csv_file = csv.DictWriter(w_file, fieldnames=header)
        csv_file.writeheader()
        for row in csv_data:
           csv_file.writerow(row)
        csv_file.writerow(self.exif)
        w_file.close()

a = MainWindow(tk.Tk())