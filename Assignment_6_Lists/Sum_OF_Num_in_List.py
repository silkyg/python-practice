#Program to add the numbers in the list
import math as s
l=[]
sum=0
a=int(input("How may numbers want to enter:"))
for x in range (1,a+1):
    m=int(input("Enter numbers:"))
    l.append(m)
    sum=sum+m
print("Sum of all the numbers is :",sum)


