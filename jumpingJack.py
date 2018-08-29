#Name: Austin Hollis
#jumpingJack.py
#
#Problem: This function will be used to create a program that checks for
#         a mouse click to either start, stop or quit a program that has
#         a stick figure doing jumping jacks. The figure will continue 
#         to do jumping jacks once the start button is pressed and until
#         the stop button has been pressed, it will continue if the
#         start button is pressed again and vice versa until the quit
#         button is pressed.
#
#Certification of Authenticity:
#         I certify that this lab is entirely my own work, but I talked
#         about my code with Stefan, Sarah and Eduardo.
#

#NEED TO ADD AN UPPER AND LOWER BOUND FOR ARMS(HEIGHT OF BODY)#
#NEED TO ADD A LEFT AND RIGHT BOUND FOR LEGS(HALF DISTANCE OF THE ARMS#
from graphics import *

from time import *

from math import *

def wasClicked(pt, rect):
    rtnValue = False

    if pt != None:
        #Gets the x and y coordinates of the point
        xCoord = pt.getX()
        yCoord = pt.getY()

        #Gets the first point of the rectangle and gets the x and y
        #coordinates
        pointOne = rect.getP1()
        rectXCoordOne = pointOne.getX()
        rectYCoordOne = pointOne.getY()

        #Gets the second point of the rectangle and gets the x and y
        #coordinates
        pointTwo = rect.getP2()
        rectXCoordTwo = pointTwo.getX()
        rectYCoordTwo = pointTwo.getY()
        
        #stop if pt >= x1 and pt <= x2 and pt >= y1 and pt <= y2
        if(xCoord >= rectXCoordOne and xCoord <= rectXCoordTwo and yCoord
            >= rectYCoordOne and yCoord <= rectYCoordTwo):
            rtnValue = True
    return rtnValue

