

# Get Student Scores
student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)


# A simple way to write this code above.
# max_score = max(student_scores)
# print(f"The highest score in the class is: {max_score}")

highest_score = 0

for score in student_scores:
      if score > highest_score: