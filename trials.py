import functions as func
from PIL import Image, ImageFont, ImageDraw


font_size = 20
font = ImageFont.truetype("Arial Unicode.ttf", font_size)
sudoku = func.return_solutions("sudoku.csv", "solutions", 1)[0]
img_height = 900
img_width = 900
box_height = img_height // 9
box_width = img_width // 9
start_x = (box_width - font_size) // 2
start_y = (box_height - font_size) // 2
img = Image.open("/Users/anuj/Desktop/Sudoku/Images/grid-1646985520.479167.png")
draw = ImageDraw.Draw(img)
print(sudoku)
print(len(sudoku))
count = 0
for x in range(start_x, img_height, 100):
    for y in range(start_y, img_width, 100):
        draw.text((y,x), sudoku[count], font = font)
        count +=1


img.save("Sudoku1.png")
