#program to print even numbers in reverse order using for loop
n=int(input('Enter a number :'))
s=range(2*n,0,-2)
for x in s:
    print("even numbers in reverse are",x)