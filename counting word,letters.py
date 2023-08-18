n=str(input("enter the sentence"))
print(n)
w,d,u,l=0,0,0,0
l_w=n.split()
w=len(l_w)
for i in n:
    if(i.isdigit()):
       d=d+1
    elif(i.isupper()):
        u=u+1
    elif(i.islower()):
        l=l+1
print("number of digit is:",d)
print("number of lowercase is:",l)
print("number of uppercase is:",u)
