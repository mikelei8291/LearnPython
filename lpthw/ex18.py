def printTwo(*args):
    arg1, arg2 = args
    print(f"Last Name: {arg1}, First Name: {arg2}")


def printTwo2(arg1, arg2):
    print(f"Last Name: {arg1}, First Name: {arg2}")


def printOne(arg1):
    print(f"Who are they? {arg1}")


def printNone():
    print("All done!")


printTwo("Kafuu", "Chino")
printTwo2("Yuuki", "Asuna")
printOne("They are my waifus!")
printNone()
