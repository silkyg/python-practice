# Progrm to check which no. is greatest of three entered numbers
x=int(input ("Enter first number :"))
y=int(input ("Enter second number :"))
z=int(input ("Enter third number :"))
if x>y>z:
    print("%d is greatest of all"%x)
elif y>x>z:
    print("%d is greatest of all" %y)
else :
    print("%d is greatest of all" % z)