amount = int(input("enter your amount"))
if amount >= 5000:
    print("eligible for the discount")
elif (amount > 0) and (amount < 5000):
    print("not eligible")
else:
    print("not eligible for the shopping")
