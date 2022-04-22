#wroite a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :

'''
cost = int(input("enter your bike price: "))    
if cost > 100000:
    print("yours tax rate : 15% ")
if cost > 50000 and cost <= 100000:
    print("your tax rate : 10% ") 

if cost <= 50000:
    print("your tax rate : 5% ")     
    '''

tax = 0
pr = int(input("enter the price of bike : "))
if pr > 100000:
    tax = 15/100*pr
elif pr > 50000 and pr <= 100000:
    tax = 10/100*pr
else:
    tax = 5/100*pr
print("tax to be paid ", tax)                   