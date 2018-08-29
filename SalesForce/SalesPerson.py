#Name: Austin Hollis
#
#Problem: This program will be used to create two classes, one class
#         will be a class for individual people and the other class
#         will the overall function that calls and compares the
#         individual people and their sales.
#
#Certification of Authenticity:
#   I certify that this lab is entirely my own work, but I talked
#   about my code with Professor Stalvey and Sarah.



#Class for a single person.
class SalesPerson:
    
    #Constructor
    #Input: ID and Name of person
    def __init__(self, ID, name):
        #Sets the ID
        self.ID = ID
        #Sets the name
        self.name = name
        #Creates an empty list
        self.salesList = []
        
    ###Getter Methods###
        
    #Gets ID
    #Input: None
    #Output: ID number
    def getID(self):
        return self.ID
    
    #Gets Name
    #Input: None
    #Output: Name of person
    def getName(self):
        return self.name
    
    #Gets Sales
    #Input: None
    #Output: List of sales list
    def getSales(self):
        return self.salesList
    
    #Gets the total amount of sales
    #Input: None
    #Output: Self Sum of Sales
    def getSumSales(self):
        return self.sumSales

    ###Setter Methods###
    
    #Sets the Name
    #Input: None
    #Output: checks to see if name is a str then sets name
    def setName(self):
        if type(self.name)== str:
            name = self.name
            
    #Evaluates and appends sale to the list
    #Input: Sales
    #Output: Appends Sales to a list
    def enterSale(self,aSale):
        aSale = eval(str(aSale))
        self.salesList.append(aSale)
        
    #Sums up the sales
    #Input: None
    #Output: Sum of the sales.
    def totalSales(self):
        sumSales = 0
        for i in range(len(self.salesList)):
            sumSales += self.salesList[i]
        return sumSales
    
    #Determines if the person met the quota or not based on sales
    #Input: Quota Goal
    #Output: Boolean based on met goal or not.
    def metQuota(self,quota):
        rtnStatement = False
        if quota <= self.totalSales():
            rtnStatement = True
        return rtnStatement

    #Compares total sales of one person to another person
    #Input: Parameter for the other person
    #Output: Negative if less than other person, positive if greater
    #        than the other person and 0 if equal.
    def compareTo(self,otherPerson):
        if self.totalSales() < otherPerson.totalSales():
            rtnValue = -1
        elif self.totalSales() > otherPerson.totalSales():
            rtnValue = 1
        else:
            rtnValue = 0
        return rtnValue

    #String of what should be returned to the user.
    def __str__(self):
        rtnStr = ""
        rtnStr += "ID #: " + str(self.ID)
        rtnStr += "\nName: " + str(self.name)
        rtnStr += "\nList of Sales: " + str(self.salesList)
        rtnStr += "\nTotal Sales: $" + str(self.totalSales())
        return rtnStr

#Class for the Sales Force
class SalesForce:

    #Constructor
    #Input: None
    #Output: None
    def __init__(self):
        self.salesList = []
        
    #Input: Name of File
    #Output: Appends person to sales list
    def addData(self,fileName):
        #Reads File
        infile = open(fileName, 'r')
        for line in infile:
            #Splits line into parts
            parts = line.split()
            #Sets ID to the evaluation parts at position 0
            ID = eval(parts[0])
            #Sets First Name to parts at position 1
            firstName = parts[1]
            #Sets Last Name to parts at position 2
            lastName = parts[2]
            #Sets Sales to parts at position 3 to the end of list
            sales = parts[3:]
            #Makes the name as the string of the first and last name
            name = str(firstName) + " " + str(lastName)
            #Sets person as a Class of SalesPerson
            person = SalesPerson(ID,name)
            #Evaluates the sales
            for sale in sales:
                person.enterSale(eval(sale))
            #Appednds the person to salesList
            self.salesList.append(person)

    #Input: receives a quota
    #Output: Statements of whether or not they met the quota
    def quotaReport(self,quota):
        salesList = self.salesList
        for person in salesList:
            returnStatement = person.metQuota(quota)
            print()
            print(person)
            print("Met quota: ", returnStatement)

    #Input: None
    #Output: Returns the maximum position
    def topSalesPerson(self):
        #Number of items
        numItems = len(self.salesList)
        pos = 0
        for i in range(pos+1, numItems):
            if self.salesList[i].totalSales()>self.salesList[pos].totalSales():
                pos = i
        return self.salesList[pos]

    #Input: Received the ID number
    #Output: Statements depending on the ID number.
    def individualSales(self, ID):
        i = 0
        numItems = len(self.salesList)
        while i < numItems and self.salesList[i].getID() != ID:
            i+=1
        if i < len(self.salesList):
            print(self.salesList[i])
            print("Individual sales: ", self.salesList[i].getSales())
        else:
            print("ID not found in index.")
