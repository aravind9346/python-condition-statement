#accept the percentage from user and display the grade according the 
#following criteria

#    belwo 25 -- D
#    25 to 45 --- C

#    45 to 50 —- B
#    50 to 60 –– B+
#    60 to 80 — A
#    Above 80 –- A+

per = int(input("enter your perscentage :"))
if per > 80:
    print("your grade is : A+ ")
elif per > 60 and per < 80:
    print("yours grade is : A")
elif per > 50 and per < 60:
    print("your grade is : B+")
elif per > 45 and per < 50:
    print("your grade is : B")
elif per > 25 and per< 45:
    print("your grade is : C ")
elif per < 25:
    print("your grade is : D")                    
