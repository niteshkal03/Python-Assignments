# 11. Write a Python program to print alternate characters from a given string. 

str1 = "Nitesh"
size = len(str1)

print(f"Given Strings : {str1}")
print("="*25)
print("Alternate Characters : ")

for i in range(0,size,2):
    print(str1[i], end=" ")