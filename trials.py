import functions as func
from PIL import Image, ImageFont, ImageDraw


font = ImageFont.truetype("Arial Unicode.ttf", 40)
strr = func.return_solutions("sudoku.csv", "solutions", 1)
img = Image.open("/Users/anuj/Desktop/Sudoku/Images/grid-1646985520.479167.png")
draw = ImageDraw.Draw(img)
for item in strr:
    draw.text((10,10), item, font = font)
img.save("Sudoku1.png")