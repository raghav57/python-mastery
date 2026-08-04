#Assumptions

# Maximum marks: 100 for each subject

#input

marks = []

marks.append(float(input("Mathematics: ")))
marks.append(float(input("Science: ")))
marks.append(float(input("English: ")))
marks.append(float(input("Social Studies: ")))
marks.append(float(input("Computer Science: ")))

total_marks = sum(marks)
average_marks = total_marks / len(marks)
highest_marks = max(marks)
lowest_marks = min(marks)

#Output
print(f"Total Marks  :{total_marks}")
print(f"Average Marks  :{average_marks}")
print(f"Highest Marks  :{highest_marks}")
print(f"Lowest Marks  :{lowest_marks}")



