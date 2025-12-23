import turtle
turtle = turtle.Turtle()                     #creates turtle object

def drawTree(level, branchLength):           #defines the function
  if level > 0:
    turtle.forward(branchLength)             #goes forward
    turtle.left(120)                         #turns left 120 degrees
    drawTree(level-1, branchLength/1.7)      #length
    
    
    turtle.left(120)                         #turns left 120 degrees again
    drawTree(level-1, branchLength/1.7)       #length

    turtle.left(120)                          #turns left 120 degrees again
    drawTree(level-1, branchLength/1.7)      #length
    turtle.back(branchLength)                 #goes back
  else:
    turtle.color("green")                 #changes color to green
    turtle.stamp()                        #draws the shape
    turtle.color("green")                 #changes color back to brown
turtle.speed(0)                           #sets the speed to the fastest
turtle.penup()                            #stops drawing
turtle.goto(0, -180)                      #goes to the starting position
turtle.left(90)                           #turns left 90 degrees
turtle.pendown()                          #starts drawing

turtle.color("brown")                     #changes color to brown
turtle.width(1)                           #sets the width of the pen
turtle.shape("triangle")                  #turtle shape to triangle
levels = input("How many levels do you want me to draw? ")  #user input for levels
drawTree(int(levels), 120)  #calls the function


