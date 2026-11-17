# Practical 2: Simple ATM Machine
# Flow Control in Python

# Initial values
balance = 10000
correct_pin = "1234"
attempts = 0
login = False

# PIN Verification (Maximum 3 Attempts)
while attempts < 3:

    pin = input("Enter your ATM PIN: ")

    if pin == correct_pin:
        print("Login Successful!")
        login = True
        break

    else:
        attempts += 1
        print("Incorrect PIN!")

        if attempts < 3:
            print("Attempts Left:", 3 - attempts)

# Check ATM Login Status
if login == False:
    print("Your ATM is Locked!")
    print("Please try again later.")

else:

    # ATM Menu using while loop
    while True:

        print(" ATM MENU")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("5. Change PIN")
       

        choice = input("Enter your choice: ")

        # Check Balance
        if choice == "1":
            print("Your Current Balance is: Rs.", balance)

        # Deposit Money
        elif choice == "2":

            amount = float(input("Enter Deposit Amount: "))

            if amount < 0:
                print("Negative amount is not allowed!")
                continue

            elif amount == 0:
                print("Please enter a valid amount!")
                continue

            else:
                balance += amount
                print("Money Deposited Successfully!")
                print("Updated Balance:", balance)

        # Withdraw Money
        elif choice == "3":

            amount = float(input("Enter Withdraw Amount: "))

            if amount < 0:
                print("Negative amount is not allowed!")
                continue

            elif amount > balance:
                print("Insufficient Balance!")
                continue

            elif amount == 0:
                print("Please enter a valid amount!")
                continue

            else:
                balance -= amount
                print("Money Withdrawn Successfully!")
                print("Remaining Balance:", balance)

        # Exit ATM
        elif choice == "4":
            print("Thank you for using our ATM!")
            print("Final Balance: Rs.", balance)
            break

        # Change PIN Placeholder
        elif choice == "5":
            pass
            print("Change PIN feature is not available yet.")

        else:
            print("Invalid Choice! Please try again.")