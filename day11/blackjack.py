import random

def game1():
    card = random.choice(cards)
    player.append(card)
    print(f"player: {player}")
def game2():
    card = random.choice(cards)
    computer.append(card)
    print(f"computer: {computer}")
def lose():
    print(f"player: {player}")
    print(f"computer: {computer}")
    print("You lost")
def game():
    hit = input("Do you hit another? (yes or no) : ")
    if hit == 'yes':
        game1()
        if sum(player) > 21:
            lose()
        game()
    else:
        comute()
def comute():
    game2()
    if sum(computer) > 21:
        print("Computer Lost")
    elif sum(computer) > sum(player):
        lose()
    else:
        comute()
print("BlackJack game")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
computer = []
print("Player cards")
print("Initial")
game1()
game2()
game()