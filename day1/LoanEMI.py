#Assumptions

# Simple interest calculated for entire tenure
# Total repayment calculated compounded annually
# Input

loan = float(input("Enter Loan Amount: "))
int_rate = float(input("Enter Interest Rate % : "))
loan_term = int(input("Enter Loan Term in years: "))

#Processing
simple_int = (loan*int_rate * loan_term)/100
total_rep_amount_simp = loan + simple_int
total_rep_amount_comp = loan * ((1+int_rate/100) ** loan_term)
comp_interest = total_rep_amount_comp - loan

interest_diff = comp_interest - simple_int

#Output
print(f"Simple Interest = {simple_int :.2f}")
print(f"Compound Interest (compounted annually)= {comp_interest :.2f}")
print(f"Total Repayment Amount with Simple Interest= {total_rep_amount_simp:.2f}")
print(f"Total Repayment Amount with Compound Interest= {total_rep_amount_comp:.2f}")
print(f"Difference between Compound Interest and Simple Interest:{interest_diff:.2f}")

