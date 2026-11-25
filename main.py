
# WHY: Import the required ATM functions from atm.py.
from atm import (
    set_pin,
    display_menu,
    check_balance,
    deposit,
    withdraw,
    show_transactions
)

def main():

    # WHY: Set the initial balance for this ATM simulation.
    balance = 10000

    # WHY: Store all transactions during the current program session.
    transactions = []

    # WHY: Allow the user to create a PIN before accessing the ATM.
    print("Welcome to PyATM Machine!\n")
    pin = set_pin()

    # WHY: Set the maximum number of incorrect PIN attempts.
    max_attempts = 3
    attempts = 0

    # WHY: Repeat PIN verification until the PIN is correct or attempts run out.
    while attempts < max_attempts:

        entered_pin = input("Enter your PIN to access the ATM: ")

        if entered_pin == pin:
            print("\nPIN verified successfully!\n")
            break

        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts

            if remaining_attempts > 0:
                print(f"\nIncorrect PIN! {remaining_attempts} attempt(s) remaining.\n")

            else:
                print("\nMaximum attempts reached. Access denied.")
                return

    # WHY: Show the ATM menu only after successful PIN verification.
    while True:

        display_menu()

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit(balance, transactions)

        elif choice == "3":
            balance = withdraw(balance, transactions)

        elif choice == "4":
            show_transactions(transactions)

        elif choice == "5":
            print("\nThank you for using PyATM Machine!")
            break

        else:
            print("\nInvalid option. Please choose between 1 and 5.\n")

# WHY: Run main() only when this file is executed directly.
if __name__ == "__main__":
    main()