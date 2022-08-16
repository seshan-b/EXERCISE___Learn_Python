

# Get input from user
student_heights = input("Input a list of student heights ").split()

# Loop through the input heights
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


# Sum up all the heights
total_height = 0