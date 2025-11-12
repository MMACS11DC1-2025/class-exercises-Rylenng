# Fractal Tree Project 🌳

## Overview
This project draws a fractal tree using Python’s turtle graphics module.  
The goal was to create a recursive tree structure with branching patterns inspired by real fractal trees.



## Development Summary
- Created a recursive function to draw the tree.  
- Experimented with angles and branch lengths to achieve a natural, recursive look.  
- Took inspiration from online fractal tree examples.  
- Consulted the Turtle Graphics documentation for specific drawing commands.  
- Traced the tree multiple times to ensure correct angles and recursion.  
- Tuned parameters for a visually appealing tree structure*.  
- Final result produced a good-looking recursive fractal tree.  
- Faced no major challenges during implementation.  



## Test Case 1

### Code
```python
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

levels = input("How many levels do you want me to draw? ")
drawTree(int(levels), 120)
```
## Notes
* Expected to make a tree with four branches per level.

* Angles didn’t match expectations — caused overlapping branches.

* The program drew the tree twice, making it slow to render.

* The output resembled a fractal tree but needed angle adjustments.

Reference: See test_case_no_1.png.

## Test Case 2
### Code
```python

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

levels = input("How many levels do you want me to draw? ")
drawTree(int(levels), 120)
```
## Notes
* Attempted to replicate the shape from Test Case 1.

* Angle of 240° was too large.

* Tree started drawing on the right side — desired to start from the left.

* This version was close to the final idea but required fine-tuning.

Reference: See test_case_no_2.png.

## Peer Review Feedback
Tejas: Liked the shape of the tree but felt it was a bit basic.

Gabe: Mentioned that it takes too long to draw at higher recursion levels.

## Final Thoughts
* The final tree design achieved the recursive, organic look intended.

### Future Improvements
* Add randomized angles for a more natural variation.

* Use color gradients for branches and leaves.

* Implement speed optimization for higher recursion depths.


