#Program to print Armstrong Numbers

while True :
        for n in range(1, 1001):
            s = 0
            n += 1

            r=n%10
            s=s+r*r*r
            n=n/10

if s==n :
 print("armstron no. are "%n)


