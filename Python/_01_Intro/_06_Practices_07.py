# 07. Read the radius of a circle and calculate the area
import math

radius = float(input("Radius: "))

area = math.pi * (radius ** 2)

print(f"The area is {round(area, 5)}")