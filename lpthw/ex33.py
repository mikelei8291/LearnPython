def makeList(num, inc):
    i = 0
    numbers = []
    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += inc
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    print("The numbers: ")
    for num in numbers:
        print(num)


def makeForList(num, inc):
    numbers = []
    for i in range(0, num, inc):
        print(f"i is {i}")
        numbers.append(i)
        print(f"Numbers now: {numbers}")
    print("The numbers:")
    for num in numbers:
        print(num)


makeList(6, 1)
print("Make list with for loop:")
makeForList(6, 1)
