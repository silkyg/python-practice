#Program to check the roots of a quadratic equation
a=int(input("Enter first number :"))
b=int (input("Enter second number :"))
c=int(input("Enter third number :"))
discriminant=b*b-4*a*c
print("equation={}x^2+{}x+{}=0".format(a,b,c))

if discriminant>0 :
    print("Roots are unequal and Real ")
elif discriminant==0 :
    print("Roots are equal and Real ")
else :
    print("Roots are Unequal and Imaginary ")