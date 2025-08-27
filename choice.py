import random

while True:
    choice = input("Enter a choice (separated by commas): ")
    choices = choice.split(", ")
    random_choice = random.choice(choices)
    print(f"The chosen option is: {random_choice}")
    next_choice = input("Do you want to choose again? (yes/no): ")
    
    if next_choice.lower() == "yes":
        while True:
                random_choice = random.choice(choices)
                print(f"The chosen option is: {random_choice}")
                next_choice = input("Do you want to choose again? (yes/no): ")

                if next_choice.lower() == "no":
                    break
    break 