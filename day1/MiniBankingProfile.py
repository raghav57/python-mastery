#Inputs
customer_name = input("Enter Customer Name: ")
account_name = input("Enter Account Number: ")
account_type = input("Enter Account type: ")
current_balance = float(input("Current Balance: "))
loan_amount = float(input("Enter Loan amount: "))
credit_score = float(input("Enter Credit Score: "))

#processing

total_assets = current_balance + loan_amount

if credit_score>=750:
    risk_category = "Low Risk"
elif credit_score>=650:
    risk_category = "Medium Risk"
else:
    risk_category = "High Risk"

#Output

print(50*"*")

print(f"*   Your total assets are {total_assets :.2f} *")
print(f"*   Your are a {risk_category} customer       *")

print(50*"*")


