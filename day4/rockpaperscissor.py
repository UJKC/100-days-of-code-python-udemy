import random

print("Rock paper Scissor. 0 for Rock, 1 for Paper, 2 for Scissor")
options = ["rock", "paper", "scissor"]
rand = random.randrange(0, 2)
yours = int(input("Select your option: "))
if rand == 0 and yours == 0:
    print(f"Computer: {options[rand]} Yours: {options[yours]}")
    print("Play again")
elif rand == 0 and yours == 1:
    print(f"Computer: {options[rand]} Yours: {options[yours]}")
    print("You win")
elif rand == 0 and yours == 2:
    print(f"Computer: {options[rand]} Yours: {options[yours]}")
    print("You lose")
elif rand == 1 and yours == 0:
    print(f"Computer: {options[rand]} Yours: {options[yours]}")
    print("You lose")
elif rand == 1 and yours == 1:
    print(f"Computer: {options[rand]} Yours: {options[yours]}")
    print("Play again")
elif rand == 1 and yours == 2:
    print(f"Computer: {options[rand]} Yours: {options[yours]}")
    print("You win")
elif rand == 2 and yours == 0:
    print(f"Computer: {options[rand]} Yours: {options[yours]}")
    print("You win")
elif rand == 2 and yours == 1:
    print(f"Computer: {options[rand]} Yours: {options[yours]}")
    print("You lose")
else:
    print(f"Computer: {options[rand]} Yours: {options[yours]}")
    print("Play again")