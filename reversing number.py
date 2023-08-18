def reverse(n):
    while(n!=0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
num=int(input("enter the number"))
print(reverse(num))
