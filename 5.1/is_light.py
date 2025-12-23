from PIL import Image
def is_light(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    average = int((r + g + b) / 3)
    return average >= 128
white_pixel = (255, 255, 255)
print(is_light((255, 255, 255)))
print(is_light(white_pixel))

my_image = Image.open("5.1/kid-green.jpg").load()
output_large = Image.open("5.1/kid-green.jpg")

width = output_large.width
height = output_large.height
for i in range(width):
    for j in range(height):
        if is_light(my_image[i, j]):
            xy = (i, j)
            output_large.putpixel(xy, (255, 255, 255))
        else:
            xy = (i, j)
            output_large.putpixel(xy, (0, 0, 0))
output_large.save("kidgreen_output.png", "png")
