import random

monthlySalary = round(random.randint(20000, 35000), -2)
yearlySalary = monthlySalary*12

def rentPercentage(monthlySalary):
    rent = monthlySalary * 0.35
    return rent

def groceriesPercentage(monthlySalary):
    groceries = monthlySalary * 0.15
    return groceries

maximumRent = rentPercentage(monthlySalary)
maximumGroceries = groceriesPercentage(monthlySalary)

print("Monthly Salary:", monthlySalary)
print("Yearly Salary:", yearlySalary)
print("Monthly maximum rent:", maximumRent)
print("Cost of Groceries:", maximumGroceries)

