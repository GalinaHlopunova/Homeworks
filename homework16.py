class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


Buil1 = Building(15, "Жилой")
Buil2 = Building(15, "Жилой")
Buil3 = Building(24, "Жилой")
Buil4 = Building(15, "Производственный")
print(Buil1 == Buil2)
print(Buil1 == Buil3)
print(Buil2 == Buil4)
