a=eval(input("a= "))
b=eval(input("b= "))
c=eval(input("c= "))
d=b**2-4*a*c
if d<0:
    print("There is no real root.")
elif d==0:
    x=y=0.5*(-b)
    print("There is only one root x= ",x)
else:
    x=0.5*(-b+(d**0.5))
    y=0.5*(-b-(d**0.5))
    print("The roots of the function is x1=",x,"x2=",y)
