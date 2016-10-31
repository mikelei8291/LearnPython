car_reg = str(input("Car reg: "))
date = str(input("Date: "))
n_repair = int(input("Number of repairs: "))
f = open("CARSALES1.txt", "a")
f.write("%s\n%s\n%d\n" %(car_reg, date, n_repair))
f.close()

import os
print(os.path.isfile("CARSALES1.txt"))
f = open("CARSALES1.txt", "r")
print(f.read())
f.close()