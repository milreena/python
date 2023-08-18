def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 

s=str(input("enter string")) 
print("The original string is : ")
print(s)
 
print("The reversed string is : ")
print(reverse(s))
