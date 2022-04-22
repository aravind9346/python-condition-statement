#write a program to display "hello" if a number entered by 
#user is a multile of five ,
#otherwise print"bye"

num = int(input("enter your number or word : "))
if num % 5 == 0:
    print("HELLO")

else:
    print("BYE")    