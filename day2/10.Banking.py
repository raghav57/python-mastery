#Input

name = input("Enter your Name: ")
account_type = input("Enter Account Type: ")
balance = float(input("Enter Balance: "))
monthly_salary = float(input("Enter Monthly Salary: "))
loan_amount = float(input("Enter Loan Amount: "))
credit_score = int(input("Enter Credit Score: "))

#Assumptions

# Premium Account Eligibility
# (balance > 10,00,000/- or 
# monthly salary > 3,00,000) and
# credit score>=800
# premium account eligibility = yes else no
# loan eligibility
# credit_score <=550  strict no
# credit_score between 550 and 750 risky but if loan amount is less than 3,00,000 then yes
# credit_score above 750 loan eligibility = yes


# Premimum Account
if balance>=0 and monthly_salary>=0 and loan_amount>=0 and credit_score>=0:
    # premium account eligibility
    if (balance > 1000000 or monthly_salary > 300000) and credit_score>=800:
        premium_account_eligibility = "Eligible for premium account"
        recommendation_prem = "You are a premium account membert"
    else: 
        premium_account_eligibility = "no"
        if balance <= 1000000:
            recommendation_prem = "Maintain balance of more than 10,00,000/-"
        elif monthly_salary <= 300000:
            recommendation_prem = "You salary needs a correction to be part of premium banking services:)"
    
    # Loan eligibility
    if credit_score>=750:
        loan_eligibility = "Eligible for loan"
        recommendation_loan = "You are eligible for all Loans"
        risk_level = "Low"
    elif credit_score>=550:
        if loan_amount <= 300000:
            loan_eligibility = "Eligible for loan"
            recommendation_loan = "You are eligible but be cautious with your credit score"
        else:
            loan_eligibility = " Not Eligible for loan"
            recommendation_loan = "Your existing loan amount is too high for your credit score"
        risk_level = "Medium"
    else:
            loan_eligibility = " Not Eligible for loan"
            recommendation_loan = "Your really need to work on your credit score and payments"

    line = "=" * 50

    print()
    print(line)
    print("CUSTOMER ASSESSMENT")
    print(line)
    print(f"Customer Name           : {name}")
    print(f"Account Type            : {account_type}")
    print(f"Credit Score            : {credit_score:.0f}")
    print(f"Balance                 : ₹{balance:.2f}")
    print(f"Loan Amount             : ₹{loan_amount:.2f}")
    print(f"Risk Level              : {risk_level}")
    print(f"Eligibility for premium account: {premium_account_eligibility}")
    print(f"Eligibility for loan: {loan_eligibility}")
    print(f"Recommendation for premium account: {recommendation_prem}")
    print(f"Recommendation for loan: {recommendation_loan}")
    print(line)

else:
    print("Invalid Input")

# Output

            





