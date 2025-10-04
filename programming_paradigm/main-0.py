# main-0.py
import sys
from bank_account import BankAccount

def parse_arg(arg):
    """
    Parse a single argument of form "command:amount" or "display".
    Returns (command, amount_or_None).
    """
    parts = arg.split(':', 1)
    command = parts[0].lower()
    amount = None
    if len(parts) > 1 and parts[1] != '':
        try:
            amount = float(parts[1])
        except ValueError:
            print("Amount must be a number.")
            sys.exit(1)
    return command, amount

def main():
    # Example starting balance (change if you want)
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, amount = parse_arg(sys.argv[1])

    if command == "deposit":
        if amount is None:
            print("Please provide an amount for deposit (e.g. deposit:50)")
            sys.exit(1)
        try:
            account.deposit(amount)
            print(f"Deposited: {BankAccount._format_currency(amount)}")
        except ValueError as e:
            print(e)
            sys.exit(1)

    elif command == "withdraw":
        if amount is None:
            print("Please provide an amount for withdraw (e.g. withdraw:20)")
            sys.exit(1)
        try:
            if account.withdraw(amount):
                print(f"Withdrew: {BankAccount._format_currency(amount)}")
            else:
                print("Insufficient funds.")
        except ValueError as e:
            print(e)
            sys.exit(1)

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command.")
        sys.exit(1)

if __name__ == "__main__":
    main()
