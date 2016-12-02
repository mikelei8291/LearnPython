import pickle


class carRecord():
    def __init__(self):
        super(carRecord, self).__init__()
        self.vehicleID = ""
        self.registration = ""
        self.dateOfReg = None
        self.engineSize = 0
        self.price = 0.00


recordNum = int(input("Input record number: ")) + 1

thisCar = carRecord()
car = [thisCar for i in range(recordNum)]
for i in range(recordNum):
    car.append(input("Input record:"))

# Write
carFile = open("cars.dat", "wb")
for i in range(recordNum):
    pickle.dump(car[i], carFile)
carFile.close()

# Read
carFile = open("cars.dat", "rb")
car = []
while True:
    car.append(pickle.load(carFile))
carFile.close()
print(car)
