#Name: Austin Hollis
#fallGreeting.py
##Use fallGreeting() to call function.
#
#Problem: This function will be used to create a fall greeting
#         card that contains a jack-o-lantern and other items
#         using the graphics package. Within the program will contain
#         a flickering effect and other extra items.
#
#Certification of Authenticity:
#   I certify that this lab is entirely my own work.
#

from graphics import *

def fallGreeting():
    
###Graphic Window Portion###
    #Below goup of code sets the dimensions of the graphic window.
    winWidth = 800
    winHeight = 600
    win = GraphWin("My Fall Greeting Card", winWidth, winHeight)

###Sky Portion###
    #Creates the sky and colors it midnight blue and draws it.
    sky = Polygon(Point(0,0), Point(800,0), Point(800,250),
                  Point(0,250))
    sky.setFill("midnightblue")
    sky.draw(win)

###Witch Portion###
    #Points acquired after tracing the witch image.
    witch = Polygon(Point(207,132), Point(238,146), Point(243,145),
                    Point(241,147), Point(245,153), Point(253,155),
                    Point(247,159), Point(247,164), Point(241,164),
                    Point(242,168), Point(236,168), Point(238,180),
                    Point(250,183), Point(285,176), Point(285,181),
                    Point(241,197), Point(245,203), Point(240,211),
                    Point(219,217), Point(211,220), Point(200,230),
                    Point(206,208), Point(211,211), Point(215,205),
                    Point(201,210), Point(201,213), Point(194,215),
                    Point(175,228), Point(166,235), Point(157,225),
                    Point(156,214), Point(162,210), Point(188,211),
                    Point(197,204), Point(200,206), Point(215,201),
                    Point(215,198), Point(208,199), Point(207,189),
                    Point(219,164), Point(230,161), Point(228,158),
                    Point(224,159), Point(227,155), Point(207,131))
    #Draws and colors the witch a black color.
    witch.setFill("black")
    witch.draw(win)

###Ground Portion###
    #Below are the points used to create the ground.
    ground = Polygon(Point(0,250), Point(0,600), Point(800,600),
                     Point(800,250))
    #Colors the ground green.
    ground.setFill("green")
    #Draws the ground.
    ground.draw(win)

###Moon Portion###
    #Points used to create the moon.
    moon = Circle(Point(750,50),25)
    #Colors the moon gold.
    moon.setFill("gold")
    #Draws the moon.
    moon.draw(win)

###Body Section###
    #Points used to create the pumpkin body.
    pumpkinBody = Circle(Point(400,400),200)
    #Colors the pumpkin orange.
    pumpkinBody.setFill("Orange")
    #Draws the pumpkin.
    pumpkinBody.draw(win)

###Right Eye Section###
    #Points used to create the right eye.
    rightEye = Polygon(Point(490,270), Point(430,375), Point(550,375))
    #Outlines the right eye orange.
    rightEye.setOutline("orange")
    #Colors the right eye black.
    rightEye.setFill("Black")
    #Draws the right eye.
    rightEye.draw(win)

###Left Eye Section###
    #Points used to create the left eye.
    leftEye = Polygon(Point(310,270), Point(250,375), Point(370,375))
    #Outlines the left eye orange.
    leftEye.setOutline("orange")
    #Colors the left eye black.
    leftEye.setFill("Black")
    #Draws the left eye.
    leftEye.draw(win)

###Nose Section###
    #Points used to create the nose.
    nose = Polygon(Point(400,375), Point(370,450), Point(430,450))
    #Colors the nose black.
    nose.setFill("black")
    #Outlines the nose black.
    nose.setOutline("black")
    #Draws the nose.
    nose.draw(win)

