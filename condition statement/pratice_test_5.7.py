#accept the age , sex(m,f), number of days and display the wages accordingly 


age = int(input("enter your age : "))
sex = input("enter your  gender (M/F) are : ")
nd = int(input("number of of days : "))
if age >= 18 and age <= 30 and sex.upper() =="M":
    amt = nd*700
    print("total wages is : ", amt)
elif age >= 18 and age <= 30 and sex.upper()=="F":
    amt = nd*750
    print("total wages is : ", amt)
elif age >= 30 and age <= 40 and sex.upper()=="M":
    amt = nd*800
    print("total wages is : ", amt)
elif age >= 30 and age <= 40 and sex.upper()=="F":
    amt = nd*850
    print("total wages is :", amt)
else:
    print("enter approprite age ")    

