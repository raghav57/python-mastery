# Age calculation problem
from datetime import datetime

age = int(input("Please enter your current age: \n"))

current_year = datetime.now().year

print(50* "=")
print("AGE PROJECTION")
print(50*"=")
print(f"Age after 5 years  :{age+5}     (Year: {current_year + 5})")
print(f"Age after 10 years :{age+10}    (Year: {current_year + 10})")
print(f"Age after 20 years :{age+20}    (Year: {current_year + 20})")
print(50*"=")