###Mouth Section###
    #Points used to create the mouth.
    mouth = Polygon(Point(290,480), Point(340,480), Point(340,500),
                    Point(375,500), Point(375,480), Point(425,480),
                    Point(425,500), Point(460,500), Point(460,480),
                    Point(510,480), Point(480,520), Point(440,540),
                    Point(415,540), Point(415,520), Point(385,520),
                    Point(385,540), Point(350,540), Point(310,520),
                    Point(290,480))
    #Outlines the mouth black.
    mouth.setOutline("black")
    #Colors the mouth black.
    mouth.setFill("Black")
    #Draws the mouth.
    mouth.draw(win)

###Stem Portion###
    #Points used to create the stem.
    stem = Polygon(Point(380,200), Point(420,200), Point(420,160),
                   Point(380,160))
    #Outlines the stem in black.
    stem.setOutline("black")
    #Colors the stem a brown color.
    stem.setFill("saddlebrown")
    #Draws the stem.
    stem.draw(win)

###Tree Branch Portion###
    #Points used to create the top left branch.
    branchTopLeft = Polygon(Point(0,82),Point(22,35),Point(55,10),
                     Point(27,36),Point(16,62),Point(41,62),
                     Point(77,41),Point(83,13),Point(84,43),
                     Point(71,51),Point(124,49),Point(56,61),
                     Point(44,70),Point(17,70),Point(13,79),
                     Point(33,91),Point(13,89),Point(0,106))
    #Outlines the top left branch black.
    branchTopLeft.setOutline("black")
    #Colors the top left branch black.
    branchTopLeft.setFill("black")
    #Draws the top left branch.
    branchTopLeft.draw(win)

    #Points used to create the middle left branch.
    branchMiddleLeft = Polygon(Point(0,282),Point(22,235),
                               Point(55,210),Point(27,236),
                               Point(16,262),Point(41,262),
                               Point(77,241),Point(83,213),
                               Point(84,243),Point(71,251),
                               Point(124,249),Point(56,261),
                               Point(44,270),Point(17,270),
                               Point(13,279),Point(33,291),
                               Point(13,289),Point(0,306))
    #Outlines the middle left branch black.
    branchMiddleLeft.setOutline("black")
    #Colors the middle left branch black.
    branchMiddleLeft.setFill("black")
    #Draws the middle left branch.
    branchMiddleLeft.draw(win)

    #Points used to create the middle right branch.
    branchMiddleRight = Polygon(Point(800,300), Point(745,275),
                                Point(780,300), Point(738,290),
                                Point(730,275), Point(725,275),
                                Point(722,263), Point(730,255),
                                Point(720,260), Point(720,270),
                                Point(690,275), Point(710,275),
                                Point(700,280), Point(720,280),
                                Point(725,280), Point(730,295),
                                Point(760,300), Point(800,310))
    #Outlines the middle right branch.
    branchMiddleRight.setOutline("black")
    #Colors the middle right branch black.
    branchMiddleRight.setFill("black")
    #Draws the middle right branch.
    branchMiddleRight.draw(win)

###Tree Portion###
    #Points used to create the tree.
    tree = Polygon(Point(440,348), Point(455,314), Point(468,312),
                   Point(482,299), Point(485,280), Point(497,271),
                   Point(483,280), Point(480,296), Point(466,306),
                   Point(457,305), Point(470,287), Point(453,301),
                   Point(438,330), Point(419,335), Point(409,305),
                   Point(397,289), Point(418,292), Point(399,280),
                   Point(401,271), Point(429,269), Point(469,242),
                   Point(467,214), Point(461,242), Point(426,264),
                   Point(396,261), Point(387,281), Point(397,303),
                   Point(395,326), Point(349,278), Point(377,316),
                   Point(388,337), Point(420,365), Point(397,366),
                   Point(408,368), Point(363,381), Point(418,374),
                   Point(407,382), Point(425,377), Point(438,377),
                   Point(451,381), Point(477,384), Point(455,375),
                   Point(486,377), Point(461,369), Point(443,355))
    #Colors the tree black.
    tree.setFill("black")
    #Moves the tree to the right 200 pixels and up 120 pixels.
    tree.move(200,-120)
    #Draws the tree.
    tree.draw(win)

