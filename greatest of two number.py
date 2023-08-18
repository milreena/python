m1=int(input("Enter the marks of first subject"));
m2=int(input("Enter the marks of first subject"));
m3=int(input("Enter the marks of first subject"));

if(m1<m2 and m2<m3):
    avg=float(m3+m2)/2;
elif(m2<m1 and m2<m3):
    avg=float(m3+m1)/2
elif(m3<m1 and m3<m2):
    avg=float(m1+m2)/2;

print("Average of two marks is {0}".format(avg));
