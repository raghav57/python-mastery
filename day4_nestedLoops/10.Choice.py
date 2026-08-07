# Menu

choice = ""

while True:
    choice = input("Enter your choice (only number) \n 1. Rectangle: \n 2. Triangle: \n 3. Multiplication:" \
" \n 4. Exit to exit: ")
    if choice == '1':
        rect_rows = int(input("Enter rows: "))
        rect_columns = int(input("Enter Columns: "))
        for i in range(rect_rows):
            for j in range(rect_columns):
                print("*",end=" ")
            print()
    elif choice == '2':
        triangle_height = int(input("Enter Triangle Height: "))
        for i in range(triangle_height):
            for j in range(i+1):
                print("*",end=" ")
            print()
    elif choice == '3':
        number = int(input("Enter n for n by n multiplication table: "))
        for i in range(number):
            for j in range(number):
                print(f"{(i+1) * (j+1) :4}",end="")
            print()
    elif choice == '4':
        print("Thank you")
        break
    else:
        print("Invalid Choice")