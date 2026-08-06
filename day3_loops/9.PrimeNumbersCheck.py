# Input 

number = int(input("Enter a number: "))

prime_check = 0

for i in range(number):
    check = (number%(i+1))
          
    if (i != 0 and i != (number-1)) and check==0:
        prime_check = 1
        break

if number == 1 or number ==0:
    print("Number is neither nor composite")
elif prime_check == 0:
    print("Number is prime")
else:
    print("Number is composite")