from PIL import Image

def is_green(r,g,b):
    if r >= 0 and r <= 100 and g >= 200 and g <= 255 and b >= 0 and b <= 100:
        return True
    else:
        return False
image_green = Image.open("CS11/5.1/kid-green.jpg").load()
image_beach = Image.open("CS11/5.1/beach.jpg").load()

pixel = image_green[0,0]
r = pixel[0, 0][0]
g = pixel[0, 0][1]
b = pixel[0, 0][2]

print(is_green(r,g,b))