# # 4. Write a Python program to check if a number provided by the user is prime or not.

# chk_num = int(input("Enter a Number : "))

# for i in range(chk_num):
#     if chk_num %2==0:
#         print("Its a Prime!")
#     else:
#         print("Its Not Prime!")

for i in range(1,16):
    if i>1:
        for j in range(2,i):
            if (i%j) ==0:
                break
        else:
             print(i)