#Name: Austin Hollis
#bumper.py
#
#Problem: This function will be used to create and move two unique
#         'bumper cars' and have them bounce off the walls and
#         each other while changing directions on each bounce off
#         of the walls and each other while also changing colors when
#         the cars collide off of each other.
#
#Certification of Authenticity:
#         I certify that this lab is entirely my own work, but I talked
#         about my code with Stefan and Eduardo.

from graphics import *

import math

import random

import time

#Function for getting random amounts to move the balls by.
def getRandom(moveAmount):
    return random.randint((-1) * moveAmount, moveAmount)

#Function to set a hit box for the vertical side.
def hitVertical(ball, win):
    didHitVertical = False
    winWidth = win.getWidth()
    #Gets the center and radius of the balls.
    ballCenter = ball.getCenter()
    ballRadius = ball.getRadius()
    #Sets the area for the balls to bounce off of.
    posDistBounce = ballCenter.getX() + ballRadius
    negDistBounce = ballCenter.getX() - ballRadius
    #sets the boolean for the balls to bounce off of.
    if posDistBounce > winWidth or negDistBounce < 0:
        didHitVertical = True

    return didHitVertical

#Function to set a hit box for the horizontal sides.
def hitHorizontal(ball, win):
    didHitHorizontal = False
    winHeight = win.getHeight()
    #gets the radius and centers of the balls.
    ballCenter = ball.getCenter()
    ballRadius = ball.getRadius()
    #sets the area for the balls to bounce off of.
    posDistBounce = ballCenter.getY() + ballRadius
    negDistBounce = ballCenter.getY() - ballRadius
    #sets the boolean for the balls to bounce off of.
    if posDistBounce > winHeight or negDistBounce < 0:
        didHitHorizontal = True

    return didHitHorizontal

#Function for the collisions of the balls.
def didCollide(ball1, ball2):
    #Gets the centers.
    ballOneCenter = ball1.getCenter()
    ballTwoCenter = ball2.getCenter()
    #Gets the X and Y coordinates of the Centers.
    ballOneX = ballOneCenter.getX()
    ballOneY = ballOneCenter.getY()
    ballTwoX = ballTwoCenter.getX()
    ballTwoY = ballTwoCenter.getY()
    #Formula for the distance.
    distance=math.sqrt((ballOneX-ballTwoX)**2 + (ballOneY-ballTwoY)**2)
    totalRadius = ball1.getRadius() + ball2.getRadius()

    return distance <= totalRadius

#Function for changing random colors 
def randomColor():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return color_rgb(red, green, blue)

#Function for getting a random point.
def randomPoint(ballRadius,win):
    pt = Point(random.randint(0+ballRadius,win.getWidth()-ballRadius),
               random.randint(0+ballRadius,win.getHeight()-ballRadius))
    return pt

#Main Function.    
def main():
    #Sets the window width.
    winWidth = 400
    #Sets the window height.
    winHeight = 400

    #Names the GraphWin win.
    win = GraphWin("Bumper Cars", winWidth, winHeight)

    #Sets amount for the balls to move at
    moveAmount = 10
    #Adds a delay to make the ball seem like it is moving
    delay = .03
    #CycleAmount is for the loop and the amount of repetition.
    cycleAmount = 350
    #Radius for the balls.
    ballRadius = 15

    #variable for the first ball.
    ball1 = Circle(randomPoint(ballRadius,win),ballRadius)
    ball1.setFill(randomColor())
    ball1.draw(win)

    #variable for the second ball.
    ball2 = Circle(randomPoint(ballRadius,win),ballRadius)
    ball2.setFill(randomColor())
    ball2.draw(win)

    #Change in direction variable.
    dx1 = getRandom(moveAmount)
    dy1 = getRandom(moveAmount)
    dx2 = getRandom(moveAmount)
    dy2 = getRandom(moveAmount)

    #loop for the hit boxes.
    for i in range(cycleAmount):
        #vertical collision for ball one.
        if(hitVertical(ball1,win) == True):
            dx1 = -dx1
        #vertical collision for ball two.
        if(hitVertical(ball2,win) == True):
            dx2 = -dx2
        #horizontal collision for ball one.
        if(hitHorizontal(ball1,win) == True):
            dy1 = -dy1
        #horizontal collision for ball two.
        if(hitHorizontal(ball2,win) == True):
            dy2 = -dy2
        #collisions for the balls colliding.
        if(didCollide(ball1,ball2) == True):
            dx1 = -dx1
            dx2 = -dx1
            dy1 = -dy1
            dy2 = -dy2

            ball1.setFill(randomColor())
            ball2.setFill(randomColor())
        #Moves the balls.
        ball1.move(dx1,dy1)
        ball2.move(dx2,dy2)
        #activates the delay for the movements.
        time.sleep(delay)
    win.getMouse()
    win.close()

main()  
