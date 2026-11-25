
# WHY: This function allows the user to create a 4-digit PIN.
def set_pin():
    while True:
        pin = input("Create your 4-digit PIN: ")

        # WHY: Check whether the PIN contains exactly four digits.
        if pin.isdigit() and len(pin) == 4:
            print("\nPIN created successfully!\n")
            return pin

        print("Invalid PIN. Please enter exactly 4 digits.\n")


# WHY: Display the ATM menu whenever the user needs it.
def display_menu():
    print("========== PYATM MACHINE ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")
    print("===================================")

# WHY: Display the current account balance.
def check_balance(balance):
    print(f"\nYour Current Balance: ₹{balance}\n")


# WHY: Take a valid positive amount from the user.
def get_amount(message):
    while True:
        try:
            amount = int(input(message))

            # WHY: Zero and negative amounts are not valid transactions.
            if amount > 0:
                return amount

            print("Please enter an amount greater than zero.")

        except ValueError:
            # WHY: Prevent the program from crashing on non-numeric input.
            print("Invalid input. Please enter a valid number.")


# WHY: Add the deposited amount to the existing balance.

# WHY: Deposit money and record the successful transaction.
def deposit(balance, transactions):
    amount = get_amount("Enter deposit amount: ₹")

    balance += amount

    # WHY: Store transaction details in the history list.
    transactions.append({
        "type": "Deposit",
        "amount": amount,
        "balance": balance
    })

    print("\nMoney deposited successfully!")
    check_balance(balance)

    return balance



# WHY: Withdraw money and record the successful transaction.
def withdraw(balance, transactions):
    amount = get_amount("Enter withdrawal amount: ₹")

    if amount > 20000:
        print("\nYou can withdraw a maximum of ₹20,000 per transaction.\n")

    elif amount > balance:
        print("\nInsufficient balance!\n")

    else:
        balance -= amount

        # WHY: Record only successful withdrawals.
        transactions.append({
            "type": "Withdrawal",
            "amount": amount,
            "balance": balance
        })

        print("\nMoney withdrawn successfully!")
        check_balance(balance)

    return balance


# WHY: Display all recorded transactions.
def show_transactions(transactions):

    if not transactions:
        print("\nNo transactions available yet.\n")
        return

    print("\n========== TRANSACTION HISTORY ==========")

    # WHY: Loop through every transaction stored in the list.
    for index, transaction in enumerate(transactions, start=1):

        print(f"\nTransaction {index}")
        print(f"Type: {transaction['type']}")
        print(f"Amount: ₹{transaction['amount']}")
        print(f"Balance after transaction: ₹{transaction['balance']}")

    print("\n=========================================\n")