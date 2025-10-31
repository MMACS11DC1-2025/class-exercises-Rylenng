import turtle

turtle = turtle.Turtle()

def drawTree(level, branchLength):
  if level > 0:
    turtle.forward(branchLength)             #goes forward
    turtle.left(120)                         #turns left 120 degrees
    drawTree(level-1, branchLength/1.7)      #length
    
    
    turtle.left(120)                         #turns left 120 degrees again
    drawTree(level-1, branchLength/1.7)
    
    turtle.left(120)
    drawTree(level-1, branchLength/1.7)
    turtle.back(branchLength)
  else:
    turtle.color("green")
    turtle.stamp()
    turtle.color("green")
turtle.speed(0)
turtle.penup()
turtle.goto(0, -180)
turtle.left(90)
turtle.pendown()

turtle.color("brown")
turtle.width(1)
turtle.shape("triangle")
levels = input("How many levels do you want me to draw? ")
drawTree(int(levels), 120)