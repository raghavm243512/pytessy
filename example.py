from pytessy import PyTessy # assuming that it is the same folder or installed with pip
import cv2
from PIL import Image

reader = PyTessy(language='eng', oem=2, psm=11) # other options only needed for file paths for installation

# for opencv
img = cv2.imread('example.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # while the software can handle color, typically the best OCR results come from black on white images
# ...
# ... any type of processing needed for OCR, usually some expansion, opening, etc.
# ... 
string = reader.read(img.tobytes(), img.shape[1], img.shape[0], 1) # the last parameter is bits used per pixel. For grayscale, this is 1, for RGB, it should be 3 (Although for opencv, BGR should first be made RGB)

# for PIL
img = Image.open('example.jpg')
# apply any desired processing
imgbytes = img.tobytes()
depth = int(len(imgbytes) / (img.width * img.height)) # example calculation, will still be 1 for grayscale
string = reader.read(imgbytes, img.width, img.height, depth, raw=True, resolution=100) # raw text reading and resolution can be set in both cases, shown here for example
