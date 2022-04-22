

per = int(input("enter your percentage : "))
if per >= 65:
    print("excellent")
elif per >= 55 and per < 65:
    print("GOOD")
elif per >= 40 and per < 55:
    print("FAIR")
elif per < 40:
    print("FAILED")            