s1=input("enter string1")
s2=input("enter string2")
count=0
for i in range(0,len(s1)):
    if(s1[i]!=s2[i]):
        count+=1
if(count==1):
    print("yes")
else:
    print("no")

           
