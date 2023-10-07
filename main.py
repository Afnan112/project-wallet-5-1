import random

print("Welcome to 'whose wallet?' \nYou will give me a list of names, and I will pick a person to pay") 
names_string = input("If you're ready, enter names separated by a comma...").split(", ")
random_name = random.randint(0, len(names_string)-1)
print(f"Ask ' {names_string[random_name]} ' to take his wallet out. \nDinner is on him")