###Stars Portion###
    #Below is coding used for each star in the sky.
    #First line in each set is used to create a point for a star.
    #Second line in each set is used to turn the point to a white color.
    #Third line in each set is used to draw each point.
    star1 = Point(45,55)
    star1.setFill("white")
    star1.draw(win)

    star2 = Point(80,89)
    star2.setFill("white")
    star2.draw(win)

    star3 = Point(125,57)
    star3.setFill("white")
    star3.draw(win)

    star4 = Point(148,82)
    star4.setFill("white")
    star4.draw(win)

    star5 = Point(169,31)
    star5.setFill("white")
    star5.draw(win)

    star6 = Point(197,67)
    star6.setFill("white")
    star6.draw(win)

    star7 = Point(240,22)
    star7.setFill("white")
    star7.draw(win)

    star8 = Point(289,33)
    star8.setFill("white")
    star8.draw(win)

    star9 = Point(278,58)
    star9.setFill("white")
    star9.draw(win)

    star10 = Point(335,76)
    star10.setFill("white")
    star10.draw(win)

    star11 = Point(356,29)
    star11.setFill("white")
    star11.draw(win)

    star12 = Point(389,96)
    star12.setFill("white")
    star12.draw(win)

    star13 = Point(404,53)
    star13.setFill("white")
    star13.draw(win)

    star14 = Point(456,25)
    star14.setFill("white")
    star14.draw(win)

    star15 = Point(478,40)
    star15.setFill("white")
    star15.draw(win)

    star16 = Point(453,69)
    star16.setFill("white")
    star16.draw(win)

    star17 = Point(505,55)
    star17.setFill("white")
    star17.draw(win)

    star18 = Point(523,19)
    star18.setFill("white")
    star18.draw(win)
    
    star19 = Point(542,89)
    star19.setFill("white")
    star19.draw(win)

    star20 = Point(569,27)
    star20.setFill("white")
    star20.draw(win)

    star21 = Point(595,57)
    star21.setFill("white")
    star21.draw(win)

    star22 = Point(649,91)
    star22.setFill("white")
    star22.draw(win)

    star23 = Point(692,67)
    star23.setFill("white")
    star23.draw(win)

    star24 = Point(740,82)
    star24.setFill("white")
    star24.draw(win)

    star25 = Point(792,15)
    star25.setFill("white")
    star25.draw(win)

    star26 = Point(663,46)
    star26.setFill("white")
    star26.draw(win)

    star27 = Point(637,27)
    star27.setFill("white")
    star27.draw(win)

###Happy Fall Text Portion###
    #Below creates a text point and message and sets the size to 20,
    #and colors the text red and then creates the text on screen.
    message = Text(Point(400,100), "Happy Fall!")
    message.setSize(20)
    message.setTextColor("red")
    message.draw(win)

###Flickering Light Color Loop###
    #Begins the loop for a flickering effect.
    for color in range(5):
        #Colors the mouth, eyes and nose yellow.
        mouth.setFill("yellow")
        rightEye.setFill("yellow")
        leftEye.setFill("yellow")
        nose.setFill("yellow")
        #Creates a flickering effect with a 4/10ths of a second pause.
        time.sleep(0.4)
        #Colors the mouth, eyes and nose red.
        mouth.setFill("red")
        rightEye.setFill("red")
        leftEye.setFill("red")
        nose.setFill("red")
        #Creates the flickering effect with a 4/10ths of a second pause.
        time.sleep(0.4)

###Lightning Portion###
    #Points used to create the 1st lightning bolt.
    lightning1 = Polygon(Point(430,0),Point(439,0),
                        Point(435,10),Point(443,10),
                        Point(425,75),Point(434,23),
                        Point(425,23),Point(430,0))
    #Colors the 1st lightning bolt yellow.
    lightning1.setFill("yellow")
    #Draws the 1st lightning bolt.
    lightning1.draw(win)

    #Points used to create the 2nd lightning bolt.
    lightning2 = Polygon(Point(236,0),Point(246,0),
                         Point(240,15),Point(252,15),
                         Point(231,80),Point(240,36),
                         Point(231,23),Point(236,0))
    #Colors the 2nd lightning bolt yellow.
    lightning2.setFill("yellow")
    #Draws the 2nd lightning bolt.
    lightning2.draw(win)
    #Creates a 2/10ths of a second pause for a flash effect.
    time.sleep(0.2)

