# 8. Write a Python program to calculate the factorial of a number provided by the 
# user.

# start_num = int(input("Enter Your Starting Number : "))
num = int(input("Enter Your Number : "))
mul = 1
for i in range(1,num):
    mul=mul*i
    print(f"The sum is : {mul}")