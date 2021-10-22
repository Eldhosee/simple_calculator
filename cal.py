def cal(x,y):
    if s=="+":
        z=x+y
        return z
    elif s=="-":
        z=x-y
        return z
    elif s=="/":
        z=x/y
        return z
    elif s=="*":
        z=x*y
        return z
    elif s=="%":
        z=x%y
        return z    
    else:
        print("please the operator")
print("enter the 2 vales: ")
x=float(input())
y=float(input())
print("enter the operator: ")
s=str(input()) 
q=cal(x,y)
print("The answer is: ",q)
