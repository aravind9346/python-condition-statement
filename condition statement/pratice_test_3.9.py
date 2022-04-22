#write a program to whether a number (accepted from user) is 
#divisible by 2 and 3 both

num = int(input("enter your number : "))
if num % 2== 0 and num%3==0:
    print("number is divisible by both :", num)
elif num%2==0 or num%3==0:
    print("number is divisible by single numb : ", num)
else:
    print("it can not divisible by any number :", num)        