weight=input("Please enter your weight:")
unit=input("which unit? (K)g or (L)bs")
if unit is "K" or "k":
    convert=float(weight)//0.45359237
    print(convert, "lbs")
elif unit is "L" or "l":
    convert=float(weight)* 0.45359237
    print(convert, "kg")