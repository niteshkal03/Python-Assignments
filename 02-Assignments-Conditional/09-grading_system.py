# 10.Task : Student Grading System 
 
marks = int(input("Enter Your Marks: "))

# Grade A: 90–100 
if marks >= 90 and marks <=100:
    print(f"Marks: {marks} -> Grade A")

# Grade B: 80–89 
elif marks >= 80 and marks <=89:
    print(f"Marks: {marks} -> Grade B ")

# Grade C: 70–79 
elif marks >= 70 and marks <=79:
    print(f"Marks: {marks} -> Grade C")

# Grade D: 60–69 
elif marks >= 60 and marks <=69:
    print(f"Marks: {marks} -> Grade D")

# Grade E: 50–59 
elif marks >= 50 and marks <=59:
    print(f"Marks: {marks} -> Grade E")

# Grade F: 0–49 
elif marks >= 0 and marks <=49:
    print(f"Marks: {marks} -> Grade F")

# Invalid marks: Outside the range 0–100. 
else:
    print(f"Marks: {marks} -> Invalid Marks")


  