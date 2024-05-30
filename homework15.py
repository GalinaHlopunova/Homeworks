class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)
        print(f"В данном доме {self.numberOfFloors} этажей")



House1 = House()
House1.setNewNumberOfFloors(9)
