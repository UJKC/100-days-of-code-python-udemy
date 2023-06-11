print("Love Calculator")
name1 = input("Enter Lover1 name: ").lower()
name2 = input("Enter lover2 name: ").lower()
print(f"{name1} should be compared with 'true'")
print(f"{name2} should be compared with 'love'")
tensplace = (name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")) * 10
onesplace = (name1.count("l") + name1.count("0") + name1.count("v") + name1.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e"))
truelove = tensplace + onesplace
print(f"Your love percentage is: {truelove}")
if truelove < 10 or truelove > 90:
    print("Your story is like coke and mentos")
elif truelove >= 40 or truelove <= 50:
    print("Alright you are together")
else:
    print("Be careful")