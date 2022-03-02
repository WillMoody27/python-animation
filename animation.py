import math
import random
from graphics import *
import time


# function
def Scanner():
    # Window size to be used
    x = 400
    y = 400

    # variables used
    textColor = "#ccc"
    colorGray = "#f2f2f2"
    lineOneColor = "#d8eefe"
    approvedColor = color_rgb(67, 241, 0)
    deniedColor = color_rgb(255, 0, 0)

    # Set random color upon compile using RGB format not hex or black (rgb(0,0,0))
    r = random.randint(125, 130)
    g = random.randint(125, 130)
    b = random.randint(125, 130)

    # size of the shape - this is what we want to see
    window = GraphWin("A Rectangle", x, y)

    # Window background color
    window.setBackground("white")

    # Display the name of agency using Text method
    agency = Text(Point(x / 2, 350), "CIA")
    agency.setTextColor(textColor)
    agency.getText()
    agency.setStyle("bold")
    agency.setSize(36)
    agency.draw(window)

    # Layer behind housing the text of the message
    rect2 = Rectangle(Point(20, 10), Point(380, 70))
    rect2.setFill("#000")
    rect2.setWidth(5)
    rect2.setOutline(colorGray)
    rect2.draw(window)

    # Layer behind moving scanner animation
    rect = Rectangle(Point(-5, 250), Point(405, 150))
    rect.setFill("#f9f9f9")
    rect.setWidth(10)
    rect.setOutline(colorGray)
    rect.draw(window)

    # Gray circle outermost layer
    cir3 = Circle(Point(x / 2, y / 2), 20)
    cir3.setWidth(40)
    cir3.setOutline("#c2c2c2")
    cir3.draw(window)

    # Innermost
    cir2 = Circle(Point(x / 2, y / 2), 20)
    cir2.setWidth(0)
    cir2.setOutline("white")
    cir2.draw(window)

    # First text displayed mimics a face scan
    message = Text(Point(x / 2, y / 10), "FACE SCAN...")
    message.setStyle("bold")
    message.setTextColor(textColor)
    message.getText()
    message.setSize(30)
    message.draw(window)

    # create random int odd and even
    rand = random.randint(1, 2)

    # Move both drawn circles then change text
    for i in range(80):
        cir2.setFill(color_rgb(227, 230, 235))
        if i < 20:
            # cir2.setFill(color_rgb(r, g, b))
            cir2.move(5, 0)
            cir3.move(5, 0)
        if 20 < i <= 40:
            # cir2.setFill(color_rgb(r, g, b))
            cir2.move(-5, 0)
            cir3.move(-5, 0)

        if 40 <= i <= 60:
            # cir2.setFill(color_rgb(r, g, b))
            cir2.move(-5, 0)
            cir3.move(-5, 0)
        if 60 <= i <= 80:
            cir2.move(5.31, 0)
            cir3.move(5.31, 0)
    message.undraw()

    # time.sleep(.05)
    for i in range(20):
        cir2.setWidth(i)

    i = 0

    # Second text displayed mimics a retina scan
    message = Text(Point(x / 2, y / 10), "RETINA SCAN...")
    message.setStyle("bold")
    message.setTextColor(textColor)
    message.getText()
    message.setSize(30)
    message.draw(window)

    # Mimic the animation of a eye scanner
    while i < 360:
        if i % 1 == 0:
            # converted to radians
            radians = math.radians(i)
            px = x / 2 + 119 * math.cos(radians)
            py = y / 2 + 119 * math.sin(radians)
            # Point in which shape begins on canvas
            pointOfRect = Point(px, py)

            if i < 360:
                if i % 10 == 0:
                    line1 = Line(Point(x / 2, y / 2), pointOfRect)
                    line1.setWidth(1)
                    line1.setFill(lineOneColor)
                    line1.draw(window)
                    time.sleep(0.05)
        i = i + 1
    message.undraw()

    # Animation scanner complete determine access granted based on conditional statements
    if rand % 2 == 0:
        message1 = Text(Point(x / 2, y / 10), "ACCESS APPROVED")
        message1.setStyle("bold")
        message1.setTextColor(approvedColor)
        message1.getText()
        message1.setSize(32)
        message1.draw(window)
        cir2.setOutline(approvedColor)

    # Animation scanner complete determine access denied based on conditional statements
    else:
        message2 = Text(Point(x / 2, y / 10), "ACCESS DENIED")
        message2.setStyle("bold")
        message2.setTextColor(deniedColor)
        message2.getText()
        message2.setSize(36)
        message2.draw(window)
        cir2.setOutline(deniedColor)

    # places the circle onto the canvas that was specified
    window.getMouse()
    window.close()


# Function that is called
Scanner()
