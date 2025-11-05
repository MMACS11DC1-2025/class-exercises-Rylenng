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


#testing summary
# This function draws a fractal tree using recursion
# wanted to create a branching tree structure
#played around with angles and lengths to get a recursive tree look
#viewed examples of fractal trees online for inspiration
#Followed the turtle graphics documentation for specific commands
#traced the drawing to ensure correct angles and lengths
#played with parameters to get a visually appealing tree
#finally got a recursive tree that looks good
#satisfied with the final result
#no major challenges faced

"""test case code
import turtle

turtle = turtle.Turtle()                     

def drawTree(level, branchLength):           
  if level > 0:
    turtle.forward(branchLength)            
    turtle.left(120)                         
    drawTree(level-1, branchLength/1.7)      
    
    
    turtle.right(240)                         
    drawTree(level-1, branchLength/1.7)       

    turtle.right(120)                        
    drawTree(level-1, branchLength/1.7)  

    turtle.left(240)                        
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
levels = input("How many levels do you want me to draw? ")  #user input for levels
drawTree(int(levels), 120)  

expected to make a tree with four branches at each level, but the angles were not what i wanted
drew the tree twice so it took too long to draw
overlapping branches
Looked like examples of fractal trees with four branches
look at test case no 1.png for reference
"""
"""test case code number 2
import turtle

turtle = turtle.Turtle()                     

def drawTree(level, branchLength):           
  if level > 0:
    turtle.forward(branchLength)            
    turtle.left(240)                         
    drawTree(level-1, branchLength/1.7)      
    
    
    turtle.left(240)                         
    drawTree(level-1, branchLength/1.7)       

    turtle.left(240)                        
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
levels = input("How many levels do you want me to draw? ")  #user input for levels
drawTree(int(levels), 120)

tried to make exact shape as previous test case 
the angle was more than needed
Last test case before the final one
this one started drawing on the right and i wanted it to start on the left
had the right idea but the angles were off
look at test case no 2.png for reference
"""
"""peer review feedback
tejas: He likes the shape of the tree but thinks its a bit basic
gabe: takes too long to draw at higher levels
"""