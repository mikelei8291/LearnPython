class carRecord():
    def __init__(self, vehicleID, registration, dateOfReg, engineSize, price):
        super(carRecord, self).__init__()
        self.vehicleID = vehicleID
        self.registration = registration
        self.dateOfReg = dateOfReg
        self.engineSize = engineSize
        self.price = price


ThisCar = carRecord()
ThisCar.engineSize = 2500

Car = [ThisCar for i in range(100)]
Car[1].engineSize = 2500
