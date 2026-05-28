# 15. Write a Python program that allows the user to search for a character within a 
# given string. 
str1 = "Python Programming"
search = input("Enter a Character of given String : ")
print()
print(f"Word is : {str1}")
for i in str1:
    if search in str1:
        print(f"""Yes, "{search}" is present in given string.""")
        break
    else:
        print(f""""{search}" is not present in given string.""")
        break