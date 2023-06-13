import random

def death1(death):
    if len == 4:
        if death == 0:
            print("continue")
        elif death == 1:
            print("(0)")
        elif death == 2:
            print("(0)")
            print(" | ")
            print(" | ")
            print(" | ")
        elif death == 3:
            print("  (0)  ")
            print("   |   ")
            print("  /|\\ ")
            print("/  |  \\")
        else:
            print("  (0)  ")
            print("   |   ")
            print("  /|\\ ")
            print("/  |  \\")
            print("  / \\ ")
            print("/     \\")
            print("Game Over!")
    else:
        if death == 0:
            print("continue")
        elif death == 1:
            print("(0)")
        elif death == 2:
            print("(0)")
            print(" | ")
        elif death == 3:
            print("  (0)  ")
            print("   |   ")
            print("  /|\\ ")
            print("/     \\")
        elif death == 4:
            print("  (0)  ")
            print("   |   ")
            print("  /|\\ ")
            print("/  |  \\")
        else:
            print("  (0)  ")
            print("   |   ")
            print("  /|\\ ")
            print("/  |  \\")
            print("  / \\ ")
            print("/     \\")
            print("Game Over!")

print("Hangman Game")
option = random.randint(0,1)
words = ["udai", "ujwal"]
selected = words[option]
len = len(selected)
print(f"There are {len} words available")
death = 0
good = 0
j = 0
for j in selected:
    print("_")
i = 0
while death < (len):
    input_word = input("Enter the letter: ")
    if input_word in selected:
        print("Good")
        good += 1
    else:
        death += 1
    if good == len:
        print("Very Good!")
        break
    death1(death)