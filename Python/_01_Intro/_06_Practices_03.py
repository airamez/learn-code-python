# 3. Read an integer number and print the three predecessors and successors.
number = int(input("Number: "))

print(f"{number - 3} {number - 2} {number - 1} {number + 1} {number + 2} {number + 3}")

predecessor_1 = number - 3
predecessor_2 = number - 2
predecessor_3 = number - 1
successor_1 = number + 1
successor_2 = number + 2
successor_3 = number + 3

print(f"{predecessor_1} {predecessor_2} {predecessor_3}")
print(f"{successor_1} {successor_2} {successor_3}")