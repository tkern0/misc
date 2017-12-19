from fractions import Fraction as Frac
import re
import struct

# Converts the format value in IFD tables into chars for struct.unpack()
# 5 and 10 are special and need their own processing first
# Also stores bytes per component for each format
FORMAT_CONVERT = {1:  ("B", 1),   # Unsigned byte
                  2:  ("c", 1),   # ASCII string
                  3:  ("H", 2),   # Unsigned short
                  4:  ("L", 4),   # Unsigned long
                  5:  ("L_f", 8), # Unsigned fraction
                  7:  ("B", 1),   # Unknown (?) treat as unsigned byte
                  6:  ("b", 1),   # Signed byte
                  8:  ("h", 2),   # Signed short
                  9:  ("l", 4),   # Signed long
                  10: ("l_f", 8), # Signed fraction
                  11: ("f", 4),   # Float
                  12: ("d", 8)}   # Double

# Converts hex IFD tags into their name as a string
TAG_CONVERT = {b"\x01\x00": "Image Width",
               b"\x01\x01": "Image Height",
               b"\x01\x02": "Bits per Sample",
               b"\x01\x03": "Compression",
               b"\x01\x06": "Photometric Interpretation",
               b"\x01\x0e": "Image Description",
               b"\x01\x0f": "Manufacturer",
               b"\x01\x10": "Model",
               b"\x01\x11": "Strip Offsets",
               b"\x01\x12": "Orientation",
               b"\x01\x15": "Samples per Pixel",
               b"\x01\x16": "Rows per Strip",
               b"\x01\x17": "Strip Byte Counts",
               b"\x01\x1a": "X Resolution",
               b"\x01\x1b": "Y Resolution",
               b"\x01\x1c": "Planar Configuration",
               b"\x01\x2d": "Transfer Function",
               b"\x01\x28": "Resolution Unit",
               b"\x01\x31": "Software",
               b"\x01\x32": "Date Time",
               b"\x01\x3b": "Artist",
               b"\x01\x3e": "White Point",
               b"\x01\x3f": "Primary Chromaticities",
               b"\x02\x01": "Thumbnail SOI",
               b"\x02\x02": "Thumbnail Length",
               b"\x02\x11": "YCbCr Coefficients",
               b"\x02\x12": "YCbCr Sub-Sampling",
               b"\x02\x13": "YCbCr Positioning",
               b"\x02\x14": "Reference Black White",
               b"\x82\x98": "Copyright",
               b"\x87\x69": "EXIF IFD Pointer",
               b"\x88\x25": "GPS Info IFD Pointer",
               b"\x90\x00": "EXIF Version",
               b"\x90\x03": "Date Time Original",
               b"\x90\x04": "Date Time Digitized",
               b"\x91\x01": "Components Configuration",
               b"\x91\x02": "Compressed Bits per Pixel",
               b"\x92\x7c": "Maker Note",
               b"\x92\x86": "User Comment",
               b"\x92\x90": "Sub-Sec Time",
               b"\x92\x91": "Sub-Sec Time Original",
               b"\x92\x92": "Sub-Sec Time Digitized",
               b"\xa0\x00": "Flashpix Version",
               b"\xa0\x01": "Colourspace",
               b"\xa0\x02": "Pixel X Dimention",
               b"\xa0\x03": "Pixel Y Dimention",
               b"\xa0\x04": "Related Sound File",
               b"\xa0\x05": "Interoperability IFD Pointer",
               b"\xa4\x20": "Image Unique ID"}

# Makes sure program won't crash with invalid key
# Used for TAG_CONVERT
def dict_get_safe(dictionary, key, default=None):
    if not default:
        default = key
    if not key in dictionary:
        return default
    return dictionary[key]

# Converts bytes, taking endianness into account
# Tries to assume input type if not specified
def c_byte(byte, E, typ=None):
    if not typ:
        typ = {1:"B", 2:"H", 4:"I"}[len(byte)]
    if not typ: raise ValueError # Unknown type
    return struct.unpack(E + typ, byte)[0]

