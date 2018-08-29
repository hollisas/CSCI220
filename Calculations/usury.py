#Name: Austin Hollis
#usury.py
#Use calcInterest() to call the function to work
#
#Problem: This function will be used to calculate the principal
#         payments and help calculate the interest that will need
#         to be paid over the period of the loan length time frame.
#Certification of Authenticity:
#   I certify that this lab is entirely my own work.

#Variable name for the function
def calcInterest():
    print("This function will help you calculate the", end = " ")
    print("principal payments for financial purchases", end = " ")
    print("with respect to interest and monthly", end = " ")
    print("payments in respect to the length of the loan.")
    print()
    #Tells the user what the function will do and adds a line break
    #the above print lines are all for one print statement.
    months = eval(input("Enter how many months the loan will be for: "))
    #Asks the user to input the number of months the loan is for.
    interest = eval(input("Enter what percent the interest rate is: "))
    #Asks the user to input the interest rate as it would appear in
    #percentage format.
    principal = eval(input("Enter the initial loan amount: "))
    #Asks the user to input the initial loan amount.
    rate = interest / 1200
    #Formula used to find the rate, given formula.
    topPortion = (principal*(rate*((1+rate))**months))
    #Breaks down the monthlyPayment formula to be less
    #than 72 characters long. This is the top portion
    bottomPortion = (((1+rate)**months)-1)
    #Breaks down the monthlyPayment formula to be less
    #than 72 characters long. This is the bottom portion.
    monthlyPayment = (topPortion / bottomPortion)
    #Formula used to find the monthly payment based on given information
    #from the user.
    ##The formula was originally the long version of
    ##the topPortion divided by the bottomPortion but was broken
    ##down to make the reading easier.
    totalPayment = monthlyPayment * months
    #Formula used to find the total payment amount made.
    totalInterest = totalPayment - principal
    #Formula used give the total interest that will be paid.
    print("With a principal amount of", principal, "for", end = " ")
    print(months, "months, and with an interest rate of", end = " ")
    print(interest, "percent, the results are below!")
    print()
    #The above print commands print out and recap what information
    #was given by the user to ensure accuracy!
    #The above print lines are for one print statement.
    print("Initial loan: $", end = "")
    print(principal)
    #These above print lines inform the user that the numbers
    #printed out are supposed to verify the initial loan amount
    #while also making it pleasing to look at.
    print("The loan will be for: ", end = "")
    print(months, "months")
    #These above print lines inform the user that the numbers
    #printed out are supposed to verify the amount of months
    #that the loan will be for while making it pleasing to look at.
    print("With an interest of: ", end = "")
    print(interest, end = "")
    print("%")
    #These above print lines inform the user that the numbers
    #printed out are in relation to the interest and make
    #the printed characters pleasing to look at.
    print("The monthly payment will be: $", end = "")
    print(monthlyPayment)
    #These above print lines inform the user that the numbers
    #printed out are in relation to the monthly payment amount
    #and make it pleasing to look at.
    print("The total payment will be: $", end = "")
    print(totalPayment)
    #These above print lines inform the user that the numbers
    #printed out are in relation to the total payment amount
    #and make it pleasing to look at.
    print("The total interest paid will be: $", end = "")
    print(totalInterest)
    #These above print lines inform the user that the numbers
    #printed out are in relation to the total payment amount
    #and make it pleasing to look at.
    #
    #To clarify on the print statements, the print lines
    #are seperated in order to put the numbers together
    #with the proper special characters. ($ and %)
    print()
    print("Thank you for using my program! Have a nice day!")
    #Thanks and tells the user to have a nice day.
