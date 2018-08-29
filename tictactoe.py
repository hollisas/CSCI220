#Name: 
#tictactoe.py
#
#Problem: This program will be used to create a game of tic-tac-toe.
#         The game will be played between two human players.
#Certification of Authenticity:
#         I certify that this lab is entirely my own work.

from random import *

#Creates the list for the numbers that are seen and shown to the player.
def createBoard():
    board = ["1","2","3","4","5","6","7","8","9"]
    return board

#Draws the board
def drawBoard(board):
    print("   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |")

#Asks for the letter of the player.
def inputPlayerLetter():
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()

    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]

#Randomly decides the first player to go.
def firstMove():
    if randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"

#Asks if the players would like to play again.
def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")

#Makes the position of the board based on the spot the player chooses,
#to become the letter of the player.
def makeMove(board,letter,move):
    board[move] = letter

#Checks for any chances to be a winner.
def isWinner(board,letter):
    #Returns value of True for a winner if the letters are the same in
    #the form of a straight line either vertically, horizontally, or
    #diagonally.
    #Horizontal Top
    if (board[0]==letter and board[1]==letter and board[2]==letter):
        winner = True
    #Horizontal Middle
    elif (board[3]==letter and board[4]==letter and board[5]==letter):
        winner = True
    #Horizontal Bottom
    elif (board[6]==letter and board[7]==letter and board[8]==letter):
        winner = True
    #Vertical Left
    elif (board[0]==letter and board[3]==letter and board[6]==letter):
        winner = True
    #Vertical Middle
    elif (board[1]==letter and board[4]==letter and board[7]==letter):
        winner = True
    #Vertical Right
    elif (board[2]==letter and board[5]==letter and board[8]==letter):
        winner = True
    #Diagonal from Top Left to Bottom Right
    elif (board[0]==letter and board[4]==letter and board[8]==letter):
        winner = True
    #Diagonal from Top Right to Bottom Left
    elif (board[2]==letter and board[4]==letter and board[6]==letter):
        winner = True
    #If none match there is no winner
    else:
        winner = False
    return winner

#Checks for free spaces that have not been taken by other player.
def freeSpace(board, move):
    if board[move] in "1 2 3 4 5 6 7 8 9".split():
        emptySpace = True
    else:
        emptySpace = False
    return emptySpace

#Function for player one's move.
def playerOneMove(board):
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not freeSpace(board,
                                                                   int(move)-1):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)

#Function for player two's move.
def playerTwoMove(board):
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not freeSpace(board,
                                                                   int(move)-1):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)

#Function for the board to continue drawing the board until there
#no more free spaces.
def fullBoard(board):
    for i in range(1,10):
        if freeSpace(board,i):
            return False
    return True

#Function to play the game
def doPlay():
    #If this is true the game plays.
    gamePlay = True
    #While the game is playing the board is created the letters are
    #assigned and the first turn is taken.
    while gamePlay == True:
        #Creates the board
        theBoard = createBoard()
        #Assigns the letters
        playerOneLetter, playerTwoLetter = inputPlayerLetter()
        #Takes the first turn
        turn = firstMove()
        print(turn + " will go first.")
        gameIsPlaying = True

        #While the game is being played it switches between player one
        #and player two. Each turn has the board drawn, a move taken and
        #checks for a winner and if no winner is found goes to the next
        #person.
        while gameIsPlaying == True:
            if turn == "Player one":
                drawBoard(theBoard)
                move = playerOneMove(theBoard) - 1
                makeMove(theBoard, playerOneLetter, move)

                if isWinner(theBoard, playerOneLetter):
                    drawBoard(theBoard)

                    print(playerOneLetter + "'s have won the game!")
                    gameIsPlaying = False
                else:
                    if fullBoard(theBoard):
                        drawBoard(theBoard)
                        print("The game is a tie!")
                        gameIsPlaying = False
                    else:
                        turn = "Player two:"
            else:
                drawBoard(theBoard)
                move = playerTwoMove(theBoard) - 1
                
                makeMove(theBoard, playerTwoLetter, move)

                if isWinner(theBoard, playerTwoLetter):
                    drawBoard(theBoard)
                    print("The " + playerTwoLetter + "'s have won the game!")
                    gameIsPlaying = False
                else:
                    turn = "Player one"
        #Asks if they would like to play again.
        if not playAgain():
            rtnValue = False

def main():
    #Initially draws the board and plays the game.
    board = createBoard()
    drawBoard(board)
    doPlay()
    
main()
                        
