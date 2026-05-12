# 19.Calculate Class Attendance Percentage 
# ○ Task: Write a program to calculate the percentage of classes attended by a 
# student and determine their eligibility to sit in the exam. 
# ○ Conditions: 
# ■ Attendance percentage < 75%: Not eligible to sit in the exam. 
# ■ Attendance percentage ≥ 75%: Eligible to sit in the exam. 
# ○ Output: Display the attendance percentage and eligibility status. 
attendance_per = int(input("Enter Your Attendance Percentage (%): "))
print()

if attendance_per < 75:
    print("You Are Note Eligible to Sit in the Exam.")
elif attendance_per >= 75:
    print("You are Eligible to sit in the Exam.")
