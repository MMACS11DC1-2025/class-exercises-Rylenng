"""
Create a program that uses comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You may use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
#rylen ng
#comparison assignment
#Oct 8

file = open("2.4/responses.csv")
lines = file.readlines()[1:]


print("1. Compare favourite digits")
print("2. Compare favourite pets")
choice = input("Type 1 or 2: ")

if choice == "1":
    number = input("Enter a number from 1 to 9: ")

    higher = ""
    lower = ""
    same = ""

    for line in lines:
        parts = line.strip().split(",")
        name = str(parts[1])
        digit = str(parts[2])

        if digit > number:
            higher = higher + name + ", "
        elif digit < number:
            lower = lower + name + ", "
        else:
            same = same + name + ", "

    print("People with higher numbers: " + higher)
    print("People with lower numbers: " + lower)
    print("People with the same number: " + same)

elif choice == "2":
    pet = input("Enter a pet (Dog, Cat, Rabbit, etc): ")
    result = ""

    for line in lines:
        pe = line.strip().split(",")
        name = str(pe[1])
        favpet = str(pe[3])

        if favpet.lower() == pet.lower():
            result = result + name + ", "

    print("People who chose " + pet + ": " + result)

else:
    print("try again")



