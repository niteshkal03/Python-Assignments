# 6. Write a Python program to calculate the product of numbers between a starting 
# and ending point provided by the user.

start_num = int(input("Enter Your Starting Number : "))
end_num = int(input("Enter Your Ending Number : "))
mul = 1
for i in range(start_num, end_num):
    mul=mul*i
print(f"The sum is : {mul}")