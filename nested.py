amount = int(input("enter your amount"))
if amount >= 5000:
    print("eligible for the discount")

    print("enter mode of payement")
    mode = input("A-CASH \n B-CARD \n C-UPI")
    if mode == "B":
        print("discount applied")
    elif mode == "A" or mode == "C":
        print("discount not applicable on this method")
    else:
        print("incorrect input")
elif (amount > 0) and (amount < 5000):
    print("not eligible")
else:
    print("not eligible for the shopping")
