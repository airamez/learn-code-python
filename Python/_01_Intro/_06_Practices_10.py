"""
10. Read a temperature in Fahrenheit and convert to Celsius
"""

fahrenheit = float(input("Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print(round(celsius, 2))