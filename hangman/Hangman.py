#Name: Austin Hollis
#hangman.py
#
#Problem: This function will be used to create a game of Hangman. It
#         will read a file to get the words and then create a game
#         based off of the length of the word and the words are
#         randomized.
#
#Certification of Authenticity:
#         I certify that this lab is entirely my own work, but I talked
#         about my code with Sarah and Eduardo.

import random

from graphics import *

#RETURNS A LIST OF STRINGS
def readFile():
    #Opens and reads a file.
    infile = open("wordList.txt", "r")
    #Variable for splitting the wordlist.
    wordList = infile.read().split()
    return wordList

#RETURNS A STRING
def randomWord():
    #Reads the file.
    wordList = readFile()
    #Chooses a random position in the file.
    secretWordPosition = random.randint(0,len(wordList)-1)
    #Selects the word of the random position that was chosen.
    secretWord = wordList[secretWordPosition]
    #Returns the word.
    return secretWord
    #print(secretWord)

def drawPiece(wrongLetters,win):
    #Adjusts the variable wrongLetters
    wrongLetters = len(wrongLetters) + 1
    
    #sets the winWidth and winHeight
    winWidth = win.getWidth()
    winHeight = win.getHeight()
    #The body of the hangman will align with this axis
    hangmanYAxis = winWidth/2

    #Checks for wrong letters and increases so that it draws each piece        
    if wrongLetters == 2:
            # Strike 2: Draw the head
            circle4=Circle(Point(hangmanYAxis,254),16)
            circle4.draw(win)
            
    elif wrongLetters == 3:
            # Strike 3: Draw the torso
            line5=Line(Point(hangmanYAxis,238),
                       Point(hangmanYAxis,180))
            line5.draw(win)
            
    elif wrongLetters == 4:
            # Strike 4: Draw the left arm
            line6=Line(Point(hangmanYAxis,225),
                         Point(hangmanYAxis-20,200))
            line6.draw(win)
            
    elif wrongLetters == 5:
            # Strike 5: Draw the right arm
            line7=Line(Point(hangmanYAxis,225),
                         Point(hangmanYAxis+20,200))
            line7.draw(win)
            
    elif wrongLetters == 6:
            # Strike 6: Draw the left leg
            line8=Line(Point(hangmanYAxis,180),
                         Point(hangmanYAxis-15,135))
            line8.draw(win)
            
    elif wrongLetters == 7:
            # Strike 7: Draw the right leg
            line9=Line(Point(hangmanYAxis,180),
                       Point(hangmanYAxis+15,135))
            line9.draw(win)

            # GAME OVER: Draw a face on our hangman guy
            # Draw his "X"-eyes
            line10=Line(Point(hangmanYAxis+7,260),
                          Point(hangmanYAxis+2,255))
            line10.draw(win)
            
            line11=Line(Point(hangmanYAxis+2,260),
                        Point(hangmanYAxis+7,255))
            line11.draw(win)
            
            line12=Line(Point(hangmanYAxis-7,260),
                          Point(hangmanYAxis-2,255))
            line12.draw(win)
            
            line13=Line(Point(hangmanYAxis-2,260),
                          Point(hangmanYAxis-7,255))
            line13.draw(win)

            # Draw his mouth
            line14=Line(Point(hangmanYAxis-7,247),
                          Point(hangmanYAxis+7,247))
            line14.draw(win)

