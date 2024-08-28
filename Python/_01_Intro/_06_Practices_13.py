"""
13. Read the name, salary and salary increase percentage and
    print the name and the new salary of a employee.
"""

name = input("Name: ")
current_salary = float(input("Salary: "))
salary_raise_percentage = float(input("Salart increase %: "))

salary_raise = salary_raise_percentage / 100 * current_salary
new_salary = current_salary + salary_raise
print(f"New Salary = {round(new_salary, 2)}; Salary Raise = {salary_raise}")

new_salary = current_salary * ( 1 + salary_raise_percentage / 100)
print(f"New Salary = {round(new_salary, 2)}")