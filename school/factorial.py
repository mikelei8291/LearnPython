from scipy.special import factorial

num = int(input("Input a number: "))
facnum = factorial(num, exact=False)
print(facnum)
