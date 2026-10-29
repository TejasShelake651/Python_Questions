# User-Defined / Custom Exceptions

class AgeError(Exception):
    pass


class InsufficientFundError(Exception):
    def __init__(self, bal, amt):
        self.bal = bal
        self.amt = amt
        super().__init__(f"Cannot withdraw {amt}. Current balance is only {bal}.")


class ExceptionDemoAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundError(self.balance, amount)
        self.balance -= amount
        return self.balance


if __name__ == "__main__":
    # Custom AgeError test
    test_age = 15
    print("Testing Custom AgeError:")
    try:
        if test_age < 18:
            raise AgeError(f"Age {test_age} is invalid. Age must be 18 or above.")
        print("Valid age:", test_age)
    except AgeError as e:
        print("  -> Caught Custom AgeError:", e)

    # Custom InsufficientFundError test
    print("\nTesting Custom InsufficientFundError:")
    bank_acc = ExceptionDemoAccount(balance=500)
    print("Bank account balance:", bank_acc.balance)
    try:
        print("Attempting to withdraw 1200...")
        bank_acc.withdraw(1200)
    except InsufficientFundError as e:
        print("  -> Transaction failed:", e)
    finally:
        print("  -> Thank you for banking with us.")
