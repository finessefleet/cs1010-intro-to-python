emp_no = input("Enter employee number: ")
emp_name = input("Enter employee name: ")
salary = float(input("Enter current salary: "))

hike = salary * 0.10
total_salary = salary + hike

print("Employee No:", emp_no)
print("Employee Name:", emp_name)
print("New Total Salary after 10% hike:", total_salary)
print("Hike Amount:", hike)

# This program calculates the new salary of an employee after a 10% hike based on their current salary.
# It prompts the user to input the employee number, name, and current salary, and then computes the hike and total salary.