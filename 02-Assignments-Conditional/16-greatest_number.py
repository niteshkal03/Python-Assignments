# 17.Find the greatest number. 

first = int(input("Enter first number : "))
second = int(input("Enter second number : "))
third = int(input("Enter third number : "))
print()

if first > second and first > third:
    print(f"Greatest Number : {first}")

elif second > first and second > third:
    print(f"Greatest Number : {second}")

elif third > first and third > second:
    print(f"Greatest Number : {third}")
else:
    print("Something Went Wrong")