def getSalary() :
    salary = float(input(" Enter your salary for the month : "))
    return salary

def monthName() :
    month = input(" Enter the name of the month : ")
    return month

def percentages() :
    saving_percentage = float(input(" Enter the percentage for savings : ")) 
    rent_percentage = float(input(" Enter the percentage for rent : "))
    electricity_percentage = float(input(" Enter the percentage for electricity : ")) 
    return saving_percentage , rent_percentage , electricity_percentage

def calculateAllocations(salary ,saving_percentage ,rent_percentage ,electricity_percentage) :
    savings = salary * (saving_percentage / 100 )
    rent = salary * (rent_percentage / 100 )
    electricity = salary * (electricity_percentage / 100 ) 
    return savings , rent , electricity

def calculateRemainder(salary , savings , rent , electricity):
    total_expenses = savings + rent + electricity
    remainder = salary - total_expenses
    return total_expenses , remainder

def yearlyCosts(rent , electricity) :
       yearly_rent = rent * 12
       yearly_electricity = electricity * 12
       return  yearly_rent , yearly_electricity

def funSalary(salary) : 
     funsalary = salary ** 2
     return funsalary

def savingsDivision(savings) : 
    additional_savings = 50

    if savings > 0 :
       after_division =   additional_savings / savings
    else :
      after_division  = float('inf')
    return after_division



def finalResult(salary, month , savings , rent , electricity , total_expenses ,remainder , yearly_rent , yearly_electricity , funsalary , after_division   ) :
    
    print (f"    The Summary for  {month}    ")
    print(f"Total Salary : {salary}$")
    print(f"Allocation for savings : {savings}$")
    print(f"Allocation for rent : {rent}$")
    print(f"Allocation for electricity : {electricity}$")
    print(f"Total expenses : {total_expenses}$")
    print(f"Remainder after expenses : {remainder}$")
    print(f"Yearly cost for rent : {yearly_rent}$")
    print(f"Yearly cost for electricity : {yearly_electricity}$")
    print(f"Salary to the power of 2 : {funsalary}")
    print(f"Additional amount divided by total amount allocated to savings: {after_division}")


def main() :
    salary = getSalary()
    month = monthName()
    saving_percentage , rent_percentage , electricity_percentage = percentages()
    savings , rent , electricity = calculateAllocations(salary ,saving_percentage ,rent_percentage ,electricity_percentage)
    total_expenses , remainder = calculateRemainder(salary , savings , rent , electricity)
    yearly_rent , yearly_electricity  = yearlyCosts(rent , electricity)
    funsalary = funSalary(salary)
    after_division = savingsDivision(savings) 
    finalResult(salary, month , savings , rent , electricity , total_expenses ,remainder , yearly_rent , yearly_electricity , funsalary , after_division)



main()