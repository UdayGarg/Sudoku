from PIL import Image, ImageFont, ImageDraw, ImageEnhance

source_img = Image.open("demo.png").convert("RGBA")

draw = ImageDraw.Draw(source_img)
draw.rectangle(((50,50), (400, 400)), fill = "black")
draw.text((300,300), "3", font=ImageFont.load_default())

source_img.save("output1.png")
