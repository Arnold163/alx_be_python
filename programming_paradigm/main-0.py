#main page 
from bank_account import BankAccount
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("action", choices=["deposit", "withdraw", "balance"])
parser.add_argument("amount", type=float, nargs="?")
args = parser.parse_args()


account = BankAccount()

if args.action == "deposit":
    account.deposit(args.amount)
    account.display_balance
elif args.action == "withdraw":
    if account.withdraw(args.amount):
        account.display_balance
    else:
        print("Insufficient funds")
elif args.action == "balance":
    account.display_balance
