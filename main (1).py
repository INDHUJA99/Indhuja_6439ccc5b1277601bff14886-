# 1.1 IMPLEMENT A RECURSIVE FUNCTION TO CALCULATE THE FACTORIAL OF A GIVEN NU


def fact_rec(n):
     if n==0 or n==1:
       return 1 
     else:
       return n*fact_rec(n-1)

number =5
res = fact_rec(number)

print("The factorial of {} is {}.".format (number, res))