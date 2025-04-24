seat_no = input("Enter seat number: ")
student_id = input("Enter student ID: ")
name = input("Enter student name: ")

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total_marks = sum(marks)
average = total_marks / 5

print("Seat No:", seat_no)
print("Student ID:", student_id)
print("Name:", name)
print("Total Marks:", total_marks)
print("Average Marks:", average)