# 22. Menu-Driven Login System 
# 1. Create the Menu: 
# ○ Display a menu with three choices for the user: 
# ■ Login with Phone 
# ■ Login with Email 
# ■ Exit the system 
# 2. Predefined Credentials: 
# ○ Phone number: "1234567890" 
# ○ OTP: "1234" 
# ○ Email: "user@example.com" 
# ○ Password: "password123” 
# 3. Login Functionality: 
# ○ Option 1 (Login with Phone): 
# ■ Prompt the user to enter their phone number and OTP. 
# ■ Compare the input with a predefined phone number and OTP. 
# ■ Display success if both match or an error message if they don’t. 
# ○ Option 2 (Login with Email): 
# ■ Prompt the user to enter their email and password. 
# ■ Compare the input with predefined email and password. 
# ■ Display success if both match or an error message if they don’t. 
# ○ Option 3 (Exit): 
# ■ Display an exit message and terminate the program. 
# ○ Invalid Input: 
# ■ Handle invalid user choices and ask the user to select a valid option. 
# Output: 
# 1. If the user enters a valid phone number and OTP, display: "Login successful 
# with phone!" 
# 2. If the user enters valid email and password, display: "Login successful 
# with email!" 
# 3. If the user selects the exit option, display: "Exiting the program. Have a 
# nice day!" 
# 4. If the user enters invalid credentials or an invalid choice, display appropriate error 
# messages.
ph_no = "1234567890" 
otp = "1234" 
email = "user@example.com" 
password = "password123"

print("""
Predefined Credentials: 
○ Phone number: "1234567890" 
○ OTP: "1234" 
○ Email: "user@example.com" 
○ Password: "password123” """)
print("="*27)

print("""
Option 1 : Login with Phone.
Option 2 : Login with Email.
Option 3 : Exit the System.
""")

options = input("Enter Your Choice-(like 1, 2, 3): ")
if options == "1":
    mob_no = input("Enter Phone Number : ")
    otp1 = input("Enter Your OTP : ")

    if mob_no == ph_no and otp1 == otp:
        print("Login successful with phone!")
    else:
        print("Credentials Incorrect, Please Enter Correct!")

elif options == "2":
    email1 = input("Enter Phone Email : ")
    passwd = input("Enter Your Password : ")

    if email1 == email and passwd == password:
        print("Login successful with Email!")
    else:
        print("Credentials Incorrect, Please Enter Correct!")

elif options == "3":
        print("Exiting the program. Have a nice day!")

else:
    print("Invalid Choice, Please Select a Valid Option!")


