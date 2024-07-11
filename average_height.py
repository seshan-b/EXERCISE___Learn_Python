### Pseudo Code ###
# Get user input for a list of student heights and split the input into individual heights.
# Loop through each height and convert it to an integer.
# Print the list of student heights.
# Initialize total_height to 0 and loop through the list to sum up all the heights.
# Print the total height.
# Initialize number_of_students to 0 and loop through the list to count the number of students.
# Print the number of students.
# Calculate the average height by dividing total_height by number_of_students and rounding the result.
# Print the average height.


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
    number_of_students += 1
print(number_of_students)


# Get average height
average_height = round(total_height / number_of_students)
print(average_height)
