#Program to Print sum of n odd Natural Numbers
x=1
sum=0
n=int (input("enter no."))
while x<=n:
 if x%2!=0 :
    print(x,end="\n")
 sum = sum +x
 x=x+2
print("sum of all the numbers  is :",sum)
