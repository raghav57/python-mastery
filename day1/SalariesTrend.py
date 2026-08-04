#input

salaries=[120000,
90000,
150000,
130000,
110000
]

#processing
total_payroll = sum(salaries)
highest_salary = max(salaries)
lowest_salary = min(salaries)
average_salary = sum(salaries)/len(salaries)

#Output
print(f"Highest Salary  : {highest_salary :.2f}")
print(f"Lowest Salary   : {lowest_salary :.2f}")
print(f"Average Salary  : {average_salary :.2f}")
print(f"Total payroll   : {total_payroll :.2f}")


