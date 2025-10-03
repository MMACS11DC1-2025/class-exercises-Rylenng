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
file = open("2.4/responses.csv")
junk = file.readline()
lines = file.readline()
name = input("What is your name\n")
answer = input("\n Whats your favourite subject?\n")
