#main page 
from bank_account import BankAccount
import argparse

parser = argparse.ArgumentParser(description="BankAccount Operations")
parser.add_argument("--deposit", type=float, help="Amount to deposit")
parser.add_argument("--withdraw", type=float, help="Amount to withdraw")
parser.add_argument("--balance", action="store_true", help="Current Balance")
args = parser.parse_args()

account = BankAccount()

if args.deposit:
    account.deposit(args.deposit)
    print(f"Deposited ${args.deposit:.2f}")

if args.withdraw:
    if account.withdraw(args.withdraw)
        print(f"Withdrew ${args.withdraw:.2f}")
    else:
        print(f"Insufficient funds")

if args.balance:
    print(f"Current balance: ${account.get_balance():.2f}")
