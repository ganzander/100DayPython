student_heights = [197, 258, 312]
sum_heights = 0
count = 0

for n in range(0, len(student_heights)):
    sum_heights = sum_heights + student_heights[n]
    count = count + 1

total_students = count
total_height = sum_heights
average_heights = round(sum_heights / count)
print("total height = " + str(total_height))
print("number of students = " + str(total_students))
print("average height = " + str(average_heights))
