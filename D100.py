import random

def roll_d100():
            roll_100 = random.randint(1, 100)
            return roll_100
result = roll_d100()
print(f"You rolled a {result}!")
