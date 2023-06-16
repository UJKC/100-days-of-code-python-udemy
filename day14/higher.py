import day17.data as data
import random

def compare(to_be_choosen1, to_be_choosen2):
    print("1.")
    print(data.data[to_be_choosen1]['name'])
    print(data.data[to_be_choosen1]['description'])
    print(data.data[to_be_choosen1]['country'])
    print("")
    print("")
    print("")
    print("VS")
    print("")
    print("")
    print("")
    print("2.")
    print(data.data[to_be_choosen2]['name'])
    print(data.data[to_be_choosen2]['description'])
    print(data.data[to_be_choosen2]['country'])
    player_input = int(input("Enter who has more followers (1 or 2): "))
    if player_input == 1:
        if data.data[to_be_choosen1]['follower_count'] > data.data[to_be_choosen2]['follower_count']:
            print("Good")
            player12 = player2()
            compare(to_be_choosen1, player12)
        else:
            print("Game Over")
            exit()
    else:
        if data.data[to_be_choosen2]['follower_count'] > data.data[to_be_choosen1]['follower_count']:
            print("Good")
            player11 = player1()
            to_be_choosen1 = to_be_choosen2
            compare(to_be_choosen1, player11)
        else:
            print("Game Over")
            exit()
def player1():
    to_be_choosen1 = random.randint(0, 49)
    return to_be_choosen1
def player2():
    to_be_choosen2 = random.randint(0, 49)
    return to_be_choosen2
print("Higher or Lower")
player11 = player1()
player12 = player2()
compare(player11, player12)