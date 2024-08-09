"""
04. Read two integer numbers A and B and print the result of all arithmetic
    operations you know for A and B.
"""
number_a = int(input("Number a: "))
number_b = int(input("Number b: "))

addition = number_a + number_b
subtraction = number_a - number_b
multiplication = number_a * number_b
division = number_a / number_b
integer_division = number_a // number_b
mod = number_a % number_b
power = number_a ** number_b
min = min(number_a, number_b)
max = max(number_a, number_b)

print(f"{number_a} + {number_b} = {addition}")
print(f"{number_a} - {number_b} = {subtraction}")
print(f"{number_a} * {number_b} = {multiplication}")
print(f"{number_a} / {number_b} = {division}")
print(f"{number_a} // {number_b} = {integer_division}")
print(f"{number_a} % {number_b} = {mod}")
print(f"{number_a} ** {number_b} = {power}")
print(f"min({number_a},{number_b}) = {min}")
print(f"max({number_a},{number_b}) = {max}")