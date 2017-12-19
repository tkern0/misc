import re

class ImageReader:
    def __init__(self, path):
        with open(path, "rb") as f:
            self.data = re.search(b"\xff\xd8(.*?)\xff\xda", f.read(), flags=re.S).group(1)

    def get_data(self): return self.data

    def get_JFIF(self):
        return re.search(b"\xff\xe0(..)JFIF(.+?)\xff", self.data, flags=re.S)

    def get_EXIF(self):
        self.exif = re.search(b"\xff\xe1(?P<size>..)Exif\x00\x00(?P<align>[MI]{2})..(?P<IFD>....)(.+?)\xff", self.data, flags=re.S)
        # align II means 0x2a00 -> 0x2a 0x00, MM means 0x2a00 -> 0x00 0x2a
        # IFD: b"(?P<size>..)"
        # IFD entry: b"(?P<num>..)(?P<type>..)(?P<components>....)(?P<data>....)"
        # IFD end: B"(?P<IFD>....)"

test = ImageReader("C:\\Users\\Public\\Pictures\\Sample Pictures\\Desert.jpg")
print(test.get_data())
# a = test.get_JFIF()
# if a:
#     print("JFIF:", a.groups())
a = test.get_EXIF()
if a:
    print("EXIF:", a.groups())