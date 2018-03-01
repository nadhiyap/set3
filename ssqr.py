import math
a=int(input("enter a number"))
c=0
while(a!=0):
    b=a%10
    c=c+b**2
    a=a//10
print(c)
