#Program to Print Product of n odd Natural Numbers
x=1
product=1
n=int (input("enter no."))
while x<=n:
 if x%2!=0 :
    print(x,end="\n")
 product = product*x
 x=x+2
print("Product of all the numbers  is :",product)
