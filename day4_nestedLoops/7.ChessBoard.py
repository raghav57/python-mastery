#Chess Board

symbol1="O"
symbol2="X"


for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
                print(symbol1,end=" ")
        else:
                print(symbol2,end=" ")
    print()

