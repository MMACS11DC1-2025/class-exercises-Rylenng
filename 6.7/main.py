from PIL import Image
import time

# ---------------------------------------
# A simple function to check for dead grass
# ---------------------------------------
def is_dead_grass(pixel):
    r, g, b = pixel

    # Very simple rule:
    # Dead grass tends to look brown or yellow
    if r > 120 and g > 90 and b < 90:
        return True
    else:
        return False



image_files = [
    "lawn1.jpg",
    "lawn2.jpg",
    "lawn3.jpg",
    "lawn4.jpg",
    "lawn5.jpg",
    "lawn6.jpg",
    "lawn7.jpg",
    "lawn8.jpg",
    "lawn9.jpg",
    "lawn10.jpg"
]

# This list will store the results
results = []


# Start timing the processing
start_time = time.time()

# ---------------------------------------
# Go through every image
# ---------------------------------------
for filename in image_files:
    img = Image.open(filename)
    img = img.convert("RGB")

    width, height = img.size

    dead_pixels = 0
    total_pixels = width * height

    # Look at every pixel in the image
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))

            if is_dead_grass(pixel):
                dead_pixels += 1

    # Score = % of pixels that look like dead grass
    score = dead_pixels / total_pixels

    # Save the result
    results.append([filename, score])


# End timing
end_time = time.time()
time_taken = end_time - start_time

# ---------------------------------------
# Print the results
# ---------------------------------------
print("Dead Grass Scores:")
for item in results:
    print(item[0], "→", round(item[1], 3))

print("\nTime taken:", round(time_taken, 3), "seconds")
