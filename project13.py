balance = float(input("Enter the balance: "))


while True:
    print("Welcome to the ATM. Please select an option:")
    print("1. Check balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit\n")

    option = int(input("Enter option number: "))

    if option == 1:
        print(f"Your balance is: ${balance:,.2f}")

    elif option == 2:
        withdraw = float(input("Enter withdraw amount: "))
        if balance >= withdraw:
            balance -= withdraw
            print(f"Withdrawal successful. Your new balance is: ${balance:,.2f}")
        else:
            print("Insufficient balance")

    elif option == 3:
        deposit = float(input("Enter deposit amount: "))
        balance += deposit
        print(f"Deposit successful. Your new balance is: ${balance:,.2f}")

    elif option == 4:
        print("Thank you for using the ATM. Have a great day!")
        break

    else:
        print("Invalid option. Please try again.")

