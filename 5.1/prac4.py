from PIL import Image

def is_yellow(r, g, b):

    if r > 150 and g > 150 and b < 150:
        return "yellow" 
    else:
        return "not yellow"

white_pixel = (150, 150, 150)





my_image = Image.open("5.1/jelly_beans.jpg").load()
output_large = Image.open("5.1/jelly_beans.jpg")





width = output_large.width
height = output_large.height
for i in range(width):
    for j in range(height):
        if is_yellow(my_image[i, j][0], my_image[i, j][1], my_image[i, j][2]) == "yellow":
            xy = (i, j)
            output_large.putpixel(xy, (255, 255, 255))
output_large.save("jellybeans_output.png", "png")