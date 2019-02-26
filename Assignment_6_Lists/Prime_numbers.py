#Program to print n prime numbers , where n is taken from the user
def nextprime(num):
    while True :
        num+=1
        for i in range(2,num):
            if num %i==0:
                break
        else :
            return num
def Primeproducer(N):
    num=1
    count=1
    while count<= N :
        num=nextprime(num)
        yield num
        count+=1
N=int(input("numbers to print "))
l=[x for x in Primeproducer(N)]
print(l)