# Converts multiple bytes, taking endianness into account
# Input type must be specified
# Input must contain a whole number of types
def m_byte(byte, E, typ):
    num = int(len(byte)/struct.calcsize(typ))
    result = struct.unpack(E + typ*num, byte)
    if typ == "c":
        return "".join([i.decode("ascii") for i in result])
    else:
        return result

# Because I couldn't install Pillow
# Reads .jpg files and extracts data about the images
class ImageReader:
    def __init__(self, path):
        with open(path, "rb") as f:
            self.data = re.search(b"\xff\xd8(.+?)\xff\xd9", f.read(), flags=re.S).group(1)
            self.JFIF = re.search(b"\xff\xe0(..)JFIF(.+?)\xff", self.data, flags=re.S)
            self.EXIF = re.search(b"\xff\xe1(?P<size>..)Exif\x00\x00(?P<align>MM|II)..(?P<IFD>....)", self.data, flags=re.S)
        self.tags = {}
        # No need to run one of these functions if the image file doesn't have
        #  that type of data encoded
        # Issues might occur if the two types contain different information, but
        #  that (hopefully) should never happen in practice
        if self.JFIF:
            self.get_JFIF()
        if self.EXIF:
            self.get_EXIF()

    def get_JFIF(self):
        return self.JFIF # TODO: whole formatting type

    def get_EXIF(self):
        # Endianness. Yes it changes.
        E = {b"II":"<", b"MM":">"}[self.EXIF.group("align")]
        # No need to process over the whole file anytime you want to check stuff
        E_DATA = self.data[self.EXIF.start("align"):c_byte(self.EXIF.group("size"), E)]
        ifd = c_byte(self.EXIF.group("IFD"), E)
        while not ifd == 0:
            entries = c_byte(E_DATA[ifd:ifd + 2], E)
            to_check = {}
            for i in range(entries):
                c_row = E_DATA[(ifd + 2) + (i * 12):(ifd + 2) + (i * 12) + 12]
                tag =    dict_get_safe(TAG_CONVERT, c_row[0:2])
                form = FORMAT_CONVERT[c_byte(c_row[2:4], E)]
                num =    c_byte(c_row[4:8], E)
                if num * form[1] < 4:
                    # This will never be a fraction so we don't need to worry
                    #  about them here
                    self.tags[tag] = m_byte(c_row[8:12], E, form[0])[:num]
                else:
                    to_check[c_byte(c_row[8:12], E)] = (form[0], form[1] * num, tag)
            for i in to_check:
                c_val = to_check[i]
                if c_val[0].endswith("_f"):
                    all_vals = []
                    for j in range(0, c_val[1], 8):
                        n = c_byte(E_DATA[i + j    :i + j + 4], E, c_val[0][:1])
                        d = c_byte(E_DATA[i + j + 4:i + j + 8], E, c_val[0][:1])
                        all_vals.append(Frac(n, d))
                    self.tags[dict_get_safe(TAG_CONVERT, c_val[2])] = tuple(all_vals)
                else:
                    self.tags[c_val[2]] = m_byte(E_DATA[i:i + c_val[1]], E, c_val[0])
            f_pos = (ifd + 2) + (12 * entries)
            ifd = c_byte(E_DATA[f_pos:f_pos + 4], E)
        self._fix_tags()

    # Removes single item tuples
    def _fix_tags(self):
        for i in self.tags:
            if len(self.tags[i]) == 1:
                self.tags[i] = self.tags[i][0]

test = ImageReader("C:\\Users\\Public\\Pictures\\Sample Pictures\\Desert.jpg")
# print(test.get_data())
# a = test.get_JFIF()
# if a:
#     print("JFIF:", a.groups())
test.get_EXIF()
print(test.tags.keys())
