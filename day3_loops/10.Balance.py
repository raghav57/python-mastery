#Input

name=""


num_cust = 0
total=0
max_balance = 0
min_balance=float("inf")

while True:
    name = input("Enter Your Name or type exit: ")

    if name.lower()=="exit":
        break

    balance = -1
    while balance < 0 :
        balance = float(input("Enter Balance: "))
        if balance<0:
            print("Invalid Input")

    num_cust+=1
    total+=balance

    if balance > max_balance:
        max_balance = balance
        max_balance_cust = name

    if balance < min_balance:
        min_balance = balance
        min_balance_cust = name


line = 50 * "="


print(line)

print(f"Total Number of customers: {num_cust}") 

print(f"Total balance: {total}") 

print(f"Average balance: {total/num_cust :.2f}")

print(f"Maximum balance: {max_balance :.2f}")

print(f"Richest customer: {max_balance_cust}")

print(f"Minimum balance: {min_balance :.2f}")

print(f"Poorest customer: {min_balance_cust}")

print(line)




    