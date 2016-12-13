import pickle

class carRecord():
    def __init__(self):
        super(carRecord, self).__init__()
        self.vehicleID = ""
        self.registration = ""
        self.dateOfReg = None
        self.engineSize = 0
        self.price = 0.00

# Write
def carWrite(carfile):
    try:
        f = open(carfile, "rb+")
    except:
        f = open(carfile, "wb+")
    thisCar = carRecord()
    recordNum = int(input("Input record number: "))
    car = [thisCar for i in range(recordNum)]
    for i in range(recordNum):
        car.append(input("Input record: "))
        try:
            pickle.dump(car[i], f)
        finally:
            f.close()

# Read
def carRead(carfile):
    f = open(carfile, "rb")
    car = []
    try:
        return car.append(pickle.load(f))
    finally:
        f.close()

try:
    carWrite("cars.dat")
    carRead("cars.dat")
except:
    Error = True
