# 1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.


def isLeapyear(year):
        if (year % 4==0 and year % 100 !=0)or year % 400 == 0:
          return  True
        else:
          return False 

year  =int (input("enter the year"))

if isLeapyear(year):

  print("{} is a leap year.".format(year))
else:

  print("{} is not a leap year.".format(year))