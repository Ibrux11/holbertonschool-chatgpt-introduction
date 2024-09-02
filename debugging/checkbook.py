#!/usr/bin/python3

class Checkbook:
    """
    A class to represent a checkbook for managing account transactions.

    Attributes
    ----------
    balance : float
        The current balance of the account.

    Methods
    -------
    deposit(amount: float) -> None
        Adds the specified amount to the balance.
    withdraw(amount: float) -> None
        Withdraws the specified amount from the balance if funds are sufficient.
    get_balance() -> None
        Prints the current balance.
    """

    def __init__(self):
        """
        Initializes the Checkbook with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount to the checkbook balance.

        Parameters
        ----------
        amount : float
            The amount to be deposited into the account.

        Returns
        -------
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook balance if funds are sufficient.

        Parameters
        ----------
        amount : float
            The amount to be withdrawn from the account.

        Returns
        -------
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.

        Returns
        -------
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    The main function that drives the program, allowing user interaction with the Checkbook.

    Users can:
    - Deposit money into the checkbook.
    - Withdraw money from the checkbook.
    - Check the current balance.
    - Exit the program.

    Returns
    -------
    None
    """
    # Create an instance of Checkbook
    cb = Checkbook()
    
    # Loop indefinitely until the user chooses to exit
    while True:
        # Prompt user for an action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()

        if action == 'exit':
            # Exit the loop if the user types 'exit'
            break
        elif action == 'deposit':
            try:
                # Prompt user for the deposit amount
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    # Ensure the deposit amount is positive
                    print("Please enter a positive amount.")
                else:
                    # Deposit the specified amount
                    cb.deposit(amount)
            except ValueError:
                # Handle non-numeric input for deposit
                print("Invalid input. Please enter a valid number.")
        elif action == 'withdraw':
            try:
                # Prompt user for the withdrawal amount
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    # Ensure the withdrawal amount is positive
                    print("Please enter a positive amount.")
                else:
                    # Withdraw the specified amount
                    cb.withdraw(amount)
            except ValueError:
                # Handle non-numeric input for withdrawal
                print("Invalid input. Please enter a valid number.")
        elif action == 'balance':
            # Display the current balance
            cb.get_balance()
        else:
            # Handle invalid commands
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
