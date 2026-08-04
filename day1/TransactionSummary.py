#Input 

customer_name = input("Enter Your Name: ")
opening_balance = float(input("Enter Opening Balance: "))
deposit_amount = float(input("Enter Deposit amount: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))

#Processing
closing_balance = opening_balance + deposit_amount - withdrawal_amount

print(50*"*")

print(f"Customer: {customer_name}")
print(f"Opening Balance: {opening_balance :.2f}")
print(f"Deposit Balance: {deposit_amount :.2f}")
print(f"Withdrawal Balance: {withdrawal_amount :.2f}")

if (closing_balance)<0:
    print("Warning: You are utilizing overdraft limit")
    print(f"Overdraft Limit Utilized: {closing_balance :.2f}")
else:
    print(f"Closing Balance: {closing_balance :.2f}")

print(50*"*")



