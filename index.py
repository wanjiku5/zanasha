



exam_scores = int (input("Enter the student's exam score: "))

if exam_scores >= 90:
     grade = 'A'
elif exam_scores >= 80:
     grade = 'B'
elif exam_scores >= 70:
    grade = 'C'
elif exam_scores >= 60:
    grade = 'D'
else:
    grade = 'F'
print("The student's grade is: " , grade)

