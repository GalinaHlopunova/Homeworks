class Car:
    price = 1000000
    def __init__(self, qty):
        self.qty = qty

    def horse_powers(self, qty):
        return self.qty


class Nissan(Car):
    price = 1190000
    def __init__ (self, qty, name):
        self.name = str(name)
        super().__init__(qty)

class Kia(Car):
    price = 2000000
    def __init__ (self, qty, name):
        self.name = str(name)
        super().__init__(qty)

Nissan_Juke = Nissan(117, "Nissan Juke")
Kia_Rio = Kia (123,"Kia Rio")
print(f"Стоимость {Nissan_Juke.name}: {Nissan_Juke.price}")
print(f"Стоимость {Kia_Rio.name}: {Kia_Rio.price}")
#h = Car(100)
#print(h.price)
#print(h.horse_powers(100))
print(f"Количество лошадиных сил {Nissan_Juke.name}: {Nissan_Juke.horse_powers(117)}")
print(f"Количество лошадиных сил {Kia_Rio.name}: {Kia_Rio.horse_powers(123)}")
