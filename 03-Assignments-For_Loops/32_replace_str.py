# 32.Task: Replace Character in String 
# Write a program that takes a string input from the user, then asks for a character 
# to replace and the character to replace it with. The program should output the 
# modified string where all occurrences of the specified character are replaced by 
# the replacement character.
str1 = input("Enter Your string : ")
ask_usr = input("Which Character you want to replace into this string ? : ")
replace_char=input("Enter Your choice to replace character : ")
for i in str1:
    if ask_usr in i:
        
        print(f"DO you want to change : {ask_usr}")
 