# Input

balance = 0
option = 0

while option != 4:
    option =0
    print("Select an option from below: ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    while option < 1 or option > 4:
        option = int(input("Please input your option: "))
    if option == 1:
        deposit = -1
        while deposit < 0:
            deposit = float(input("Enter Deposit Amount: "))
            if deposit < 0:
                print("Please enter a valid amount")
        balance += deposit

    elif option == 2:
        withdrawal = -1
        while withdrawal < 0 or balance < withdrawal:
            withdrawal = float(input("Enter Withdrawal Amount: "))
            if withdrawal < 0:
                print("Please enter a valid amount")
            if balance < withdrawal:
                print("Insufficient Balance")
        balance = balance - withdrawal

    elif option == 3:
        print(f"Current Balance is ${balance:.2f}")

    elif option == 4:
        print("Thank you for banking with us")