#Program to accept marks of five subjects from user ("assuming marks out of 100 and display the student's result as PASS or FAIL,
#if the student is PASS then also display his percentage and division .
English=int(input("Enter marks in English subject out of 100 : "))
Hindi=int(input("Enter marks in Hindi subject out of 100 : "))
Social=int(input("Enter marks in Social subject out of 100 : "))
Maths=int(input("Enter marks in Maths subject out of 100 : "))
Science=int(input("Enter marks in Science subject out of 100 : "))
Total_Marks=English+Hindi+Social+Maths+Science
print("Total_Marks=",Total_Marks)

if Total_Marks>=165 :
    print("Result is PASS")
    Percentage = Total_Marks / 500 * 100
    print("Percentage=",Percentage,end="%",sep=(" "))
    if Percentage>=33 and Percentage<=50 :
       print("You passed with third division")
    elif Percentage>=50 and Percentage<=70 :
       print("You passed with second division")
    else:
      print("You passed with first division")
else:
    print("Result is FAIL")