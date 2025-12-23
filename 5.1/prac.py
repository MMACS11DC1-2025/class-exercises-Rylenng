
def is_light(pixel):

    average = sum(pixel) / 3
    return average >= 128


print(is_light((200, 150, 180)))   # Should print True
print(is_light((50, 80, 100)))     # Should print False
