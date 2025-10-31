"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""
#calculator
#Rylen Ng
#Date: sept 22
print("Hello i am a calculator")
print("ask a simple math question here (2+2)")
print("put your first whole number here")
first = float(input())
print("put your operation style (+-/*)")
operation = float(.strip(input()))
print("put your second whole number here")
second = float(input())

match operation
    case "+":
        answer = float(first) + float(second)
    case "-":
        answer = float(first) - float(second)
    case "/":
        answer = float(first) / float(second)
    case "*":
        answer = float(first) * float(second)
    print(answer)