# triangle.py
# Author: Zelle (pp. 103-04)
# Modified by Pharr to eliminate coordinates

from graphics import *

def main():
    winWidth = 400
    winHeight = 400
    
    win = GraphWin("Draw a Triangle", winWidth, winHeight)
    message = Text(Point(winWidth/2, winHeight-10), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of a triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to quit")
    win.getMouse()
    win.close()

main()
