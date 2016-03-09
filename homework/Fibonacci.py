from math import ceil

fibs = [0, 1]
numbers = int(input("How many Fibonacci numbers do you want? "))
for i in range(numbers-2):
    fibs.append(fibs[-2] + fibs[-1])
print (fibs)

n = int(input("How many Fibonacci numbers do you want? "))
a = ((5**0.5)-1)/2
b = ((5**0.5)+1)/2
c = (5**0.5)/5
for j in range(n):
    fibonacciValue = c*((b**j)-(a**j))
    #Python is stupid that it will calculate some
    #fibonacciValue to 1.000000000000002 so ceil
    #will convert it to 2, I just want to say "Fuck!"
    fibonacciNumber = int(ceil(fibonacciValue-0.1))
    print (fibonacciNumber, end=" ")
