#Name: Austin Hollis
#weightedAverage.py
#Use calcGrades() to call the function to work
#
#Problem: This function will be used to open a file of grades
#         and calculate the average of each person and give the
#         class average as well.
#
#
#Certification of Authenticity:
#   I certify that this lab is entirely my own work.

#Imports the os libraries.
import os

#Variable name for the function
def calcGrades():
    #Tells the user what the function does.
    print("This function will calculate the grades of each", end = " ")
    print("student and will also calculate the class average.")
    #Asks the user for the file name.
    infileName = input("What file are the names and grades in: ")
    #Opens th file and reads it.
    infile = open(infileName, "r")
    #Opens the file as well for the user to see the data.
    os.system(infileName)
    #Variable for Billy's name.
    billyName = str("Billy Bother's")
    #Variable for weights of Billy's grades.
    billyWeights = [20, 30, 50]
    #Variable for Billy's grades.
    billyGrades = [89, 94, 82]
    #Initializes the total for the loop.
    billyTotal = 0
    #Loop for Billy's Average. Zip command groups the lists together.
    for grades, weights in zip(billyGrades, billyWeights):
        #Adjustment for Billy's Total.
        billyTotal += grades * weights
    #Variable for Billy's Average.
    billyAvg = billyTotal / sum(billyWeights)
    #Variable for Hermione's name.
    hermioneName = str("Hermione Heffalump's")
    #Variable for Hermione's weights for grades.
    hermioneWeights = [40, 60]
    #Variable for Hermione's Grades.
    hermioneGrades = [93, 97]
    #Adjusts the total for Hermione's loop.
    hermioneTotal = 0
    #The loop for Hermione's grades.
    for grades, weights in zip(hermioneGrades, hermioneWeights):
        #Adjustment fo Hermione's total.
        hermioneTotal += grades * weights
    #Variable for Hermione's average.
    hermioneAvg = hermioneTotal / sum(hermioneWeights)
    #Variable to store Kurt's name as a string.
    kurtName = str("Kurt Kidd's")
    #Variable for the weight of Kurt's grades.
    kurtWeights = [20, 30, 40, 10]
    #Variable for Kurt's grades.
    kurtGrades = [88, 82, 76, 99]
    #Adjustment for Kurt's total.
    kurtTotal = 0
    #Loop for Kurt's grades.
    for grades, weights in zip(kurtGrades, kurtWeights):
        #Adjustment for Kurt's grades.
        kurtTotal += grades * weights
    #Variable for Kurt's average.
    kurtAvg = kurtTotal / sum(kurtWeights)
    #Variable to store Smarty's name.
    smartyName = str("Smarty Pants'")
    #Variable to store the list of the weights of Smarty's grades.
    smartyWeights = [100]
    #Variable for Smarty's grades.
    smartyGrades = [100]
    #Adjustment for the loop.
    smartyTotal = 0
    #Loop for Smarty's grades.
    for grades, weights in zip(smartyGrades, smartyWeights):
        #Adjustment for Smarty's grades.
        smartyTotal += grades * weights
    #Variable for Smarty's average.
    smartyAvg = smartyTotal / sum(smartyWeights)
    #Variable for Oh No's name.
    ohNoName = str("Oh No's")
    #Variable for Oh No's weights for the grades.
    ohNoWeights = [30, 70]
    #Variable for Oh No's grades.
    ohNoGrades = [40,55]
    #Initializes the total for the loop.
    ohNoTotal = 0
    #The loop for Oh No's grades.
    for grades, weights in zip(ohNoGrades, ohNoWeights):
        #Adjustment for Oh No's grades.
        ohNoTotal += grades * weights
    #Variable for Oh No's average.
    ohNoAvg = ohNoTotal / sum(ohNoWeights)
    #Variable for Miles' name.
    milesName = str("Miles Stalvey's")
    #Variable for the weights of the grades for Miles.
    milesWeights = [20, 80]
    #Variable for the grades of Miles.
    milesGrades = [70, 99]
    #Initialization of the loop for Miles.
    milesTotal = 0
    #Loop for Miles grades.
    for grades, weights in zip(milesGrades, milesWeights):
        #Adjustment for Miles' grade.
        milesTotal += grades * weights
    #Variable for Miles' average.
    milesAvg = milesTotal / sum(milesWeights)
    #Variable for No Good's name.
    noGoodName = str("No Good's")
    #Variable for the weights of No Good's grades.
    noGoodWeights = [20, 80]
    #Variable for No Good's grades.
    noGoodGrades = [0, 0]
    #Initialization of the loop.
    noGoodTotal = 0
    #Loop for No Good's grades.
    for grades, weights in zip(noGoodGrades, noGoodWeights):
        #Adjustment for No Good's grades.
        noGoodTotal += grades * weights
    #Variable for No Good's Average.
    noGoodAvg = noGoodTotal / sum(noGoodWeights)
    #Prints name, message stating that the average is and the average.
    print(billyName+" average is: ",billyAvg)
    #Prints name, message stating that the average is and the average.
    print(hermioneName+" average is: ",hermioneAvg)
    #Prints name, message stating that the average is and the average.
    print(kurtName+" average is: ",kurtAvg)
    #Prints name, message stating that the average is and the average.
    print(smartyName+" average is: ",smartyAvg)
    #Prints name, message stating that the average is and the average.
    print(ohNoName+" average is: ",ohNoAvg)
    #Prints name, message stating that the average is and the average.
    print(milesName+" average is: ",milesAvg)
    #Prints Good's name, message stating that the average is and average
    print(noGoodName+" average is: ",noGoodAvg)
    #First half of the top portion of the average.
    classTopFirstHalf=(billyAvg+hermioneAvg+kurtAvg+smartyAvg)
    #Second half of the top portion of the average.
    classTopSecondHalf=(ohNoAvg+milesAvg+noGoodAvg)
    #Variable for the bottom half of the average.
    NUMBER_OF_STUDENTS = 7
    #Variable for the class average.
    classAvg=(classTopFirstHalf+classTopSecondHalf)/NUMBER_OF_STUDENTS
    #Variable to format and round the average to one decimal place.
    classAvgRounded = round(classAvg,1)
    #Prints telling the user the output information.
    print("The class average is :", classAvgRounded)
calcGrades()
