def sumf(n):
    sum = 0
    for i in range (1,n+1):
        sum += sum + (1/(i*i))
    return sum

def function(a,b,n,f):
    sum = 0
    h = (b-a)/n
    for i in range (1,n+1):
        sum += f(a+i*h)*h
    return sum