###Lightning Flash Portion###
    #Points used to create a flash effect.
    flash = Polygon(Point(0,0),Point(0,600),Point(800,600),
                    Point(800,0))
    #Colors the flash white.
    flash.setFill("white")
    #Draws the flash.
    flash.draw(win)
    #Has the flash last 1/10th of a second.
    time.sleep(0.1)

###Sky Portion###
    #Points used to create the sky.
    sky = Polygon(Point(0,0), Point(800,0), Point(800,250),
                  Point(0,250))
    #Colors the sky midnight blue.
    sky.setFill("midnightblue")
    #Draws the sky.
    sky.draw(win)

###Ground Portion###
    #Points used to create the ground.
    ground = Polygon(Point(0,250), Point(0,600), Point(800,600),
                     Point(800,250))
    #Colors the ground green.
    ground.setFill("green")
    #Draws the ground.
    ground.draw(win)

###Moon Portion###
    #Points used to create the moon.
    moon = Circle(Point(750,50),25)
    #Colors the moon gold.
    moon.setFill("gold")
    #Draws the moon.
    moon.draw(win)

###Body Section###
    #Points used to create the body.
    pumpkinBody = Circle(Point(400,400),200)
    #Colors the pumpkin orange.
    pumpkinBody.setFill("Orange")
    #Draws the pumpkin.
    pumpkinBody.draw(win)

###Right Eye Section###
    #Points used to create the right eye.
    rightEye = Polygon(Point(490,270), Point(430,375), Point(550,375))
    #Outlines the right eye orange.
    rightEye.setOutline("orange")
    #Colors the right eye yellow.
    rightEye.setFill("yellow")
    #Draws the right eye.
    rightEye.draw(win)

###Left Eye Section###
    #Points used to draw the left eye.
    leftEye = Polygon(Point(310,270), Point(250,375), Point(370,375))
    #Outlines the left eye in orange.
    leftEye.setOutline("orange")
    #Colors the left eye yellow.
    leftEye.setFill("yellow")
    #Draws the left eye.
    leftEye.draw(win)

###Nose Section###
    #Points acquired after tracing the nose.
    nose = Polygon(Point(400,375), Point(370,450), Point(430,450))
    #Colors the nose yellow.
    nose.setFill("yellow")
    #Outlines the nose in an orange color.
    nose.setOutline("orange")
    #Draws the nose.
    nose.draw(win)

###Mouth Section###
    #Points acquired after tracing the mouth.
    mouth = Polygon(Point(290,480), Point(340,480), Point(340,500),
                    Point(375,500), Point(375,480), Point(425,480),
                    Point(425,500), Point(460,500), Point(460,480),
                    Point(510,480), Point(480,520), Point(440,540),
                    Point(415,540), Point(415,520), Point(385,520),
                    Point(385,540), Point(350,540), Point(310,520),
                    Point(290,480))
    #Outlines the mouth in a black color.
    mouth.setOutline("black")
    #Fills the mouth a yellow color to start with.
    mouth.setFill("yellow")
    #Draws the mouth of the pumpkin.
    mouth.draw(win)

###Stem Portion###
    #Points used to create the stem.
    stem = Polygon(Point(380,200), Point(420,200), Point(420,160),
                   Point(380,160))
    #Outlines the stem in black.
    stem.setOutline("black")
    #Colors the stem a brown color.
    stem.setFill("saddlebrown")
    #Draws the stem on the pumpkin.
    stem.draw(win)

