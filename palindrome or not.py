n=int(input("enter the value of number:"))
num=n
num1=str(n)
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if(num==rev):
    print("number is palindrome")
else:
    print("not a palindrome")
def palcount(n1):
    while(n1>0):
        digit=n1%10
        print(digit,"no of occurence is",num1.count(str(digit)))
        n1=n//10
palcount(num)
        
    
