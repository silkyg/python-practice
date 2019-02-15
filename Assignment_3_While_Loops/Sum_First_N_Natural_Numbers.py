#Program to Print sum of n Natural Numbers
x=1
sum=0
n=int (input("enter no."))
while x<=n:
 print(x,end="\n")
 sum = sum + x
 x=x+1
print("sum of all the numbers  is :",sum)