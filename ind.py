n=int(input("enter a num"))
k=int(input("enter a num"))
l=[]
for i in range(n):
    a=int(input("enter val"+str(i+1)))
    l.append(a)
print(l.index(k))
