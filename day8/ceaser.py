def initial():
    condition = input("What do you want to do? Encrypt or Decrypt: ").lower()
    condition1(condition)

def encrypt():
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
    initial()

def decrypt():
    string = input("Enter the word to be encrypted: ")
    shift = int(input("Enter the number of place the number has to be shifted: "))
    for i in string:
        j = 0
        while alpha:
            if i == alpha[j]:
                break
            j += 1
        after1 = alpha[j - shift]
        desafe.append(after1)
    print(desafe)
    initial()

def condition1(condition):
    if condition == "encrypt":
        encrypt()
    else:
        decrypt()

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s" ,"t", "u", "v", "w", "x", "v", "z"]
safe = []
desafe = []
initial()