from PIL import Image, ImageFont, ImageDraw, ImageEnhance
from random import randint

source_img = Image.open("demo.png").convert("RGBA")
fontsize = 40
draw = ImageDraw.Draw(source_img)
draw.rectangle(((10,10), (60, 60)), outline="black", width = 6)
font = ImageFont.truetype("Ubuntu-R.ttf", fontsize)
draw.text((15,15), "9",fill=(0,0,0), font=font)
width = randint(0,10)
height = randint(11,100)
filename = "grid-{}-{}.png".format(width, height)
print("Saving {}".format(filename))
source_img.save(filename)
