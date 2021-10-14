"""
Lecture 9: Balanced Search Tree
    Objective
        Understand the principles of binary search trees that assure that tree remains balanced at all times
    Binary Search Tree Problem
        Unfortunately, search tree of height n can be constructed by inserting keys in sorted order
        In this case, performance of put() method is O(n)
    Balanced Binary Search Tree
        Special kind of binary serach tree
        Automatically assures that tree remains balanced at all times
        Tree is called AVL tree
        AVL tree implements Map ADT just like regular binary search tree
        Difference lies in its performance
        Need to keep track of balance
            Height of left and right subtree of each node
            balanceFactor = height(leftSubTree) - height(rightSubTree)
Lecture 10: Dynamic Programming, Memorization
    Overview
        Graphics Module "turtle"
        Visualizing recursion
        Dynamic programming
    Objective
        Learn how to use "turtle" for visualization
        Learn how to use recursion to implement a game
        Be able to apply dynamic programming to solve optimization problems
    Visualization of Recursion
        Use turtle tool for visualization
        Turtle metaphor:
            Move forward, back, turn left/right etc.
            Tail up/ down; if down => draws a line
            Change width and color of tail
"""
import turtle

# Program to create a square spiral in turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()
def drawSpiral(myTurtle,lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)
drawSpiral(myTurtle,100)
myWin.exitonclick()

"""
    Visualization of Recursion
        Draw a fractal tree
        Fractals: same basic shape no matter how much it is magnified (self-similarity)
            Snowflakes, fern, nautilus
        Used in computer graphics to generate realistic scenes
    Generate a fractal tree
    Small twig has the same shape as tree
        Tree is trunk with smaller trees going off to the left and right
        Apply recursion to both smaller left and right trees
    Exploring a maze
        Important applications for robotics
        Problem to solve: find a way out of maze
        Assume maze is divided up in squares
            Open or occupied
            Turtle can only pass through open squares
            If it bumps in wall => needs to find different direction
        Must remember where turtle has been to avoid infinite loops
        Brothers Grim to the rescue: Bread crumbs! 
            If step back is taken and bread crumb is already there, back up further
            Try next direction
            Backing up as easy as returning from recursive call
        Representation
            __init__ reads in data file representing a maze, initializes the internal representation of 
                the maze, and finds the starting position for the turtle
            drawMaze draws the maze in a window on the screen
            updatePosition Updates the internal representation of the maze and changes the position of the turtle in the window
            isExit checks to see if the current position is an exit from the maze
        
"""