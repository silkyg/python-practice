a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
def print_factors(a,b):
   print("The factors of",a,"are:")
   for i in range(1, a + 1):
       if a % i == 0:
           print(i)
   print("The factors of", b, "are:")
   for i in range(1, b + 1):
       if b % i == 0:
           print(i)
print_factors(a,b)
def common(i):
    if i==1:
     print("coprime")
