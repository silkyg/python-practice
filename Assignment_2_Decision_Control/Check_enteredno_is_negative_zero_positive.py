#Program to check whether the entered number is Zero , Positive or Negative
x=float(input("Enter Number :"))
if x>0:
    print("%d is a Positive number "%x)
elif x<0 :
    print("%d is a Negative number " % x)
else :
    print("%d is a ZERO " % x)