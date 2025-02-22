def getSalary() :
    salary = float(input("Enter your salary for the month : "))
    return salary

def monthName() :
    month = input("Enter the name of the month : ")
    return month

def percentages() :
    saving_percentage = float(input("Enter the percentage for savings : ")) 
    rent_percentage = float(input("Enter the percentage for rent : "))
    electricity_percentage = float(input("Enter the percentage for electricity : ")) 
    return saving_percentage , rent_percentage , electricity_percentage

def calculateAllocations() :
    savings = salary * (saving_percentage / 100 )
    rent = salary * (rent_percentage / 100 )
    electricity = salary * (electricity_percentage / 100 ) 
    return savings , rent , electricity

def calculateRemainder():
    total_expenses = savings + rent + electricity
    remainder = salary - total_expenxses
    return total_expenses , remainder

def yearlyCosts() :
       yearly_rent = rent * 12
       yearly_electricity = electricity * 12
       return  yearly_rent , yearly_electricity

def funSalary() : 
     funsalary = salary ** 2
     return funsalary

def savingsDivision() : 
    additional_savings = 50

    if savings > 0 :
       after_division =   additional_savings / savings
    else :
      after_division  = float('inf')
    return after_division


