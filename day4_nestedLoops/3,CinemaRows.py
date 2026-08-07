# Cinema Rows

cinema_row = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for ch in cinema_row:
    for i in range(5):
        print((f"{ch}{i+1}"), end=" ")
    print("")
