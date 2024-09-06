"""
17. Read an integer number with 6 digits and 
    separate it into two integers with 3 digits each
"""
number = int(input("Number with 6 digits: "))

first_part = number // 1000
last_part = number % 1000

print(f"{number} = [{first_part}][{last_part}]")