# ---------------------------------
# Problem 9 - Customer Risk Assessment
# ---------------------------------

# Assumptions
# 1. Age must be between 18 and 100.
# 2. Credit score must be between 0 and 1000.
# 3. Loan amount cannot be negative.
#
# Business Rules
# Credit Score
#   < 500  -> High Risk
#   500-749 -> Medium Risk
#   >=750 -> Low Risk
#
# Loan Amount
#   > 800000 increases risk by one level
#
# Age
#   > 60 increases risk by one level
#
# Risk Priority
# Low -> Medium -> High

# -------------------------
# Input
# -------------------------

name = input("Enter Customer Name: ")
age = int(input("Enter Age: "))
credit_score = float(input("Enter Credit Score: "))
loan_amount = float(input("Enter Existing Loan Amount: "))

# -------------------------
# Validation
# -------------------------

if not (18 <= age <= 100 and
        0 <= credit_score <= 1000 and
        loan_amount >= 0):

    print("Invalid Input")

else:

    # -------------------------
    # Base Risk
    # -------------------------

    if credit_score < 500:
        risk = "High"

    elif credit_score < 750:
        risk = "Medium"

    else:
        risk = "Low"

    # -------------------------
    # Loan Modifier
    # -------------------------

    if loan_amount > 800000:

        if risk == "Low":
            risk = "Medium"

        elif risk == "Medium":
            risk = "High"

    # -------------------------
    # Age Modifier
    # -------------------------

    if age > 60:

        if risk == "Low":
            risk = "Medium"

        elif risk == "Medium":
            risk = "High"

    # -------------------------
    # Recommendation
    # -------------------------

    if risk == "Low":
        recommendation = "Eligible for premium banking products."

    elif risk == "Medium":
        recommendation = "Review income documents before approval."

    else:
        recommendation = "Detailed credit review required before approval."

    # -------------------------
    # Output
    # -------------------------

    line = "=" * 50

    print()
    print(line)
    print("CUSTOMER RISK ASSESSMENT")
    print(line)
    print(f"Customer Name : {name}")
    print(f"Age           : {age}")
    print(f"Credit Score  : {credit_score:.0f}")
    print(f"Loan Amount   : ₹{loan_amount:.2f}")
    print(f"Risk Level    : {risk}")
    print(f"Recommendation: {recommendation}")
    print(line)