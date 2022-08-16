

# Get input from user
student_heights = input("Input a list of student heights ").split()

# Loop through the input heights
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


# Sum up all the heights
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)


# Get number of students
number_of_students = 0
for student in student_heights: