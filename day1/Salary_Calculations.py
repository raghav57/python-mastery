
#Input
monthly_salary = float(input("Enter Monthly Salary: "))
annual_bonus   = float(input("Enter Annual Bonus: "))
tax_percent = float(input("Enter tax percent in %: "))

#Processing 

annual_salary_b_tax = monthly_salary * 12
tax_amount = annual_salary_b_tax * (tax_percent/100)
net_annual_salary = annual_salary_b_tax * (1-tax_percent/100)
avg_monthly_takehome = net_annual_salary/12
bonus_after_tax = annual_bonus * (1-tax_percent/100)

#Output

print(f"Annual Salary before tax    :{annual_salary_b_tax:.2f}")
print(f"Annual Tax                  :{tax_amount:.2f}")
print(f"Net Annual Salary           :{net_annual_salary:.2f}")
print(f"Average Monthly Salary      :{avg_monthly_takehome:.2f}")
print(f"Annual Bonus after tax      :{bonus_after_tax:.2f}")




