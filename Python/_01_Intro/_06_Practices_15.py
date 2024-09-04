"""
15. Read two integer numbers and swap the variables content
"""
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

print(f"Number 1 = {number1}; Number 2 = {number2}")

"""
aux = number1
number1 = number2
number2 = aux
"""

# Pythonic way
number1, number2 = number2, number1

print(f"Number 1 = {number1}; Number 2 = {number2}")
