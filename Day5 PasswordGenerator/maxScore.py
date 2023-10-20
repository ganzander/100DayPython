# Input a list of student scores
student_scores = [197, 258, 312, 90]
max = 0
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if student_scores[n] > student_scores[max]:
        max = n
print(f"The highest score in the class is: {student_scores[max]}")
