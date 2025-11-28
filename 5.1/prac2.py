from PIL import Image
def is_binarized(pixel):
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]
        if r >= 0 and r <= 100 and g >= 90 and g <= 255 and b >= 0 and b <= 100:
            return True
        else:
            return False
        
def is_light(pixel):

    average = sum(pixel) / 3
    return average >= 128

print(is_light((0, 0, 0)))
print(is_light((255, 255, 255)))
    
image_beach = Image.open("5.1/mountain.jpg").load()

image_output = Image.open("5.1/mountain.jpg")

width = image_output.width
height = image_output.height
for i in range(width):
    for j in range(height):

        if is_light(image_beach[i,j]) == True:
            beach = image_beach[i,j]
            xy = (i,j)
            image_output.putpixel(xy, (255, 255, 255))
        else:
            xy = (i,j)
            image_output.putpixel(xy, (0, 0, 0))
image_output.save("output.png","png")