import random

def game(ranga, change):
    while change > 0:
        user = int(input("Enter the guessed number: "))
        if user > number_selected:
            print("Too High")
            change -= 1
            print(f"chances: {change}")
        elif user < number_selected:
            print("Too Low")
            change -= 1
            print(f"chances: {change}")
        else:
            print("You Won")
            break
    print(f"Number Selected: {number_selected}")
    print("Game Over")
print("Number guessing game")
level = input("Enter the level of game: (easy or moderate or hard): ")
if level == 'easy':
    change = 20
elif level == 'moderate':
    change = 10
else:
    change = 5
ranga = int(input("Enter the range to be selected: "))
number_selected = random.randint(0, ranga)
game(ranga, change)