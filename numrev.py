a=int(input("enter the number"))
c=0
while(a!=0):
    b=a%10
    c=int(str(c)+str(b))
    a=a//10
print(c)
