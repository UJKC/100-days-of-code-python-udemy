import req

flag = True
def proccessing(coffee):
    if req.MENU[coffee]['ingredients']['water'] < req.resources['water']:
        if req.MENU[coffee]['ingredients']['milk'] < req.resources['milk']:
            if req.MENU[coffee]['ingredients']['coffee'] < req.resources['coffee']:
                print("Your coffee is ready")
                req.resources['water'] = req.resources['water'] - req.MENU[coffee]['ingredients']['water']
                req.resources['milk'] = req.resources['milk'] - req.MENU[coffee]['ingredients']['milk']
                req.resources['coffee'] = req.resources['coffee'] - req.MENU[coffee]['ingredients']['coffee']
            else:
                print("coffee not ready")
                exit()
        else:
            print("coffee not ready")
            exit()
    else:
        print("coffee not ready")
        exit()
def change(coffee):
    print(f"Your {coffee} costs {req.MENU[coffee]['cost']}")
    print("Enter the change you have: ")
    cost1 = float(input("Penny: "))
    cost2 = float(input("Dime: "))
    cost3 = float(input("Nickel: "))
    cost4 = float(input("Quarter: "))
    penny = cost1 * 1
    dime = cost2 * 10
    nickel = cost3 * 5
    quarter = cost4 * 25
    total_paid = penny + dime + nickel + quarter
    cost = req.MENU[coffee]['cost']
    recieved = total_paid - cost
    if recieved == 0:
        print(f"Thank You here is your {coffee}")
    elif recieved > 0:
        print(f"Here is your {recieved}, Enjoy your coffee")
        req.resources['money'] += cost
    else:
        print("You do not have balance it seems please try again")
        exit()
print("Coffee Making Machine")
while flag:
    option = input("Enter the coffee you want to make (espresso, latte, cappuccino): ")
    if option == 'report':
        print(req.resources)
    elif option == 'espresso':
        proccessing(option)
        print("Please make payment")
        change(option)
    elif option == 'latte':
        proccessing(option)
        print("Please make payment")
        change(option)
    elif option == 'cappuccino':
        proccessing(option)
        print("Please make payment")
        change(option)
    else:
        print("Try again")
    command = input("Do you want to continue: ")
    if command == 'yes':
        flag = True
    else:
        flag = False
        print("Thank You")