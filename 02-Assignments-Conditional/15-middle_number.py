# 16.Finding the Middle Number 
# ○ Task: Write a program to determine the middle number among three inputs. 
# ○ Input: Prompt the user to enter three numbers. 
# ○ Processing: Identify the middle number, which is neither the largest nor the 
# smallest. 
# ○ Output: Display the middle number.
a = int(input("Enter Your First Number : "))
b = int(input("Enter Your Second Number : "))
c = int(input("Enter Your Third Number : "))

if a <= b and a >= c:
     print(a)
elif b <= a and b >= c:
     print(b)
else:
     print(c)
