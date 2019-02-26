#Program to print table of 5
def num(n):
    for i in range (1,11):
        mul=n*i
        print("%d*%d:"%(n,i),mul)
    i=i+1
num(5)
