# 21.UPSC Selection Process 
# ○ Task: Simulate the UPSC selection process with the following steps: 
# 1. Eligibility Check 
# ■ Criteria: 
# ■ Age: 21–32 years.

# ■ Output: 
# ■ If eligible, proceed to Prelims. 
# ■ If ineligible, display the reason for ineligibility. 
# 2. Prelims Exam 
# ■ Processing: Check if the candidate’s score ≥ cut-off. 
# ■ Output: 
# ■ If passed, proceed to Mains. 
# ■ If failed, display "You failed the Prelims." 
# 3. Mains Exam 
# ■ Processing: Check if the candidate’s score ≥ cut-off. 
# ■ Output: 
# ■ If passed, proceed to Interview. 
# ■ If failed, display "You failed the Mains." 
# 4. Interview 
# ■ Processing: Check if the candidate’s score ≥ cut-off. 
# ■ Output: 
# ■ If passed, display "Congratulations! You have cleared the 
# UPSC." 
# ■ If failed, display "You failed the Interview." 
# ○ Final Output: Use nested conditional statements to simulate the entire process.
cut_off = 120
age = int(input("Please Enter Your Age : ")) 
graduation = input("Enter Your Graduation Status (graduate): ")
nationality = input("Enter Your Nationality : ")
if age >=21 and age <=32:
    if graduation == "Graduate":
        if nationality == "Indian":
            print("You Are Eligible for UPSC Prelims.")
            
        else:
            print("Your Nationality is not Matched !!")
    else:
        print("You Are Not Graduated")
else:
    print("Your Age is Not Matched to our Criteria.")