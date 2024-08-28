"""
14. Read the name, salary, years of experience and the numbers of kids 
    of a employee and print the name and new salary using the following 
    formula:
    - 0.5% per year of experience
    - 2% per kid
"""

name = input("Name: ")
salary = float(input("Salary: "))
years_of_experience = int(input("Years of experience: "))
kids = int(input("Number of kids: "))

experience_raise_percentage = 0.5 * years_of_experience
experiece_raise = experience_raise_percentage / 100 * salary
kids_raise_percentage = 2 * kids
kids_raise = kids_raise_percentage / 100 * salary
new_salary = salary + experiece_raise + kids_raise

print(f"Name: {name}; New Salary: {new_salary}")