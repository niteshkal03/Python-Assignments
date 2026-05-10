# 7. Task: Students Interview Eligibility Checker 
 # ○ Academic Score (percentage): 
score = float(input("Student's Academic Score (%) : ")) 

#Attendance Percentage:  
attend_per = float(input("Student's Attendance Percentage (%) : ")) 

#Extracurricular Participation: 
extra_act = input("Student's Extracurricular Participation (Yes/No) : ")

# Conditions for Interview Eligibility:
# 1. The student’s academic score must be 60 or above. 
if score >= 60:
    print("First Condition is Matched")

# 2. The student’s attendance percentage must be 75 or above. 
    if attend_per >= 75:
       print("Second Condition is Matched")
       
# 3. The student should have participated in at least one extracurricular activity. 
       if extra_act == "Yes":
            print("Eligible for Interview")
       else:
           print("Not Eligible for Interview Due to Extra Activities")
    else:
        print("Not Eligible for Interview Due Attendance Percentage")
else:
    print("Not Eligible for Interview Due Academic Score")

    


           
           
           

# Output: 
# ● If the student meets all three conditions print "Eligible for Interview". 
# ● If the student fails to meet any of the conditions print "Not Eligible for Interview". 