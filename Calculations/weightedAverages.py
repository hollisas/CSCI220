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

#Variable name for the function
def calcGrades():
    #Tells the user what the function does.
    print("This function will calculate the grades of each", end = " ")
    print("student and will also calculate the class average.")
    #Asks the user for the file name.
    infileName = input("What file are the names and grades in: ")
    #Opens th file and reads it.
    infile = open(infileName, "r")
    #Begins loop for splitting the file into parts.
    for line in infile:
        #Splits the file into lines and labels them as person.
        person = line.split()
        #print(person)
        for grade in person:
            #Variable fo persons first name
            firstName = person[0]
            #Variable for persons last name
            lastName = person[1]
            #variable for the weight of the grades.
            gradeWeight = person[2::2]
            #variable for the grades of the students.
            grades = person[3::2]
            #initializes the total for the loop.
            total = 0
            totalGrades = 0
            #Variable for the total weight which equals 100.
            TOTAL_WEIGHT = 100
            totalGrade = []
            classAverage = 0
            for i in range(len(grades)):
                portionOne = int(float(str(gradeWeight[i])))
                portionTwo = int(float(str(grades[i])))
                gradesWeight = portionOne * portionTwo
                total+= gradesWeight
                totalGrades+= int(float(str(grades[i])))
                totalGrade.append(totalGrades)
                studentGrades = {totalGrades}
                avg = (total) / (TOTAL_WEIGHT)
                grades.append(str(totalGrades))
                for j in range(1):
                    avg = (total) / (TOTAL_WEIGHT)
                    classAverage = classAverage + avg
            totalGrade.append(totalGrades)
            #print(classAverage)
            #print(total)
        print(totalGrades)
        #print(len(grades))
        print(grades)
        print(avg)
        print(firstName + " " + lastName + "'s average is: " + str(avg))
calcGrades()
