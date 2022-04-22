# Write a program to check whether an years is leap year or not

yr = int(input("enter the year: "))
if yr % 100 == 0:
    if yr % 400 == 0:
        print("entered year is leap year")
    else:
        print("entered year is not a leap year")
else:
    if yr % 4 == 0:
        print("entered year is leap year")
    else:
        print("entered yewr is not a leap year")                