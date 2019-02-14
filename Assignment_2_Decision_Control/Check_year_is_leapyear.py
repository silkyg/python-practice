#Program to check whether the year is a leap year or not
year=int(input("Enter a valid year :"))
if year%4==0 :
    print("%d is a Leap year"%year )
elif year % 400 == 0 and year % 100 != 0:
    print("%d is a Leap year" % year)
else :
    print("%d is a not a Leap year"%year )