

#write a program to check whether a number is prime or not

k = 0
num = int(input(""))
if num == 0 or num == 1:
    k = 1
for i in range(2,num):
    if num%i == 0:
        k = 1
if k==1:
    print("not prime")
else:
    print("prime")                
