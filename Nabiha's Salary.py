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
