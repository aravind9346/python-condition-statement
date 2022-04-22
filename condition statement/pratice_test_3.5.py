#write a program to find the lowest number out of two numbers excepted from user

n1 = int(input("enter your first number : "))
n2 = int(input("enter your second number : "))

if n1 > n2:
    print("n1 is greater than n2")
    print("smaller number is : ", n2)
else:
    print("n2 is greater than n1")
    print("smaller number is : ", n1)    