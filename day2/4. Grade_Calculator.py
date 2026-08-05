#Input

student_name = input("Enter Student Name: ")
marks = float(input("Enter Marks: "))

# processing
if marks>=0 and marks<=100:
    if marks>=90:
        grade="A"
    elif marks>=80:
        grade="B"
    elif marks>=70:
        grade="C"
    elif marks>=60:
        grade="D"
    else:
        grade="Fail"

#output

    line = "-" * 35
    print(line)
    print(f"{student_name}'s Report Card")
    print(line)

    print()
    print(line)
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
    print(line)
else: 
    print("Marks must be between 0 and 100")