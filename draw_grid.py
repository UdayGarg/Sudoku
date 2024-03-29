"""This module draws a 9x9 empty grid and then saves it as PNG file"""
import time
from PIL import Image, ImageDraw


def generate_empty_grid():
    """Function to draw a 9x9 grid in an 900x900 pixels image and save it as PNG file """
    STEP_COUNT = 9
    height = 900
    width = 900
    image = Image.new(mode='L', size=(height, width), color=255)
    # Draw some lines
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / STEP_COUNT)
    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=128)
    x_start = 0
    x_end = image.width
    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)
    del draw
    filename = f"grid-{time.time()}.png"
    print(f"saving {filename}")
    image.save(filename)



if __name__ == '__main__':
    generate_empty_grid()
