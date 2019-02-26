#program to print odd numbers in reverse order using for loop
n=int(input('Enter a number :'))
s=range(2*n-1,0,-2)
for x in s:
    print("Odd numbes in reverse order are:",x)