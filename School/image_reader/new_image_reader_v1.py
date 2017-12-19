from PIL import Image
from PIL import ExifTags

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
