import functions as func
from PIL import Image, ImageFont, ImageDraw


font = ImageFont.truetype("Arial Unicode.ttf", 40)
sudoku = str(func.return_solutions("sudoku.csv", "solutions", 1))
img = Image.open("/Users/anuj/Desktop/Sudoku/Images/grid-1646985520.479167.png")
draw = ImageDraw.Draw(img)
print(type(sudoku))

for item in range(len(sudoku)):   
    for x in range(50, 900, 100):
        for y in range(50, 900, 100):
            draw.text((x,y), sudoku[item], font = font)

img.save("Sudoku1.png")
