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

    # # this the location of point
    # p = Point(x/2, y/2)
    # c = Circle(p, 100)
    # # places the circle onto the canvas that was specified
    # c.draw(windw)

    # aLine = Line(Point(1,3), Point(7,4)) this is how we would create a line for the coordinates
    # # This makes an letter A
    # line1 = Line(Point(10, 100), Point(40,10))
    # line2 = Line(Point(40, 10), Point(70, 100))
    # line3 = Line(Point(24, 60), Point(56, 60))

    # w

    line1 = Line(Point(30, 100), Point(20,10))
    line2 = Line(Point(50, 10), Point(30, 100))
    line3 = Line(Point(60, 100), Point(50,10))
    line4 = Line(Point(80, 10), Point(60, 100))

    #I (need 2)
    line5 = Line(Point(90, 30), Point(90, 100))
    line6 = Line(Point(50, 10), Point(30, 100))

    #L (need 2)

    #A

    #M


    # corner points at origin and at max (500, 500)
    # line4 = Line(Point(0,0), Point(x, y))
    # line5 = Line(Point(x, 0), Point(0, y))

    # this will draw the shape of the line of the figure
    line1.draw(windw)
    line2.draw(windw)
    line3.draw(windw)
    line4.draw(windw)
    line5.draw(windw)
    line6.draw(windw)

    # Line Properties
    line1.setWidth(3)
    line2.setWidth(3)
    line3.setWidth(3)
    line4.setWidth(3)
    line5.setWidth(3)
    line6.setWidth(3)


    # line4.draw(windw)
    # line5.draw(windw)

    # aLine = Line(Point(1,3), Point(7,4)) this is how we would create a line for the coordinates
    # This makes an letter A

    windw.getMouse()
    windw.close()
# Function that is called
DrawCircle()
