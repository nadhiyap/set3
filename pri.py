l=int(input("enter l"))
r=int(input("enter r"))

for i in range(l,r+1):
    a=1
    for j in range(2,i):
        if(i%j==0):
            a=0
            break
    if(a==1):
        print(i)
           
