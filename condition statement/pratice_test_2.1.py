#write a program to accept percentage from the user and display 
#the grade according to the following criteria:
'''
marks = int(input("enter the your marks: "))

if marks > 90: 
    print("your grade is  : A ")

elif marks > 80 and marks <= 90:
    print("your marks are: B " )

elif marks >= 60 and marks <= 80:
    print("your grades are: C ")

else:
    print("your grade are: D ")   '''         

def grademarks(display):
    if grademarks > 90:
        return("your grade is A")
    elif grademarks > 80 and grademarks <= 90:
        return("your grade is B ")
    elif grademarks >= 60 and grademarks <= 80:
        return("your grade is C ")
    else:
        return("grade is D")

display = int(input("enter your marks : "))

grademarks(display)