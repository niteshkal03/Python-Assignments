# 3. Write a Python program to generate a table of a number provided by the user.

usr_table = int(input("Enter Your Number for Table : "))

for i in range(1,11):
    print(f"{usr_table} x {i} = {usr_table*i}")