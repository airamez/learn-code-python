# read 3 numbers and print the sum and average
# Are the number integer or float?

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Number 3: "))

sum = number1 + number2 + number3
average = sum / 3

print(f"Sum = {sum}")
print(f"Average = {average}")