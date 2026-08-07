##Input

num_of_students = 5
num_of_subjects = 3

for i in range(num_of_students):
    total = 0
    for j in range(num_of_subjects):
        mark=101
        while mark < 0 or mark > 100:
            mark = float(input(f"Enter subject {j+1} marks of student {i+1}: "))
            if mark < 0 or mark > 100:
                print("Invalid marks")
        total+= mark
    print(f"Total marks of student {i+1}: {total}")
    average_marks = total/num_of_subjects
    print(f"Average marks of student {i+1}: {average_marks:.2f} ")
            



