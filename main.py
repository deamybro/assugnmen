#NAME: mebo chukwudiebube kingsley
#dept: software
#reg: 2024934048

#pseudo side
# #BEGIN
#     INPUT student_score
#
#     IF student_score >= 70 AND student_score <= 100 THEN
#         grade = "A"
#     ELSE IF student_score >= 60 AND student_score <= 69 THEN
#         grade = "B"
#     ELSE IF student_score >= 50 AND student_score <= 59 THEN
#         grade = "C"
#     ELSE IF student_score >= 45 AND student_score <= 49 THEN
#         grade = "D"
#     ELSE IF student_score >= 40 AND student_score <= 44 THEN
#         grade = "E"
#     ELSE
#         grade = "F"
#     END IF
#
#     OUTPUT "Your grade is: " + grade
# END


#python side
def get_grade(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score <= 69:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 45 <= score <= 49:
        return "D"
    elif 40 <= score <= 44:
        return "E"
    else:
        return "F"

try:
    student_score = int(input("Enter your score (0-100): "))
    if 0 <= student_score <= 100:
        grade = get_grade(student_score)
        print(f"Your grade is: {grade}")
    else:
        print("Invalid score. Please enter a value between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numerical score.")








