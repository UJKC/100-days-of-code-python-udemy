alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s" ,"t", "u", "v", "w", "x", "v", "z"]
safe = []
desafe = []
condition = input("Ehat do you want to do? Encrypt or Decrypt: ").lower()
if condition == "encrypt":
    string = input("Enter the word to be encrypted: ")
    shift = int(input("Enter the number of place the number has to be shifted: "))
    for i in string:
        j = 0
        while alpha:
            if i == alpha[j]:
                break
            j += 1
        after = alpha[j + shift]
        safe.append(after)
    print(safe)
else:
    string = input("Enter the word to be encrypted: ")
    shift = int(input("Enter the number of place the number has to be shifted: "))
    for i in string:
        j = 0
        while alpha:
            if i == alpha[j]:
                break
            j += 1
        after = alpha[j - shift]
        safe.append(after)
    print(safe)
