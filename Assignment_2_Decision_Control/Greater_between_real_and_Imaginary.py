#Program to accept one complex number from user,and display the greater between real an Imaginary part

R=float(input("Enter a value :"))
I=float(input("Enter an Imaginary Value :"))
print("Complex_Number ={}+{}j".format(R,I))
if R>I:
    print("%d is the real part and is Greater "%R)
else:
    print("%d is the Imaginary part and is Greater " % I)