# 15. Tax Calculation for Car Purchase 
# Write a  program to calculate the tax on a car purchase based on the car brand and its price. 
# 5. Input: The car brand and price. 
# 6. Output: The calculated tax on the purchase.
car1 = "mahindra"
car2 = "audi"
car3 = "jaguar"
car4 = "mercedes"

brand = input("Enter Car Brand : ")
price = int(input("Enter Your Price (Lakh) : "))

# 1. Mahindra: 5% tax for prices between 7L (7 lakh) and 10L. 
if brand == car1 and price >= 700000 and price <=1000000:

    tax_rate = 5
    tax = (price * tax_rate) / 100
    print()
    print(f"Tax on the Purchase (%) : {tax}")

# 2. Audi: 10% tax for prices between 10L and 15L. 
if brand == car2 and price >= 1000000 and price <=1500000:

    tax_rate = 10
    tax = (price * tax_rate) / 100
    print()
    print(f"Tax on the Purchase (%) : {tax}")

# 3. Jaguar: 25% tax for prices between 15L and 20L. 
elif brand == car3 and price >= 1500000 and price <=2000000:

    tax_rate = 25
    tax = (price * tax_rate) / 100
    print()
    print(f"Tax on the Purchase (%) : {tax}")

# 4. Mercedes: 30% tax for prices between 20L and 25L. 
elif brand == car4 and price >= 2000000 and price <=2500000:

    tax_rate = 30
    tax = (price * tax_rate) / 100
    print()
    print(f"Tax on the Purchase (%) : {tax}")

else:
    print("Something went Wrong!")