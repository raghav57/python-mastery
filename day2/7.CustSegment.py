# Input

cust_balance = float(input("Enter Balance: "))

#Processing

if cust_balance>=0:
    if cust_balance < 10000:
        cust_type = "Basic"
    elif cust_balance < 100000:
        cust_type = "Silver Customer"
    elif cust_balance < 1000000:
        cust_type = "Gold Customer"
    else: 
        cust_type = "Platinum Customer"

    #Output
    print("\n---------------------------")
    print("CUSTOMER SEGMENT REPORT")
    print("---------------------------")
    print(f"Your Balance : {cust_balance:.2f}")
    print(f"Your Segment  : {cust_type}")
    print("---------------------------")
else: 
    print("Invalid Input")

