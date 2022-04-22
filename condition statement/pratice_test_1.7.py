#write a program to check whether the last digit of a number(entered by user)
# is divisible by 3 or not

num = int(input("enter number : "))
id = num % 10
if num % 3== 0:
    print("number is divisible by 3")

else:
    print("it is not divisible by 3")    