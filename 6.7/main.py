from PIL import Image
import time


def is_dead_grass(pixel):
    r, g, b = pixel
    if r > 120 and g > 90 and b < 90:
        return True
    else:
        return False



image_files = [
    "6.7/image_folder/lawn1.jpg",
    "6.7/image_folder/lawn2.jpg",
    "6.7/image_folder/lawn3.jpg",
    "6.7/image_folder/lawn4.jpg",
    "6.7/image_folder/lawn5.jpg",
    "6.7/image_folder/lawn6.jpg",
    "6.7/image_folder/lawn7.jpg",
    "6.7/image_folder/lawn8.jpg",
    "6.7/image_folder/lawn9.jpg",
    "6.7/image_folder/lawn10.jpg",
]


results = []


start_time = time.time()
for image in image_files:
    img = Image.open(image)
    img = img.convert("RGB")

    width, height = img.size

    dead_grass = 0
    total_pixels = width * height


    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))

            if is_dead_grass(pixel):
                dead_grass += 1

    score = dead_grass / total_pixels

 
    results.append([image, score])


end_time = time.time()
time_taken = end_time - start_time


print("Dead Grass Scores:")
for item in results:
    print(item[0], "=", round(item[1], 3))
print("\n Time taken:", round(time_taken, 3), "seconds")