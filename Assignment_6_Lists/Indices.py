#Program to print the indices of all the occurance of a given element in a given list
l=[]
a=int(input("How many Elements you want to enter in a list :"))
for x in range (1,a+1):
    b=input("Enter Element:")
    l.append(b)
print(l)
y=int(input("Enter the element you want to know the indices of :"))
print(l.index(y))
