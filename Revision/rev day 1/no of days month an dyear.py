def agefind(currdate, currmonth, curryear, birthdate, birthmonth, birthyear):
    month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if(birthdate>currdate):
        currmonth=currmonth-1
        currdate=currdate+month[birthmonth-1]
    if(birthmonth>currmonth):
        curryear=curryear-1
        currmonth=currmonth+12
    calcdate=currdate-birthdate
    calcmonth=currmonth-birthmonth
    calcyear=curryear-birthyear
    print("Year(s): ", calcyear, "Month(s): ", calcmonth, "Day(s): ", calcdate)
    

currdate=int(input("Enter the current day: "))
currmonth=int(input("Enter the current month: "))
curryear=int(input("Enter the current year: "))
birthdate=int(input("Enter the birth day: "))
birthmonth=int(input("Enter the birth month: "))
birthyear=int(input("Enter the birth year: "))

calcyear=curryear-birthyear

if(curryear%4==0 and birthyear%4==0):
    print("Both join and birth dates are leap years")
elif(curryear%4==0):
    print("Only join date is a leap year")
elif(birthyear%4==0):
    print("Only birth date is a leap year")
else:
    print("Both join and birth dates are not leap years")

if(calcyear>19 and birthyear%4==0):
    print("I am a lucky adult and adult means responsibility")
else:
    print("I am aspiring to become a responsible adult")
agefind(currdate, currmonth, curryear, birthdate, birthmonth, birthyear)
