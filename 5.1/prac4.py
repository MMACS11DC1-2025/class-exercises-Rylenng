from PIL import Image

def colour(r, g, b):

    colours = {
        (1, 0, 0): "red",
        (0, 1, 0): "green",
        (0, 0, 1): "blue",
        (1, 1, 0): "yellow",
        (1, 0, 1): "magenta",
        (0, 1, 1): "cyan",
        (1, 1, 1): "white",
        (0, 0, 0): "black"
    }
    
    colourlist = [0,0,0]
    if 170<=r<=255:
        colourlist[0] = 1
    
    if 100<=g<=255:
        colourlist[1] = 1

    if 170<=b<=255:
        colourlist[2] = 1

    for colours in colours:
        if tuple(colourlist) == colours:
            return colours[colours]
    return "unknown"

file = Image.open("5.1/jelly_beans.jpg")
jbimg= file.load()


width = file.width
height = file.height


for i in range(colour):
    for x in range(width):
        for y in range(height):
            r,g,b = jbimg[x,y]

            if r > 210 and r < 250 and g > 150 and b < 100:
                yellow_pixel += 1
            if r > 170 and r < 150 and g > 10 and g < 20 and b > 10 and b < 0:
                red_pixel += 1
print(yellow_pixel)
print(red_pixel)
print(width * height)