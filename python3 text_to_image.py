from PIL import Image, ImageDraw

img = image.new("RGB", (100, 30), color = 'red')

d = ImageDraw.Draw(img)
img.save('PIL_red.png')