###Tree Branch Portion###
    #Below are the points acquired after tracing the image.
    branchTopLeft = Polygon(Point(0,82),Point(22,35),Point(55,10),
                     Point(27,36),Point(16,62),Point(41,62),
                     Point(77,41),Point(83,13),Point(84,43),
                     Point(71,51),Point(124,49),Point(56,61),
                     Point(44,70),Point(17,70),Point(13,79),
                     Point(33,91),Point(13,89),Point(0,106))
    #Below is used to set the outline to black.
    branchTopLeft.setOutline("black")
    #Below is used to color the branch at the top right black.
    branchTopLeft.setFill("black")
    #Below is used to draw the figure.
    branchTopLeft.draw(win)

    #Below are the points acquired after tracing the image.
    branchMiddleLeft = Polygon(Point(0,282),Point(22,235),
                               Point(55,210),Point(27,236),
                               Point(16,262),Point(41,262),
                               Point(77,241),Point(83,213),
                               Point(84,243),Point(71,251),
                               Point(124,249),Point(56,261),
                               Point(44,270),Point(17,270),
                               Point(13,279),Point(33,291),
                               Point(13,289),Point(0,306))
    #Below is used to set the outline color to black.
    branchMiddleLeft.setOutline("black")
    #Below is used to color the branch in the top middle black.
    branchMiddleLeft.setFill("black")
    #Below is used to draw the figure.
    branchMiddleLeft.draw(win)

    #Below are the point acquired when tracing the middle right branch.
    branchMiddleRight = Polygon(Point(800,300), Point(745,275),
                                Point(780,300), Point(738,290),
                                Point(730,275), Point(725,275),
                                Point(722,263), Point(730,255),
                                Point(720,260), Point(720,270),
                                Point(690,275), Point(710,275),
                                Point(700,280), Point(720,280),
                                Point(725,280), Point(730,295),
                                Point(760,300), Point(800,310))
    #Outlines the image in black.
    branchMiddleRight.setOutline("black")
    #Colors the image a black color.
    branchMiddleRight.setFill("black")
    #Draws the image on screen.
    branchMiddleRight.draw(win)

###Witch Portion###
    #Below are the points acquired when tracing the witch image.
    witch = Polygon(Point(207,132), Point(238,146), Point(243,145),
                    Point(241,147), Point(245,153), Point(253,155),
                    Point(247,159), Point(247,164), Point(241,164),
                    Point(242,168), Point(236,168), Point(238,180),
                    Point(250,183), Point(285,176), Point(285,181),
                    Point(241,197), Point(245,203), Point(240,211),
                    Point(219,217), Point(211,220), Point(200,230),
                    Point(206,208), Point(211,211), Point(215,205),
                    Point(201,210), Point(201,213), Point(194,215),
                    Point(175,228), Point(166,235), Point(157,225),
                    Point(156,214), Point(162,210), Point(188,211),
                    Point(197,204), Point(200,206), Point(215,201),
                    Point(215,198), Point(208,199), Point(207,189),
                    Point(219,164), Point(230,161), Point(228,158),
                    Point(224,159), Point(227,155), Point(207,131))
    #Below coding is used to fill in the witch with a black color.
    witch.setFill("black")
    #Below coding is used to draw the witch figure.
    witch.draw(win)

###Tree Portion###
    #Below are the points acquired from a tree image after tracing it.
    tree = Polygon(Point(440,348), Point(455,314), Point(468,312),
                   Point(482,299), Point(485,280), Point(497,271),
                   Point(483,280), Point(480,296), Point(466,306),
                   Point(457,305), Point(470,287), Point(453,301),
                   Point(438,330), Point(419,335), Point(409,305),
                   Point(397,289), Point(418,292), Point(399,280),
                   Point(401,271), Point(429,269), Point(469,242),
                   Point(467,214), Point(461,242), Point(426,264),
                   Point(396,261), Point(387,281), Point(397,303),
                   Point(395,326), Point(349,278), Point(377,316),
                   Point(388,337), Point(420,365), Point(397,366),
                   Point(408,368), Point(363,381), Point(418,374),
                   Point(407,382), Point(425,377), Point(438,377),
                   Point(451,381), Point(477,384), Point(455,375),
                   Point(486,377), Point(461,369), Point(443,355))
    #Below coding is used to turn the tree to a black color.
    tree.setFill("black")
    #This code is used to slide the tree a certain amount of pixels.
    tree.move(200,-120)
    #Below is used to draw the tree.
    tree.draw(win)

