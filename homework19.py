class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def __init__(self, qty):
        self.qty = qty

    def horse_powers(self, qty):
        return self.qty


class Nissan(Car, Vehicle):
    price = 1190000
    vehicle_type = "Juke"

    def __init__(self, qty, name):
        self.name = str(name)
        super().__init__(qty)


Nissan_Juke = Nissan(117, "Nissan Juke")
print (f"Модель: {Nissan_Juke.vehicle_type}")
print(f"Стоимость {Nissan_Juke.name}: {Nissan_Juke.price}")
print(f"Количество лошадиных сил {Nissan_Juke.name}: {Nissan_Juke.horse_powers(117)}")
