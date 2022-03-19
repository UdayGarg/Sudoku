import functions as func
from PIL import Image, ImageFont, ImageDraw


font = ImageFont.truetype("Arial Unicode.ttf", 50)
sudoku = func.return_solutions("sudoku.csv", "solutions", 1)[0]
img = Image.open("/Users/anuj/Desktop/Sudoku/Images/grid-1646985520.479167.png")
draw = ImageDraw.Draw(img)
print(sudoku)
print(len(sudoku))
count = 0
for x in range(0, 900, 100):
    for y in range(0, 900, 100):
        draw.text((y,x), sudoku[count], font = font)
        count +=1


img.save("Sudoku1.png")
