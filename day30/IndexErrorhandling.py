fruits = ["Apple", "Pear", "Orange"]

def makepie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print(f"Give values from 0 - {len(fruits)}")

makepie(4)