import random

monthlySalary = round(random.randint(20000, 35000), -2)
yearlySalary = monthlySalary*12

def rentPercentage(monthlySalary):
    rent = monthlySalary * 0.35
    return round(rent, 5)

def groceriesPercentage(monthlySalary):
    groceries = monthlySalary * 0.15
    return groceries

def transportationPercentage(monthlySalary):
    transportation = monthlySalary * 0.15
    return transportation

def savingsPercentage(monthlySalary):
    savings = monthlySalary * 0.20
    return savings

def othersPercentage(monthlySalary):
    others = monthlySalary * 0.15
    return others

maximumRent = rentPercentage(monthlySalary)
maximumGroceries = groceriesPercentage(monthlySalary)
maximumTransportation = transportationPercentage(monthlySalary)
minimumSavings = savingsPercentage(monthlySalary)
othersCost = othersPercentage(monthlySalary)

print("Monthly Salary:", monthlySalary)
print("Yearly Salary:", yearlySalary)
print("Monthly maximum rent:", maximumRent)
print("Cost of Groceries:", maximumGroceries)
print("Cost of transporation:", maximumTransportation)
print("Monthly Savings:", minimumSavings)
print("Others: ", othersCost)
