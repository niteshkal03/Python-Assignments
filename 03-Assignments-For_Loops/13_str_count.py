# 13. Write a Python program to count the total number of characters in a string 
# entered by the user.
str1 = input("Enter a Word : ")
count = 0
for i in str1:
    count+=1  
print(f"Total Number of Characters : {count}")