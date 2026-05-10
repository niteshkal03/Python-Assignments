# 8. Task: Validating Email Domain 
 
email = input("Enter Your Email: ")
#Check if the entered email address contains the domain "gmail.com". 
domain = "gmail.com"

if domain in email:
    print("Yor Are Eligible for Registration")
else:
    print("Email is Not Eligible for Registration")
    

