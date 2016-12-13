class Car():
    def __init__(self, n, e):
        super(Car, self).__init__()
        self.__vehicleID = n
        self.__reg = ""
        self.__date = None
        self.__size = e
        self.__price = 0.00

    def setPrice(self, p):
        self.__price = p

    def setReg(self, r):
        self.__reg = r

    def setDate(self, d):
        self.__date = d

    def getVehicleID(self):
        return self.__vehicleID

    def getReg(self):
        return self.__reg

    def getDate(self):
        return self.__date

    def getSize(self):
        return self.__size

    def getPrice(self):
        return self.__price

thisCar = Car("ABC1234", 2500)
thisCar.setPrice(12000)
print(thisCar.getVehicleID())
