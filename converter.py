from PIL import Image
import pyheif
from tkinter import filedialog
import os.path
import tkinter
# heif_file = pyheif.read("IMG_0132.HEIC")
# image = Image.frombytes(
#     heif_file.mode, 
#     heif_file.size, 
#     heif_file.data,
#     "raw",
#     heif_file.mode,
#     heif_file.stride,
#     )

# image.save("IMG_0132.jpg", "JPEG")
root = tkinter.Tk()
root.withdraw()
paths = filedialog.askopenfilenames()

print(paths)

for path in paths:
    heif_file = pyheif.read(path)
    # print(os.path.basename(path))
    image = Image.frombytes(
    heif_file.mode, 
    heif_file.size, 
    heif_file.data,
    "raw",
    heif_file.mode,
    heif_file.stride,
    )
    # print(os.path.splitext(os.path.basename(path))[0])
    image.save(os.path.splitext(os.path.basename(path))[0] + ".jpg", "JPEG")


