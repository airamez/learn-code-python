# Assigment opertors
# https://www.w3schools.com/python/gloss_python_assignment_operators.asp

# The equal sign means assignment.
# We already used it multiple times :)
name = "José Santos"

# Multiple assigments in one line (PLEASE AVOID IT)
number1, number2, number3, name = 5, 10, 15, "Leila"
print(number1, number2, number3, name)

# This is recommended
number1 = 50
number2 = 100
number3 = 150
name = "Artur"
print(number1, number2, number3, name)

# One value to multiple variables.
a = b = c = d = e = 15
print(a, b, c, d, e)

# It is comun to use value of the variable to increment it
number = number1 + 3
print("number1 =", number1)
print("number =", number)

number2 = number2 + 10
print("number2 =", number2)


'''
Augmmented assignments
  a += b    => a = a + b
  a -= b    => a = a - b
  a *= b    => a = a * b        
  a /= b    => a = a / b
'''

print("number1 =", number1)

number1 += 1
print("number1 atfer += 1:", number1)

number1 -= 3
print("number1 after -= 3:", number1)

number1 *= 2
print("number1 after *2:", number1)

number1 /= 2
print("number1 after /=2:", number1)

number1 = -number1
print("number1 after -number1:", number1)

number1 = -number1
print("number1 after -number1:", number1)

number1 += number2
print("number1 after += number2:", number1)

# THERE IS NO ++ OR -- IN PYTHON :(

# OPERATION PRIORITY
average = (number1 + number2 + number3) / 3
print(f"The average of {number1}, {number2} and {number3}, is {average}")

# Danger
average = number1 + number2 + number3 / 3
print(f"The WRONG average of {number1}, {number2} and {number3} is {average}")