#Function to get the word to guess.
def guessedWord(win,word):
    #sets the window width and window height
    winWidth = win.getWidth()
    winHeight = win.getHeight()
    
    print(word)
    #Gets the length of the word
    wordLength = len(word)
    #Creates the blank spaces for the word
    blanks = ["_"] * wordLength
    print(''.join(blanks))
    #print("")
    guessedLetters = []
    wrongLetters = []

    #Text for whether or not you win.
    winOrNotText = Text(Point(500,575), "")
    winOrNotText.draw(win)

    #Input box for the letter guesses
    winGuessInput = Entry(Point(winWidth/2+30,28),2)
    winGuessInput.draw(win)

    #Draws the blank spaces
    winGrid = Text(Point(winWidth/2,winHeight-70),''.join(blanks))
    winGrid.draw(win)

    #Coordinates for the hanging portion
    hangmanYAxis = winWidth/2
    line1=Line(Point(winWidth-winWidth/3,100),
               Point(winWidth-winWidth/3,300))
    line1.draw(win)
    
    line2=Line(Point(winWidth-winWidth/3,300),
               Point(hangmanYAxis,300))
    line2.draw(win)
    
    line3=Line(Point(hangmanYAxis,300),
               Point(hangmanYAxis,270))
    line3.draw(win)

    winGuessLetters = Text(Point(300,400),guessedLetters)
    winGuessLetters.draw(win)

    #Loop to check for the game parameters
    while len(wrongLetters) < 7 and (''.join(blanks) != word):
        win.getMouse()
        #Gets the guessed letter and sets it to lower case
        guess = winGuessInput.getText()
        guess = guess.lower()
        #If the guess has not been guessed before appends it to the list
        if guess not in guessedLetters:
            guessedLetters.append(guess)
            #create array with the blanks and remove/add letter in blank
            for i in range(len(word)):
                if word[i] == guess:
                    blanks.pop(i)
                    blanks.insert(i,guess)
        #Blanks out the line for the input to be ready for next guess
        winGuessInput.setText("")
        #If guess is not in the wrong letters list and not in the word
        #appends it to wrong letters list.
        if guess not in wrongLetters and guess not in word:
            wrongLetters.append(guess)
        #Used for Console Accuracy
        print("Guessed Letters: ", end="")
        print(guessedLetters)
        print("Wrong Letters: ", end="")
        print(wrongLetters)
        print(''.join(blanks))
        print("")
        
        winGrid.setText(''.join(blanks))
        winGuessLetters.setText(guessedLetters)
        #Draws the pieces of the hangman.
        drawPiece(wrongLetters,win)                

        

    if len(wrongLetters) == 7:
        winOrNotText.setText("You lose!")
    else:
        winOrNotText.setText("You win!")
    return blanks

def shouldPlayAgain():
    winWidth = 600
    winHeight = 600
    win = GraphWin("Whacky Upside Down Hangman",winWidth,winHeight)
    yesOrNoEntry = Entry(Point(win.getWidth() /2, win.getHeight()/ 2), 1)
    yesOrNoEntry.draw(win)
    win.getMouse()
    yesOrNo = yesOrNoEntry.getText()

    if yesOrNo == "y":
        playGame()
        win.close()
    else:
        win.close()
        quit()
    
def playGame():
    #Sets the window
    winWidth = 600
    winHeight = 600
    win = GraphWin("Whacky Upside Down Hangman",winWidth,winHeight)
    play = True
    while play == True:
        #Gets the random word and length of it
        word = randomWord()
        wordLength = len(word)
        blanks = ["_ "] * wordLength
        
        #Draw the game message area, the ground of the
        #Hangman graphic, and the empty grid
        winMessage = Text(Point(winWidth/2,70),
                           "Guess a letter to see if it's in the word.")
        winMessage.setStyle('bold')
        winMessage.draw(win)
        
        #Draws the ground that is upside down.
        winGround = Line(Point(winWidth/10,100),
                         Point(winWidth-winWidth/10,100))
        winGround.draw(win)
        
        #Draw the input box and accompanying text label
        winGuessTxt = Text(Point(winWidth/2-35,30), "Type a letter:")
        winGuessTxt.draw(win)
        
        #Draw the "Guess it!" button and its label
        winButGuess = Rectangle(Point(winWidth/2+55,43),
                                 Point(winWidth/2+130,13))
        #Sets the color of the inside and the border of the button.
        winButGuess.setFill(color_rgb(126,236,53))
        winButGuess.setOutline(color_rgb(0,110,0))
        winButGuess.draw(win)
        winButGuessLabel = Text(Point(winWidth/2+94,28), 'Guess it!')
        winButGuessLabel.setTextColor(color_rgb(0, 110, 0))
        winButGuessLabel.draw(win)
        #Runs the guessedWord Function
        guessedWord(win,word)
        win.close()
        play = shouldPlayAgain()

    
def main():
    playGame()
    
main()
