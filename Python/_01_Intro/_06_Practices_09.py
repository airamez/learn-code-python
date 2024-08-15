"""
09. Read a temperature in Celsius and convert to Fahrenheit
"""

celsius = float(input("Celsius: "))

fahrenheit =  (celsius * 1.8) + 32

print(f"{celsius} Celsius is {round(fahrenheit, 2)} in fahrenheit")