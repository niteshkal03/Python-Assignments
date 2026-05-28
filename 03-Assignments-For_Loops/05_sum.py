# 5. Write a Python program to calculate the sum of numbers between a starting and 
# ending point provided by the user. 

start_num = int(input("Enter Your Starting Number : "))
end_num = int(input("Enter Your Ending Number : "))
sum1 = 1
for i in range(start_num, end_num):
    sum1=sum1+i
print(f"The sum is : {sum1}")