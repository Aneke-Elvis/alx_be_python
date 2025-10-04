# bank_account.py
"""Simple BankAccount class demonstrating basic OOP & encapsulation."""

class BankAccount:
    """A minimal bank account class."""

    def __init__(self, initial_balance=0.0):
        """Initialize account with an optional initial balance (default 0.0)."""
        try:
            self._balance = float(initial_balance)
        except Exception:
            self._balance = 0.0

    def deposit(self, amount):
        """
        Add amount to the account balance.
        Raises ValueError if amount is not positive.
        """
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        """
        Try to withdraw amount from the account.
        Returns True when successful, False if insufficient funds.
        Raises ValueError if amount is not positive.
        """
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: {self._format_currency(self._balance)}")

    @property
    def balance(self):
        """Read-only property to access the current balance."""
        return self._balance

    @staticmethod
    def _format_currency(amount):
        """
        Format amount like $50 or $12.5 (no unnecessary trailing zeros).
        Internal helper — kept simple for this exercise.
        """
        s = f"{amount:.2f}"
        # remove trailing zeros and trailing dot if integer
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return f"${s}"
