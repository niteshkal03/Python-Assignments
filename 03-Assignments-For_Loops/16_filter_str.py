# 16. Write a Python program to filter out all vowels and consonants from a string 
# entered by the user.
str1 = input("Enter Your String : ")
for i in str1:
    if i in "aeiouAEIOU":
        print(f"Vowels : {i}")
    else:
        print(f"Consonants : {i}")