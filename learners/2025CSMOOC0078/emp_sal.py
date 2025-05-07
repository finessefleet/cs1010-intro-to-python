#Calculating the hike in salary of an employee
# Hike = salary * (10/100)
# Hike_percentage = (New_salary - Old salary) / (old salary * 100)

emp_name = input("Enter the name of the employee: ")
emp_num = input("Enter the employee number: ")
salary = float(input("Enter the current salary: "))

#Calculating hike
hike = salary * 0.10
total_salary = salary + hike
_hike_percent = (total_salary-salary)/(salary*100)

#Displaying the total salary and hike amount
print("The Total Salary is : ", total_salary)
print("The hike amount is : ", hike)

#Printing hike percentage
print("The Hike Percentaage salary is: ", _hike_percent)
