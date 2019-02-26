#Program to check the number is prime or not

n=int(input("Enter number :"))
if n<2:
    print("%d is not a prime number "%n)
for i in range(2,n-1) :
  if n%i==0:
   print("%d is not a prime number "%n)
   break
else :
     print("%d is a prime number "%n)