def main():
    #The best window to use is a 400 by 400 window due to the math below
    #The graph becomes divided into 32 equal sections
    winWidth = 400
    winHeight = 400
    win = GraphWin("Jumping Jack", winWidth, winHeight)

    DELAY = .1
    #DELAY = .5
    #Creation of the Start Button and Start Border
    startButton=Text(Point(((winWidth/32)*7),
                           ((winHeight/32)*27)),
                     "Start")
    startButton.draw(win)
    startBorder=Rectangle(Point(((winWidth/32)*5),
                                ((winHeight/16)*13)),
                          Point(((winWidth/32)*9),
                                ((winHeight/16)*14)))
    startBorder.draw(win)

    #Backup Points
    #startBorder = Rectangle(Point(62.5,325),Point(112.5,350))
    #Backup Button
    #startButton=Text(Point(87.5,337.5),"Start")

    #Creation of the Stop Button and Stop Border
    stopButton = Text(Point(((winWidth/32)*16),
                            ((winHeight/32)*27)),
                      "Stop")
    stopButton.draw(win)
    stopBorder = Rectangle(Point(((winWidth/16)*7),
                                 ((winHeight/16)*13)),
                           Point(((winWidth/16)*9),
                                 ((winHeight/16)*14)))
    stopBorder.draw(win)

    #Backup Points
    #stopBorder = Rectangle(Point(175,325),Point(225,350))
    #stopButton = Text(Point(200,337.5),"Stop")

    #Creation of the Quit Button and Quit Border
    quitButton = Text(Point(((winWidth/32)*25),((winHeight/32)*27)),
                      "Quit")
    quitButton.draw(win)
    quitBorder = Rectangle(Point(((winWidth/32)*23),
                                 ((winHeight/16)*13)),
                           Point(((winWidth/32)*27),
                                 ((winHeight/16)*14)
                                  ))
    quitBorder.draw(win)

    #Backup Points
    #quitBorder = Rectangle(Point(287.5,325),Point(337.5,350))
    #quitButton = Text(Point(312.5,337.5),"Quit")

    #Sets the Radius
    RADIUS = 20
    NECK_DISTANCE = 3

    #Creation of the body
    body = Line(Point(winWidth/2,
                      (winHeight/4)+RADIUS+NECK_DISTANCE),
                Point(winWidth/2,winHeight/2))
    body.draw(win)

    #Creation of the head
    head = Circle(Point(winWidth/2,winHeight/4),
                  RADIUS+NECK_DISTANCE)
    head.draw(win)
    
    #Acquires the x and y values of the highest point of the body line
    bodyTopPt = body.getP1()
    bodyTopX = bodyTopPt.getX()
    bodyTopY = bodyTopPt.getY()

    #Acquires the x and y values of the lowest point of the body line
    bodyBottomPt = body.getP2()
    bodyBottomX = bodyBottomPt.getX()
    bodyBottomY = bodyBottomPt.getY()

    #Acquires the x and y values of the center point of the body line
    bodyCenterPt = body.getCenter()
    bodyCenterX = bodyCenterPt.getX()
    bodyCenterY = bodyCenterPt.getY()

    #Creation of the right arm
    rightArm=Line(bodyCenterPt,
                  Point(bodyCenterX+(2*RADIUS),
                        bodyCenterY))
    rightArm.draw(win)

    #Acquires the x and y values of the center point of the right arm
    rightArmCenter = rightArm.getCenter()
    rightArmX = rightArmCenter.getX()
    rightArmY = rightArmCenter.getY()

    #Creation of the left arm
    leftArm = Line(Point(bodyCenterX-(2*RADIUS),
                         bodyCenterY),
                    bodyCenterPt)
    leftArm.draw(win)
    
    #Acquires the x and y values of the center point of the left arm
    leftArmCenter = leftArm.getCenter()
    leftArmX = leftArmCenter.getX()
    leftArmY = leftArmCenter.getY()

    #Creation of the right leg
    rightLeg = Line(bodyBottomPt,
                    Point(rightArmX+(RADIUS/2),
                             (bodyBottomY+(2*RADIUS))))
    rightLeg.draw(win)

    #Creation of the left leg
    leftLeg = Line(bodyBottomPt,
                   Point(leftArmX-(RADIUS/2),
                            (bodyBottomY+(2*RADIUS))))
    leftLeg.draw(win)
    #Points for the second left arm
    leftArmTwo = Line(Point(bodyCenterX-((3/2)*RADIUS),
                       bodyCenterY-((3/2)*RADIUS)),
                             bodyCenterPt)
    #Points for the second right arm
    rightArmTwo = Line(bodyCenterPt,
                       Point(bodyCenterX+((3/2)*RADIUS),
                             bodyCenterY-((3/2)*RADIUS)))
    #Points for the second left leg
    leftLegTwo = Line(bodyBottomPt,
                      Point(leftArmX-(RADIUS),
                            (bodyBottomY+(2*RADIUS))))
    #Points for the second right leg
    rightLegTwo = Line(bodyBottomPt,
                       Point(rightArmX+(RADIUS),
                             (bodyBottomY+(2*RADIUS))))
    #Points for the third left arm line
    leftArmThree = Line(Point(bodyCenterX-((3/2)*RADIUS),
                              bodyCenterY+((3/2)*RADIUS)),
                        bodyCenterPt)
    #Points for the third right arm line
    rightArmThree = Line(bodyCenterPt,
                         Point(bodyCenterX+((3/2)*RADIUS),
                                   bodyCenterY+((3/2)*RADIUS)))
    #Points for the third left leg line.
    leftLegThree = Line(bodyBottomPt,
                        Point(leftArmX,
                              (bodyBottomY+(2*RADIUS))))
    #Points for the third right leg line
    rightLegThree = Line(bodyBottomPt,
                         Point(rightArmX,
                               (bodyBottomY+(2*RADIUS))))


    #While loop to check the mouse for clicking of any buttons.
    doPlay = True
    #Is set to set the parameter for an if statement inside the loop.
    isAnimated = False
    while doPlay:
        pt = win.checkMouse()
        #Starts the animation
        if wasClicked(pt,startBorder):
            print("Start")
            isAnimated = True    
        #Stops the animation if the button to stop was clicked
        if wasClicked(pt,stopBorder):
            print("Stop")
            isAnimated = False

        #Closes the window if the quit button is pressed.
        if wasClicked(pt,quitBorder):
            doPlay = False
            win.close()

        #Draws Jumping Jack is isAnimated is true.    
        if isAnimated == True:
            leftArm.undraw()
            rightArm.undraw()
            leftLeg.undraw()
            rightLeg.undraw()

            sleep(DELAY)

            leftArmTwo.draw(win)
            rightArmTwo.draw(win)
            leftLegTwo.draw(win)        
            rightLegTwo.draw(win)
            
            sleep(DELAY)

            leftArmTwo.undraw()
            rightArmTwo.undraw()
            leftLegTwo.undraw()
            rightLegTwo.undraw()

            sleep(DELAY)

            leftArm.draw(win)
            rightArm.draw(win)
            leftLeg.draw(win)
            rightLeg.draw(win)

            sleep(DELAY)

            leftArm.undraw()
            rightArm.undraw()
            leftLeg.undraw()
            rightLeg.undraw()

            sleep(DELAY)

            leftArmThree.draw(win)
            rightArmThree.draw(win)
            leftLegThree.draw(win)
            rightLegThree.draw(win)

            sleep(DELAY)

            leftArmThree.undraw()
            rightArmThree.undraw()
            leftLegThree.undraw()
            rightLegThree.undraw()

            sleep(DELAY)

            leftArm.draw(win)
            rightArm.draw(win)
            leftLeg.draw(win)
            rightLeg.draw(win)

            sleep(DELAY)
        sleep(DELAY)
  
main()
