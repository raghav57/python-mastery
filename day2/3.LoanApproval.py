# -------------------------
# Problem:
# Loan Approval
# -------------------------

#Input

monthly_salary = float(input("Enter Monthly Salary: "))
credit_score = float(input("Enter Credit Score: "))

#Processing

line = "-" * 35

print()
print(line)


if monthly_salary>=0 and credit_score>=0:
    if monthly_salary>=50000 and credit_score >=700:
        status="Loan Approved"
        print(status)
    else:
        status="Loan Rejected"

        print(status)

        if monthly_salary<50000 and credit_score>=700:
            reason = "Rejected because salary is too low."

        elif monthly_salary>=50000 and credit_score<700:
            reason = "Rejected because credit score is too low."

        else:
            reason = "Rejected because both credit score and salary are too low"
        
        print(reason)

    print(line)
else:
    print("Invalid Input")