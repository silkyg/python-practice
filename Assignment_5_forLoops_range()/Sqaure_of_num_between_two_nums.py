#Program to print te square of numbers between two numbers
a=int(input("Enter a number :"))
b=int(input("Enter second number :"))
for x in range (a,b+1):
    i=x*x
    print("square between %d and %d are :"%(a,b),i,end="\n")
