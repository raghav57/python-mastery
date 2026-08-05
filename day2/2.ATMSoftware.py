# #Input

# curr_balance = float(input("Enter Current Balance: "))
# withdrawal_amount = float(input("Enter withdrawal Amount: "))


# print("\n---------------------------")
# #processing and output

# if withdrawal_amount<0:
#     print("Invalid amount")

# if curr_balance < withdrawal_amount:
#     print("Insufficient Funds")
# else:
#     print("Withdrawal Successful")
#     updated_balance = curr_balance - withdrawal_amount
#     print(f"Updated Balance:{updated_balance :.2f}")


# print("---------------------------")


# -------------------------
# Problem:
# ATM Withdrawal
# -------------------------

# Input

current_balance = float(input("Enter current balance: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))

# Processing

if withdrawal_amount < 0:
    status = "Invalid withdrawal amount."
    updated_balance = current_balance

elif withdrawal_amount > current_balance:
    status = "Insufficient funds."
    updated_balance = current_balance

else:
    status = "Withdrawal Successful."
    updated_balance = current_balance - withdrawal_amount

# Output

line = "-" * 35

print()
print(line)
print("ATM TRANSACTION RECEIPT")
print(line)
print(f"Current Balance : ₹{current_balance:.2f}")
print(f"Withdrawal      : ₹{withdrawal_amount:.2f}")
print(f"Status          : {status}")
print(f"Updated Balance : ₹{updated_balance:.2f}")
print(line)
