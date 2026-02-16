accounts = {}


def create_account():
    user = input("Enter your name: ")
    num = int(input("Enter contact number: "))
    pin = int(input("Create 4 digit PIN: "))
    
    accounts[num] = {
        'name' : user,
        'account number' : num,
        'pin' : pin,
        'balance' : 0
    }



def check_balance():

    num = int(input("Enter contact number: "))
    pin = int(input("Enter PIN: "))

    if num in accounts and pin == accounts[num]["pin"]:
     
     print("Name:", accounts[num]["name"])
     print("Balance:", accounts[num]["balance"])

    else:
        print("Wrong number or PIN!!")


def deposit():
    num = int(input("Enter contact number: "))
    pin = int(input("Enter PIN: "))

    if num in accounts and pin == accounts[num]["pin"]:
     dep = int(input("Enter amount: "))
     accounts[num]["balance"] += dep
     
    else:
        print("Wrong number or PIN!!")

def withdraw():
    num = int(input("Enter contact number: "))
    pin = int(input("Enter PIN: "))

    if num in accounts and pin == accounts[num]["pin"]:
       withd = int(input("Enter amount: "))
       accounts[num]["balance"] -= withd

    else:
        print("Wrong number or PIN!!")
       

while True:
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Quit")
    
    choice = int(input("Enter Choice: "))

    if choice == 1:
        create_account()

    elif choice == 2:
        check_balance()

    elif choice == 3:
       deposit()

    elif choice == 4:
       withdraw()

    elif choice == 5:
       break

    else:
       print("Invalid Choice!!")
        
        

