"""
Make An Interactive Drawing or Animation 
Explore the turtle drawing package to create an interactive drawing.
It should use a while loop.
Your program should also include at least one function you’ve made yourself 
"""
# Rylen Ng
# Drawing with Turtle
# June 11, 2024
import turtle
t = turtle.Turtle()

while True:
    def draw_square():
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.square(30)
    t.penup()

    t.goto(-100, 0)
    t.stamp()

    draw_square()