#Input

annual_income = float(input("Enter Annual Income: "))

#Processing

if annual_income>=0:
    if annual_income>1000000:
        tax_rate = 20
    elif annual_income>500000:
        tax_rate = 10
    else:
        tax_rate = 0
    tax=annual_income*tax_rate/100
    net_income = annual_income - tax
    print("\n---------------------------")
    print("ANNUAL TAX REPORT")
    print("---------------------------")
    print(f"Gross Annual Income : {annual_income:.2f}")
    print(f"Tax: {tax :.2f}")
    print(f"Net Income:{net_income:.2f}")
    print(f"Effective Tax Rate  : {tax_rate} %")
    print("---------------------------")
else:
    print("Invalid Input")

