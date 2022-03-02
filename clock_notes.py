from graphics import *
import time
import math


def DrawCircle():
    x = 500
    y = 325
    r = 125

    windw = GraphWin("A Circle", x, y)

    # initial point
    p1 = Point(x / 2, y / 2)
    c = Circle(p1, r)
    c.draw(windw)

    cx = x / 2
    cy = y / 2


    p2 = Point(x / 3, y / 3)
    p3 = Point(x * 2 / 3, y * 2 / 3)
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    # line1.draw(windw)
    # line2.draw(windw)
    time.sleep(2)
    # line1.undraw(windw)

    for i in range(360):
        # convert degrees to radians
        if i % 1 == 0:
            rd = math.radians(i)

            # Point of each iteration based on cos
            pcx = cx + r * math.cos(rd)
            pcy = cy + r * math.sin(rd)
            pc = Point(pcx, pcy)
            # circle2 = Circle(pc, 3)
            # circle2.setFill("red")
            # circle2.draw(windw)

            line3 = Line(p1, pc)

            if i % 2 == 0:
                line3.setFill("red")
            if i % 5 == 0:
                line3.setFill("yellow")
            if i % 3 == 0:
                line3.setFill("green")
            if i % 7 == 0:
                line3.setFill("black")

            line3.setWidth(1)

            line3.draw(windw)

            # time.sleep(0.1)

    windw.getMouse()
    windw.close()

DrawCircle()