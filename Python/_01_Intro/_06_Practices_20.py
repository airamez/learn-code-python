"""
20. Generate a random number from 0 to 9 and allow the user to try 3 times and
    indicate if the user guessed the generated random number correctly
"""

import random

rnd_number = random.randint(0, 9)

guess_1 = int(input("Guess 1: "))
guess_2 = int(input("Guess 2: "))
guess_3 = int(input("Guess 3: "))

print("If there one True in the next 3 lines you guessed the number!")

print(rnd_number == guess_1)
print(rnd_number == guess_2)
print(rnd_number == guess_3)

print(f"The random number was {rnd_number}")