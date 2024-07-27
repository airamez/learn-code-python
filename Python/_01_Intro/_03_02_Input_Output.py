# Input: input - reads a value from console and returns the value as string
# Output: print - prints to the console

name = input("What is your name: ")

print("Hello", name)


print(f"Hello {name}")

greetings = f"Hello {name}" 
print(greetings)

# Show the source code implementation for input and print:
# File: https://github.com/python/cpython/blob/main/Python/bltinmodule.c
# Functions: 
#   builtin_input
#   builtin_print

# WARNING: Remember to show some input of invalid types

n1 = input ("Integer 1: ") # Warning: returns as a String
n1 = int(input("Integer number 1: ")) # Convert from string to integer
n2 = int(input("Integer number 2: "))
average = (n1 + n2) / 2
print(f"The average of {n1} and {n2} is {average}")

n1 = float(input("Float number 1: "))
n2 = float(input("Float number 2: "))
average = (n1 + n2) / 2
print(f"The average of {n1} and {n2} is {average}")

# print() always add a new line
# To avoid the new line we must to indicate that the end of the string is a empty string
print(n1)
print(n2)
print(name)
print(n1, end="") # useful to split a long print or when using looping
print(n2, end="")
print(name, end=" ")
print("Santos")

# Multiple outputs will be sepated by spaces (We already used this a lot)
first_name = input("First name: ")
last_name = input("Last name: ")
middle_name = input("Middle name: ")
print(first_name, middle_name, last_name)

# Using interpolation
print(f"{first_name} {middle_name} {last_name}")

# Storing in a variable
full_name = f"{first_name} {middle_name} {last_name}"
print(f"Full name: {full_name}")