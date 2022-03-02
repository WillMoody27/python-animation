from graphics import *
import time


# function
def DrawCircle():
    x = 500
    y = 500
    # size of the shape - this is what we want to see
    windw = GraphWin("A Circle", x, y)
    # program will recognize HEX and RGB and names of the colors
    windw.setBackground("orange")
    # this the location of point
    p = Point(x/2, y/2)
    c = Circle(p, 100)
    # places the circle onto the canvas that was specified
    c.draw(windw)
    i = 1
    while i <= 10:
        # this for the value of x1
        x1 = 150 + (i * 20)
        p2 = Point(x1, 150)
        c2 = Circle(p2, i * 10)
        # if i % 2 == 0:
        #     c2.setFill("blue")
        c2.setOutline("yellow")
        c2.setFill("purple")
        c2.draw(windw)
        i = i + 1
        time.sleep(.25)
    # get the mouse click on the window to close it
    windw.getMouse()
    windw.close()

# Function that is called
DrawCircle()
