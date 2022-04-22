#accept the following from the user and calculate the percentage
#of class attended:
# a : total number of orkeer days
#percentage is less than 75

wokd = int(input("enter total number of working days : "))
abdays = int(input("enter number of days absent: "))
per = (wokd - abdays)/wokd * 100
print("your attendence is :", per)
if per < 75:
    print("your are not eligible for exams ")

else:
    print("your are eligible for writing exam ")