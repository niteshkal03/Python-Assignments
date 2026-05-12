# 20.Library Charge Calculation 

days = int(input("Enter the Number of Days a book has been borrowed : "))
print()

if days <= 5:
    lib_charge = days * 2
    print(f"The Library Charge for {days} days : {lib_charge}")

elif days >= 6 and days <= 10:
    lib_charge = days * 3
    print(f"The Library Charge for {days} days : {lib_charge} ")

elif days >= 11 and days <= 15:
    lib_charge = days * 4
    print(f"The Library Charge for {days} days : {lib_charge} ")

elif days > 15:
    lib_charge = days * 5
    print(f"The Library Charge for {days} days : {lib_charge} ")
else:
    print("Something Went Wrong")

