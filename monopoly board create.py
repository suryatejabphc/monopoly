import math
from PIL import Image, Image Draw

w,h = 200, 200
shape = [(40,40),(w-10,h-10)]

#create new image file
img = Image.new("RGB",(w,h))

img1 = ImageDraw.Draw(img)
img1.rectangle(shape, fill = "#000000",outline = "blue")
img.show
