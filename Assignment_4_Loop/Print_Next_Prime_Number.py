#Program to print the next prime number of a given number
n=int(input("Enter a number :"))
for x in range (2,n):
        if x%n==0 :
         n+=1
         break
else:
    print(x,"Bawa  prime number ")
