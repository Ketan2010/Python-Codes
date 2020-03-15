#condition:
#A leap year is exactly divisible by 4 except for century years (years ending with 00).
#The century year is a leap year only if it is perfectly divisible by 400.
#For example,
#1999 is not a leap year
#2000 is a leap year
#2004 is a leap year
def is_leap(year):
    leap = False
    if (year % 4 == 0) :
        #check for century year
        if (year % 100 == 0) :
            #century year is leap only if it is divisible by 4
            if (year % 400 == 0):
                leap=True
            else:
                leap=False
        else:
            leap=True
    else:
        leap=False
    return leap

year = int(input(enter year to be check:))
print is_leap(year)