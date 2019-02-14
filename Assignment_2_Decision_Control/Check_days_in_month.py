# Program to take  month values in numeric format and displays the number of days in it.
month=int(input("Enter Month number (1-12):"))
if month in [1,3,5,7,8,10,12]:
    print("%dth month contains 31 days in it "%month)
elif month in [4,6,9,11]:
    print("%dth month contains 30 days in it " % month)
else :
    print("%nd month contains 28 0r 29  days in it " % month)