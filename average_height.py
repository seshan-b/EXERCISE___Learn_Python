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

# Get input from user and split it into a list of heights
student_heights = input("Input a list of student heights ").split()

# Convert each height from a string to an integer
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# Initialize total_height to 0 and sum up all the heights
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

# Initialize number_of_students to 0 and count the number of students
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

# Calculate the average height and round it
average_height = round(total_height / number_of_students)
print(average_height)