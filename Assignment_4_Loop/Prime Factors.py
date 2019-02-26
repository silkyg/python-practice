#Program to print prime factrs of all the numbers
a=int(input("Enter first number :"))
def print_factors(a):
   for i in range(1, a + 1):
       if a % i == 0:
           print(i)
   print("The factors of", a, "are:")
print_factors(a)