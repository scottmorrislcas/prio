import random

def roll_d8():
            roll_8 = random.randint(1, 8)
            return roll_8
result = roll_d8()
print(f"You rolled a {result}!")
