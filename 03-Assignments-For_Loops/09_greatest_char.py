# 9. Write a Python program to find the greatest character from the string "python". 
str1 = "python"
for i in str1:
    if str1[0] > str1[1]:
        print(str1[0])
    else:
        print(str1[1])