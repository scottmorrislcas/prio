import random

def roll_d6():
            roll_6 = random.randint(1, 6)
            return roll_6
result = roll_d6()
print(f"You rolled a {result}!")
