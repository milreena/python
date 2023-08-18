def swap(x,y):
    x,y=y,x
    return (x,y)
num1=int(input("enter num1 value"))
num2=int(input("enter num2 value"))
num1,num2=swap(num1,num2)
print("after swappping",num1,num2)
