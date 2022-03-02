from graphics import *
import time

# function
def DrawCircle():
    # Canvas to be used
    x = 400
    y = 400
    # size of the shape - this is what we want to see
    window = GraphWin("A Rectangle", x, y)
    # program will recognize HEX and RGB and names of the colors
    window.setBackground("coral")
    # this the location of point
    # p = Point(x/2, y/2)
    c = Rectangle(Point(0, 0), Point(400, 400))

    # Create line for hour
    hourLine = Line(Point(x/2, y/2), Point(270, 170))
    hourLine.draw(window)
    hourLine.setWidth(3)
    hourLine.setFill("lightgray")

    # Create line for second
    # create a loop for the second point to animate hand movement
    minLine = Line(Point(x/2, y/2), Point(150, 290))
    minLine.draw(window)
    minLine.setWidth(1.5)
    minLine.setFill("white")


    c.draw(window)

    # i = 0
    # j = 0
    # k = 0
    # l = 0
    # while i <= 400:
    #     # Create line for second
    #     # create a loop for the second point to animate hand movement
    #     # move the second hand
    #
    #     secondLine = Line(Point(x / 2, y / 2), Point(0, i))
    #     secondLine.draw(window)
    #     secondLine.setWidth(1.5)
    #     secondLine.setFill("red")
    #     i = i + 20
    #
    # while j <= 400:
    #     # Create line for second
    #     # create a loop for the second point to animate hand movement
    #     # move the second hand
    #
    #     secondLine = Line(Point(x / 2, y / 2), Point(j, 400))
    #     secondLine.draw(window)
    #     secondLine.setWidth(1.5)
    #     secondLine.setFill("blue")
    #     j = j + 25
    #
    # while k <= 400:
    #     # Create line for second
    #     # create a loop for the second point to animate hand movement
    #     # move the second hand
    #
    #     secondLine = Line(Point(x / 2, y / 2), Point(k, 400))
    #     secondLine.draw(window)
    #     secondLine.setWidth(1.5)
    #     secondLine.setFill("yellow")
    #     k = k + 25
    #
    # while l <= 400:
    #     # Create line for second
    #     # create a loop for the second point to animate hand movement
    #     # move the second hand
    #
    #     secondLine = Line(Point(x / 2, y / 2), Point(l, 400))
    #     secondLine.draw(window)
    #     secondLine.setWidth(1.5)
    #     secondLine.setFill("blue")
    #     l = l + 25

    # places the circle onto the canvas that was specified
    window.getMouse()
    window.close()

# Function that is called
DrawCircle()
