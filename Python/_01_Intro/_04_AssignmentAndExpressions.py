# The equal sign means assignment.
# We already used it multiple times :)
name = "José Santos"

# Multiple assigments in one line (PLEASE AVOID IT)
number1, number2, number3, name = 5, 10, 15, "José Santos"
print(number1, number2, number3, name)

# This is recommended
number1 = 5
number2 = 10
number3 = 15
name = "José Santos"
print(number1, number2, number3, name)

# One value to multiple variables.
a = b = c = d = e = 15
print(a, b, c, d, e)

print("n1 =", number1)

'''
Augmmented assignments
  a += b    => a = a + b
  a -= b    => a = a - b
  a *= b    => a = a * b        
  a /= b    => a = a / b
'''

print("n1 =", number1)

number1 += 1
print("n1 atfer += 1 =", number1)

number1 -= 3
print("n1 after -= 3 =", number1)

number1 *= 2
print("n1 after *2 =", number1)

number1 /= 2
print("n1 after /=2 =", number1)

number1 = -number1
print("n1 after -n1 =", number1)

# THERE IS NO ++ OR -- IN PYTHON :(

# OPERATION PRIORITY
average = (number1 + number2 + number3) / 3
print("The average of", number1, ",", number2, "and", number3, "is", average)

# Danger
average = number1 + number2 + number3 / 3
print("The WRONG average of", number1, ",", number2, "and", number3, "is", average)
