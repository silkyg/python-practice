#Program to find the greatest number in a list given by a user
l=[]
n=int(input("Enter number of elements :"))
for i in range (1,n+1):
    b=int(input("Enter number :"))
    l.append(b)
l.sort()
print("Largest in list is :",l[n-1])