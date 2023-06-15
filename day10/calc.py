print("Calculator")
def calculator(input2):
    match input2:
        case '+':
            res = input1 + input3
            return res
        case '-':
            res = input1 - input3
            return res
        case '*':
            res = input1 * input3
            return res
        case '/':
            res = input1 / input3
            return res
        case '%':
            res = input1 % input3
            return res
input1 = int(input("Enter the number 1: "))
input2 = input("Enter the operator character: ")
input3 = int(input("Enter the number 2: "))
result_main = calculator(input2)
print(f"The result is: {result_main}")