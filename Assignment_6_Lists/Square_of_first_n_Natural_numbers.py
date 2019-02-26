#Program to create  list of Square of first N natural numbers ,and fill the list of elements
l=[]
a=int(input("How may numbers want to enter:"))
for x in range (1,a+1):
    m=int(input("Enter numbers:"))
    square = m * m
    l.append(square)
print(l)

