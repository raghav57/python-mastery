#Input

row_num = int(input("Enter number of rows: "))
column_num = int(input("Enter the number of columns: "))

for i in range(row_num):
    row_column = ""
    for j in range(column_num):
        row_column = row_column + "R"+str(i+1)+"C"+str(j+1)+" "
    print(row_column)