#accept the marked price from the user and calculate the net amount
#as(marked price - discount) to pay according to following criteria

na = 0
d = 0

markp = int(input("enter your marked price :"))
if markp > 10000:
    d = 20/100*markp
if markp > 7000 and markp <= 10000:
    d = 15/100*markp
if markp <= 7000:
    d = 10/100*markp
na = markp - d
print("net amount to pay ", na)            
