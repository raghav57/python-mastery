# input
i=0
d=0
while i<8 or d==0:
    i=0
    d=0
    password = input("Enter password: ")
    for ch in password:
        i+=1
        if ch.isdigit():
            d=1
    print(i)
    print(d)

    
