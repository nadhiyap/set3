n=int(input("enter total number"))
b=[]
for i in range(1,n+1):
    a=input("enter a number")
    b.append(a)
for i in range(1,n+1):
    print(max(b))
    b.remove(max(b))
