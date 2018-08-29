#Name: Austin Hollis
#mean.py
##Use calcMean() to call function.
#
#Problem: This function will be used to calculate the mean,
#         the root mean square and the harmonic mean based on
#         given information input by the user.
#
#Certification of Authenticity:
#   I certify that this lab is entirely my own work.
#
"""---Questions 1-3---
Question 1: The program will be able to calculate the mean,
root mean square and the harmonic mean based on given information
that is input by the user.

Question 2: The inputs will be the number of terms that are in
the problem and the numbers themselves that need to be added
together before they are divided. The outputs will be the mean,
the harmonic mean, the root mean square and the sum of the numbers
that are added together before dividing by the total 'n' value to
ensure accuracy on both ends (user and programming wise).

Question 3: The program must first tell the user what it does.
The program must then ask the user to input the amount of numbers 
in the set. Once the program gets the amount of numbers in the set
it can perform the loop. Outside the loop the totals must be set for
each total; the meanTotal, the rmsTotal, and the harmonicTotal.
inside the loop the program will ask for the individual values of
each number in the set. Then the program will adjust the totals
depending on the formula that is being used in the adjustment for
the different means. Then the program will print out each mean for
the user.
"""

#Imports the math library for the use of square root.
import math

#Function used to calculate the mean.
def calcMean():
    #Tells the user what the program will do.
    print("This program will help you calculate the mean,", end = " ")
    print("the root mean square and the harmonic mean", end = " ")
    print("based on information given by you!")
    #Used to add a line break.
    print()
    #Variable asking the user to input the total amount of numbers
    #being used in the set.
    numTerms = eval(input("Enter the number of terms in the set: "))
    #Initiates the beginning of the mean total.
    meanTotal = 0
    #rms is Root Mean Square but abbreviated.
    #Initiates the beginning for the rmsAverage total.
    rmsTotal = 0
    #Initiates the beginning for the harmonicMean total.
    harmonicTotal = 0
    #Used to add a line break.
    print()
    #Begins the loop.
    for i in range(numTerms):
        #Asks the user to input the set of numbers being used.
        numValues = eval(input("Enter the number values in the set: "))
        #Formula to get the sum of the numbers.
        meanTotal = meanTotal + numValues
        #Prints out the sum as meanTotal progresses to ensure
        #accuracy. Also for error checking.
        print("The sum so far is: ", meanTotal)
        #Adds a break line.
        print()
        #Formula to get the average.
        mean = meanTotal / numTerms
        #Formula to square each value in the set, as it is entered,
        #before adding them together, also adjusts rmsTotal since it
        #is inside the loop. Is also the Root Mean Square sum.
        rmsTotal = rmsTotal + numValues**2
        #Variable to incorporate the square root function.
        sqrt = math.sqrt
        #Variable for root mean square is rmsAverage
        rmsAverage = sqrt(rmsTotal/numTerms)
        #Adjusts the harmonicTotal since it is inside the loop.
        #Is also the Harmonic sum as well.
        harmonicTotal = harmonicTotal + (1/numValues)
        #Formula for the harmonic mean.
        harmonicMean = numTerms / harmonicTotal
    #Prints out the mean.
    print("The Mean is:", mean)
    #Prints out the Root Mean Square.
    print("The Root Mean Square:", rmsAverage)
    #Prints out the Harmonic Mean.
    print("The Harmonic Mean is:", harmonicMean)
