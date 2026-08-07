#Input 

number_of_tables = 10
number_of_seats = 4
table = ""
for i in range(number_of_tables):
    seats =""
    table = "Table" + str(i+1) +" --->"
    for j in range(number_of_seats):
        seats = seats +"Seat " + str(j+1) +" "
    print(f"{table} {seats}")
