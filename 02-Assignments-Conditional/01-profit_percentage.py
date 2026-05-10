# 1. Task: Calculate Profit Percentage  
#Display the profit or loss and the respective percentage.

cost_price = int(input("Enter Your Cost Price : "))
selling_price = int(input("Enter Your Selling Price : "))
print("="*35) #Use for Alignment

#Formula Used For Profit
profit = selling_price - cost_price

#Formula Used For Loss
loss = cost_price - selling_price

if selling_price > cost_price:
    print(f"Your are in profit and it is (Rs.): {profit}")
    # Profit Percentage
    profit_percentage = (profit / cost_price) * 100
    print(f"The Profit Percentage is (%): {profit_percentage}") 

elif selling_price < cost_price:
    print(f"Your are in Loss and it is (Rs.): {loss}")
    #Loss Percentage
    loss_percentage = (loss / cost_price) * 100
    print(f"The Loss Percentage is (%): {loss_percentage}")

else:
    print("You have No Profit and No Loss !! ")
    print()





