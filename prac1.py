price = float(input("enter the price of the item "))
quantity = float(input("enter product quantitiy"))
total_price =price*quantity
gst=total_price*(18/100)
final_amount= total_price+gst
print("your bill is : ",final_amount)
