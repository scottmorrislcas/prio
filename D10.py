import random

def roll_d10():
            roll_10 = random.randint(1, 10)
            return roll_10
result = roll_d10()
print(f"You rolled a {result}!")
