#Name: Austin Hollis
#cdTime.py
###Call the function using calcTime()###
#
#Problem: The problem that I am addressing is the need to calculate
#         the total times of songs on different CDs and add the total
#         times together in order to show the combined times of the CDs
#         based on the lengths of the tracks on the CDs. The total
#         time will be output in terms of Hours::Minutes::Seconds.
#
#
#Certification of Authenticity:
#   I certify that this lab is entirely of my own work. However,
#   I met with Dr. Stalvey once to ensure I was doing loops correctly.

#Variable name for the function.
def calcTime():
    print("This function will help you find the total", end = " ")
    print("amount of time on a CD with a given amount", end = " ")
    print("information regarding the number of songs", end = " ")
    print("and the length of each song.")
    #These print lines tell the user what the function will do.
    print()
    #Adds a line break to make it easier to read.
    numCD = eval(input("How many CD's do you have: "))
    #numCD is the variable for the amount of CDs that the user has.
    overallTotal = 0
    #Initial total of CDs.
    numMin = 0
    #numMin is the variable for the number of minutes.
    #Sets the start of this variable to 0.
    numSec = 0
    #numSec is the variable for the number of seconds.
    #Sets the start of this variable to 0.
    print()
    #Adds a blank line to make it easier to follow.
    for i in range(numCD):
        #This is the external loop.
        print("CD:", i+1)
        #Prints what number CD the user is on.
        numSongs = eval(input("How many tracks are on the CD: "))
        #Asks the user to input the amount of songs on each CD.
        for i in range(numSongs):
            #This is the internal loop.
            print("Track:", i+1)
            numMin=numMin+eval(input("How many minutes in the track: "))
            #Asks the user how many minutes each song has.
            #Adds the previous number of this variable to the next
            #number of this variable.
            numSec=numSec+eval(input("How many seconds in the track: "))
            #Asks the user to input how many seconds are in the track.
            #Adds the previous number of this variable to the next
            #number of this variable.
            print()
            #Prints a blank line to make it easier to read.
        secondsTotal = numMin * 60 + numSec
        #Formula to get the total number of seconds.
        minutes = secondsTotal // 60
        #Formula used to get the total number of minutes.
        seconds = secondsTotal % 60
        #Formula used to get the total number of seconds.
        hours = (minutes // 60) % 60
        #Formula used to get the total number of hours.
        printedMinutes = minutes % 60
        #New variable to make the printed line less characters.
        #This new variable essentially means that this will be what is
        #used to print out the time log at the very end.
        print("Total time is:", hours, "Hours", end = " ")
        print(printedMinutes, "Minutes", seconds, "Seconds")
        #Prints out the total time on the CD's combined.
        print()
        #This print line adds a blank line between each CD to make
        #reading easier.