###Stars Portion###
    #Below is coding used for each star in the sky.
    #First line in each set is used to create a point for a star.
    #Second line in each set is used to turn the point to a white color.
    #Third line in each set is used to draw each point.
    star1 = Point(45,55)
    star1.setFill("white")
    star1.draw(win)

    star2 = Point(80,89)
    star2.setFill("white")
    star2.draw(win)

    star3 = Point(125,57)
    star3.setFill("white")
    star3.draw(win)

    star4 = Point(148,82)
    star4.setFill("white")
    star4.draw(win)

    star5 = Point(169,31)
    star5.setFill("white")
    star5.draw(win)

    star6 = Point(197,67)
    star6.setFill("white")
    star6.draw(win)

    star7 = Point(240,22)
    star7.setFill("white")
    star7.draw(win)

    star8 = Point(289,33)
    star8.setFill("white")
    star8.draw(win)

    star9 = Point(278,58)
    star9.setFill("white")
    star9.draw(win)

    star10 = Point(335,76)
    star10.setFill("white")
    star10.draw(win)

    star11 = Point(356,29)
    star11.setFill("white")
    star11.draw(win)

    star12 = Point(389,96)
    star12.setFill("white")
    star12.draw(win)

    star13 = Point(404,53)
    star13.setFill("white")
    star13.draw(win)

    star14 = Point(456,25)
    star14.setFill("white")
    star14.draw(win)

    star15 = Point(478,40)
    star15.setFill("white")
    star15.draw(win)

    star16 = Point(453,69)
    star16.setFill("white")
    star16.draw(win)

    star17 = Point(505,55)
    star17.setFill("white")
    star17.draw(win)

    star18 = Point(523,19)
    star18.setFill("white")
    star18.draw(win)
    
    star19 = Point(542,89)
    star19.setFill("white")
    star19.draw(win)

    star20 = Point(569,27)
    star20.setFill("white")
    star20.draw(win)

    star21 = Point(595,57)
    star21.setFill("white")
    star21.draw(win)

    star22 = Point(649,91)
    star22.setFill("white")
    star22.draw(win)

    star23 = Point(692,67)
    star23.setFill("white")
    star23.draw(win)

    star24 = Point(740,82)
    star24.setFill("white")
    star24.draw(win)

    star25 = Point(792,15)
    star25.setFill("white")
    star25.draw(win)

    star26 = Point(663,46)
    star26.setFill("white")
    star26.draw(win)

    star27 = Point(637,27)
    star27.setFill("white")
    star27.draw(win)

###Happy Fall Text Portion###
    #Below creates a text point and message and sets the size to 20,
    #and colors the text red and then creates the text on screen.
    message = Text(Point(400,100), "Happy Fall!")
    message.setSize(20)
    message.setTextColor("red")
    message.draw(win)

###Click To Close Box###
    #Sets the X-Coordinate of the button.
    boxPtX = 675
    #Sets the Y-Coordinate of the button.
    boxPtY = 550
    #Creates the border of the button.
    border = Rectangle(Point(boxPtX-110, boxPtY-15),
                       Point(boxPtX+110, boxPtY+15))
    #Colors the button grey.
    border.setFill("grey")
    #Creates the text inside the box and places the center of the text.
    button = Text(Point(boxPtX, boxPtY), "Click anywhere to close")
    #Draws the border.
    border.draw(win)
    #Draws the button on the scree.
    button.draw(win)

###Closing the Window###
    #Waits for a click from the user to close the window.
    win.getMouse()
    #Closes window.
    win.close()
fallGreeting()
