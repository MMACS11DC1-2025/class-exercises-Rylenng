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

for i in range(len(results) - 1):
    for j in range(i + 1, len(results)):
        if results[i][1] < results[j][1]:
            results[i], results[j] = results[j], results[i]

def search_start_index(results, target_score):
    low = 0
    high = len(results) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if results[mid][0] < target_score:
            return results[mid][1]

        elif results[mid][0] > target_score:
            low = mid + 1
        else:
            return results[mid][1]

    return -1

query = input("\nEnter grass % to look for (or skip)")
if query != "":
    target = float(query) / 10
    first = 0
    last = len(results) - 1
    tot = 0.01
    found = False

    while first <= last:
        mid = (first + last) // 2
        mid_value = results[mid][1]

        if abs(mid_value - target) <= tot:
            print(f"Found image: " + results[mid][0] + "=" + str(round(results[mid][1], 2)) + "%")
            found = True
            break
        elif mid_value < target:
            last = mid - 1
        else:
            first = mid + 1

        if not found:
            print("No image found with that grass percentage.")


 

print("Dead Grass Scores:")
for item in range(min(5, len(results))):
    print(results[item][0], "=", round(results[item][1], 3))
print("\n Time taken:", round(time_taken, 3), "seconds")