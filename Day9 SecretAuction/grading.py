student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}
msg=""

for scores in  student_scores:  
  if(student_scores[scores]<=70):
    msg="Fail"
  elif(student_scores[scores]<=80):
    msg="Acceptable"
  elif(student_scores[scores]<=90):
    msg="Exceeds Expectations"
  elif(student_scores[scores]<=100):
    msg="Outstanding"
  student_grades[scores]=msg
  
print(student_grades)  