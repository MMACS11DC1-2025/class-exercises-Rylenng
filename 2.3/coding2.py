"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""
print("judge number one what is your score out of 10?")
fr = float(input())
print("judge number two what is your score out of 10?")
se = float(input())
print("judge number three what is your score out of 10?")
th = float(input())
print("judge number four what is your score out of 10?")
fo = float(input())
print("judge number five what is your score out of 10?")
fi = float(input())
final = (fr+se+th+fo+fi)/5
print("your average is "+ str(final))