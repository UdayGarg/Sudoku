from PIL import Image, ImageFont, ImageDraw, ImageEnhance

source_img = Image.open("demo.png").convert("RGBA")
fontsize = 5
draw = ImageDraw.Draw(source_img)
draw.rectangle(((10,10), (60, 60)), outline="black", width = 2)
font = ImageFont.truetype("Ubuntu-R.ttf", 25)
draw.text((20,20), "3",fill=(0,0,0), font=font)

source_img.save("output1.png")
