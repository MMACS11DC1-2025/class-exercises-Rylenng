"""
Create a program that uses comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You may use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
#compare
#rylen ng
#sept 26
answer = input()
#getting data from the file
file = open("2.4/responses.csv")
junk = file.readline()

#describing variables
basketball = 0
hockey = 0
baseball = 0
volleyball = 0

for data in file:

    datalist = data.split(",")

#datalists
    print(datalist[4])

if answer == "basketball":
    basketball += 1
elif answer == "baseball":
    baseball += 1
elif answer == "hockey":
    hockey += 1
elif answer == "volleyball":
    volleyball += 1

print("basketball: " + str(basketball))
print("hockey: " + str(hockey))
print("baseball: " + str(baseball))
print("volleyball: " + str(volleyball))