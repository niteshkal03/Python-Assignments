# 6. Task: Bank Loan Approval System 
# ● Objective: You have to create a javascript script that checks whether an user is 
# eligible for a bank loan based on various criteria. 
# ● Hints: 
# ○ The applicant's age must be between 18 and 60 years. 
# ○ The applicant's monthly income must be greater than or equal to ₹25000. 
# ○ The applicant's credit score must be greater than or equal to 700. 
# ○ The applicant must not have any outstanding debts greater than ₹10000 
# 1. Output: 
# ○ Display "Loan Approved" if the applicant meets all the conditions. 
# ○ Otherwise display "Loan Rejected".
age = int(input("Applicant's Age : "))

if age >= 18 and age <= 60:
    print("Your age is Eligible")

    income = int(input("Applicant's Monthly Income : "))
    if income >= 25000:
        # print("The Applicant's Monthly Income Fullfill our Criteria")
        debts = int(input("Applicant's Outstanding Debts : "))
        if debts <= 10000:
            # print(f"The Applicant's Credit Score Fulfill our Criteria ")
            credit_score = int(input("Applicant's Credit Score : "))
            if credit_score >= 700:
                print("Loan Approved")
            else:
                print("Loan Rejected")
        else:
            print("Loan Rejected")   
    else:
        print("Loan Rejected")
else:
    print("Loan Rejected")