# Math Operators and Functions
# Operators: https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp
# Functions: https://docs.python.org/3/library/math.html

# Ue must import the module math 
import math

print("Math operations")
print("7 + 2 =", 7 + 2)
print("7 - 2 =", 7 - 2)
print("7 * 2 =", 7 * 2)
print("7 / 2 =", 7 / 2)
print("3 + 7 / 2 =", 3 + 7 / 2)
print("(3 + 7) / 2 =", (3 + 7) / 2)
print("(50 - 5 * 6) / 4 =", (50 - 5 * 6) / 4)
print("(3 + 4) / (1 - 5) =", (3 + 4) / (1 - 5))
print("10/3 =", 10 / 3)

# Integer division (WARNING: Explain the operation using Draw)
# // = division
# % = mod
print("Integer division")
print("7 // 2 =", 7 // 2)
print("7 % 2 =", 7 % 2)

result = divmod(7,2)
print("divmod(7,2)", result)
print(result[0], result[1])

# Pi
print("math.pi =", math.pi)

# Power
print("Power")
print("2 ** 0 =", 2**0)
print("2 ** 1 =", 2**1)
print("2 ** 2 =", 2**2)
print("2 ** 3 =", 2**3)
print("2 ** 4 =", 2**4)
print("3.75 ** 2.5 =", 3.75**2.5)

# Minimum and Maximum
number1 = 5
number2 = 10
number3 = 15
print('min(number1, number2) =', min(number1, number2))
print('min(number1, number2, number3) =', min(number1, number2, number3))
print('max(number1, number2) =', max(number1, number2))
print('max(number1, number2, number3) =', max(number1, number2, number3))

# ceil
print("math.ceil(10.1) =", math.ceil(10.1))
print("math.ceil(10.7) =", math.ceil(10.7))

# floor
print("math.floor(10.1) =", math.floor(10.1))
print("math.floor(10.7) =", math.floor(10.7))

# trunc
print("math.trunc(10.1) =", math.trunc(10.1))
print("math.trunc(10.7) =", math.trunc(10.7))

# round: it is a built in not from math module
print("round(10.1) =", round(10.1))
print("round(10.5) =", round(10.5))
print("round(10.7) =", round(10.7))
print("round(10.7567124, 3) =", round(10.7567124, 3))
print("round(10.7567124, 0) =", round(10.7567124, 0))

# absolute
print("math.fabs(10)  =", math.fabs(10))
print("math.fabs(-10) =", math.fabs(-10))

# Logarithm
print("math.log(16, 2) =", math.log(16, 2))
print("math.log(1024, 2) =", math.log(1024, 2))
print("math.log10(100) =", math.log10(100))
print("math.log10(1000000) =", math.log10(1000000))

# Trigonometric Functions
print(math.sin(90))
print(math.cos(180))
print(math.tan(1))

# Square Root
print("math.sqrt(9) =", math.sqrt(9))
print("math.sqrt(49) =", math.sqrt(49))
print("math.sqrt(121) =", math.sqrt(121))

# Power
print("math.pow(2, 4) =", math.pow(2, 4))
print("math.pow(10, 3) =", math.pow(10, 3))

# Random numbers
# https://docs.python.org/3/library/random.html
# Need to import random module
import random

rnd_number = random.randint(0, 10)
print("Random from 0 and 10 =", rnd_number)
rnd_number = random.randint(5, 10)
print("Random from 5 and 10 =", rnd_number)
rnd_number = random.randint(-5, 5)
print("Random from -5 and 5 =", rnd_number)