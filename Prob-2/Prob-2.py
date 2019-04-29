# Module 3
#   Programming Assignment 4
#     Prob-2.py

# David Harrsch

'''
Your IPO comment goes here
Input:Name, Wage, Hours, from user
Process: Calculate take home pay from work hours, overtime and witholdings
Output: Displayed total wages and deductions
'''

def main():
    # your code goes here
    # take user info
    name= input("What is your name?: ")
    wage= eval(input("What is your hourly wage?: "))
    hours=eval(input("How many hours did you work?: "))
    
    #assign user inputs and calculations to veriables 
    overtime=hours-40
    if hours > 40:
        Twages= ((overtime*wage*1.5)+(wage*40))
    else: 
        Twages=wage*hours
    tax=Twages*0.20
    insurance=Twages*0.10
    takehome=Twages-(tax+insurance)
# print the output of calcualtions
    print("______________________")
    print()
    print("Employee's name:\t ",name)
    print("Normal wage:\t\t",wage*(hours-overtime))
    print("Overtime wage:\t\t",wage*overtime*1.5)
    print("Total wages:\t\t",Twages)
    print("Tax Withholding:\t",tax)
    print("Insurance Witholdind:\t",insurance)
    print("Take Home Pay:\t\t",takehome)
    print()
    print("______________________")
main()