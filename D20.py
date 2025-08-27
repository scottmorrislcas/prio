import random

def roll_d20():
    #Simulates rolling a 20-sided die.
            roll_20 = random.randint(1, 20)
            return roll_20
result = roll_d20()
print(f"You rolled a {result}!")
   

