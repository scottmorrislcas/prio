import random

def roll_d1000():
    #Simulates rolling a 20-sided die.
            roll_1000 = random.randint(1, 1000)
            return roll_1000
result = roll_d1000()
print(f"You rolled a {result}!")