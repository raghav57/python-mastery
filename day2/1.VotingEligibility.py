#Input 

name = input("Enter your Name: ")
age = int(input("Enter Age: "))

while age<0:
    age = int(input("Enter valid age, Age cannot be negative: "))

#Processing and Output

print("\n---------------------------")
print("VOTER ELIGIBILITY REPORT")
print("---------------------------")
print(f"Name : {name}")
print(f"Age  : {age}")

if age >= 18:
    print("Status : Eligible to Vote")
else:
    print("Status : Not Eligible to Vote")

print("---------------------------")



