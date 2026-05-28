# 10. Write a Python program to display all letters except 'm' and 'i' from the string 
# "Dreamer infotech".

str1 = "Dreamer infotech"
for i in str1:
    if i == "m" or i=="i":
        continue
    print(i, end=" ")