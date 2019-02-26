#Program to print table
n=int(input("Enter a number :"))
def num(n):
    for i in range (1,11):
        mul=n*i
        print("%d*%d ="%(n,i),mul)
    i=i+1
num(n)
