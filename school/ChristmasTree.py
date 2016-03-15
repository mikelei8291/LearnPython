a = int(input("How big tree do you want? "))
for b in range(1,a+1,1):
    print(" " * (a-b)+"/" * b+"\\" * b)
print(" " * (a-2), "||")
