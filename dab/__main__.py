from dab.account import *

bank = [
  Account(1, "Jean", 275.30),
  Account(2, "Mathilde", 7530.00),
  Account(3, "George", 52.60)
]

print("Welcome to PyBank!")

number = int(input("Enter your account number: "))

try:
  account = bank.index(Account(number))
except ValueError:
  print("Invalid account number")
  sys.exit(1)

account = bank[account]

print(f"Hello {account.client}!")
print(account)

operation = float(input("How can we help you today? (type '-amount' to withdraw <amount> € or '+amount' to deposit <amount> €) "))

if operation > 0:
  account.deposit(operation)
elif operation < 0:
  account.withdraw(operation)
else:
  print("Invalid operation", file=sys.stderr)
  sys.exit(1)
