# 21.UPSC Selection Process 
cut_off = 120
age = int(input("Please Enter Your Age : ")) 

if age >=21 and age <=32:
    graduation = input("Enter Your Graduation Status (graduate): ")
    if graduation.lower() == "graduate":
        nationality = input("Enter Your Nationality : ")
        if nationality.lower() == "indian":
            print("Proceed Prelims.")
            pre_score = int(input("Enter Your Prelims Score : "))
            if pre_score >= cut_off:
                print("Proceed to Mains.")
                main_score = int(input("Enter Your Mains Score : ")) 
                if main_score >= cut_off:
                    print("Proceed to Interview.")
                    int_score = int(input("Enter Your Interview Score : "))
                    if int_score >= cut_off:
                        print("Congratulations! You have cleared the UPSC.") 
                    else:
                        print("You failed the Interview.")   
                else:
                    print("You failed the Mains.")
            else:
               print("You failed the Prelims.") 
        else:
            print("Your Nationality is not Matched !!")
    else:
        print("You Are Not Graduated")
else:
    print("Your Age is Not Matched to our Criteria.")