from PIL import Image

def is_green(r,g,b):
    if r >= 0 and r <= 100 and g >= 200 and g <= 255 and b >= 0 and b <= 100:
        return "green"
    else:
        return "not green"
image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

image_output = Image.open("5.1/kid-green.jpg")

width = image_output.width
length = image_output.height
for i in range(width):
    for j in range(height):
        r, g, b = image_green[i, j]
        if is_green(r, g, b) == "green":
            image_output.putpixel((i, j), image_beach[i, j])
