"""
18. Read an integer number with 5 digits and
    generate a new number with the digits in
    reverse order
    
    Examples:
    12345 => 54321
    54321 => 12345
    33666 => 66633
    00001 => 10000
    00012 => 21000
    00123 => 32100
    10000 => 1
    90000 => 9
"""

number = int(input("Number: "))

inversed_number = 0

last_digit = number % 10
inversed_number = last_digit

number = number // 10
last_digit = number % 10
inversed_number = inversed_number * 10 + last_digit

number = number // 10
last_digit = number % 10
inversed_number = inversed_number * 10 + last_digit

number = number // 10
last_digit = number % 10
inversed_number = inversed_number * 10 + last_digit

number = number // 10
last_digit = number % 10
inversed_number = inversed_number * 10 + last_digit

print(f"Inversed Number = {inversed_number}")
