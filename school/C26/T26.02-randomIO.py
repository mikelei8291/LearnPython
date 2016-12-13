import pickle, random

class carRecord():
    def __init__(self):
        super(carRecord, self).__init__()
        self.vehicleID = ""
        self.registration = ""
        self.dateOfReg = None
        self.engineSize = 0
        self.price = 0.00

def shash(data, f):
    seed = 0
    for i in data:
        seed += ord(i)
    f.seek(0, 2)
    origin = f.tell()
    return origin + random.randint(0, seed)

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
        address = shash(car.vehicleID, f)
        print(address)
        f.seek(address)
        try:
            pickle.dump(car[i], f)
        finally:
            f.close()

# Read
def carRead(carfile):
    f = open(carfile, "rb")
    vehicleID = input("Input vehicle ID: ")
    address = shash(vehicleID, f)
    f.seek(address)
    try:
        return pickle.load(f)
    finally:
        f.close()

try:
    carWrite("cars.dat")
    carRead("cars.dat")
except:
    Error = True
