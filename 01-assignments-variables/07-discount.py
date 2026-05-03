# 8. Apply a 20% discount to a price
price = 1000
discount = 20
print(f"Before Discount the Price is (Rs.): {price}")
print(f"The Discount is: {discount}%")
print()
discount = (price * discount)/100
discount_price = price - discount

print(f"After Discount The Price is (Rs.): {discount_price}")