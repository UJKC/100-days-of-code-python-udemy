print("You are in the hunt for treasure in jungle. Navigate and find the trasure")
choice1 = input("(left or right)\nYou are in middle for two way intersecting road deadend. Choose left or right where you want to go: ").lower()
if choice1 == 'left':
    choice2 = input("(swim or wait)\nGo ahead, You are in front of a lake. Do you wish to swim or wait and explore: ").lower()
    if choice2 == 'wait':
        choice3 = input("(red or yellow or blue)\nYou discover three doors, Please open one door please: ").lower()
        if choice3 == 'red':
            print("Burned by fire. Game over")
        elif choice3 == 'yellow':
            print("You win. Treasure is yours.")
        elif choice3 == 'blue':
            print("Eaten by Beast. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fell into a hole. Game Over.") 