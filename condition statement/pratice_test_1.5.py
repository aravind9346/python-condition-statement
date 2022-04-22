#write a program to calculate the electricity bill(accept number of unit from user)



#100 unit --  no charge
# 100 unit -- 5 rs per unit
#200 unit -- 10 rs per unit
#(for example if input unit is 350 than total bill amount is rs 2000)
amt = 0
num = int(input("enter electric unit from user : "))
if num <= 100:
    amt = 0
if num > 100 and num <=100:
    amt = (num -100)*5
if num > 200:
    amt = 500 +(num - 200)*10
print("amount to pay : ", amt)            