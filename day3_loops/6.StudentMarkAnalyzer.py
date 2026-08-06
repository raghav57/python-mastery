# Input

num_of_students = int(input("Enter number of Students: "))


# Processing

#intiailization
i=0
sum_marks = 0
max_marks = 0
min_marks = 101
pass_students=0

while i < num_of_students:
    mark=-1
    while mark < 0 or mark > 100 :
        mark = int(input(f"Enter the marks of student {i+1}: "))
        if mark < 0 or mark > 100:
            print("Invalid Input")
    sum_marks += mark
    if mark > max_marks:
        max_marks = mark
    if mark < min_marks:
        min_marks = mark


    if mark>=40:
        pass_students+=1

    i+=1

#Output

line = 50 * "="


print(line)

print(f"Total Number of students: {num_of_students}") 

print(f"Average marks: {sum_marks/i :.2f}")

print(f"Maximum marks: {max_marks}")

print(f"Minimum marks: {min_marks}")

print(f"Number of passing students: {pass_students}")

print(line)




