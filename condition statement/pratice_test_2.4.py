#write a program to accept a number from 1 to 7 and display 
#the name of the day like 1 for sunday , 2 for monday and so on


num = int(input("Enter any number between 1 to 7: "))
if num==1:
    print("sunday")
elif num == 2:
    print("monday")
elif num == 3:
    print("tuesday")
elif num == 4:
    print("wednesday")
elif num == 5:
    print("thursday") 
elif num == 6:
    print("friday")
else:
    print("saturday")
                  
