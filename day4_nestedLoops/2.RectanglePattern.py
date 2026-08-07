#input 

rect_rows = int(input("Enter Rows: "))
rect_columns = int(input("Enter Columns: "))

for i in range(rect_rows):
    for j in range(rect_columns):
        print("* ",end="")
    print()
