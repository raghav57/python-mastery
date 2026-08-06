#Input

number = int(input("Enter number: "))

if number>=0:
    i = 1
    product=1
    while i<=number:
        product*=i
        i+=1
    print(f"{number}! = {product}")
else:
    print("Number cannot be negative")

    

