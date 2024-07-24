class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = str(owner)
        self.__model = str(model)
        self.__color = str(color)
        self.__engine_power = int(engine_power)

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def print_info(self):
        model_ = self.get_model()
        print(f"Модель: {model_}")
        power_ = self.get_horsepower()
        print(f"Мощность двигателя: {power_}")
        color_ = self.get_color()
        print(f"Цвет: {color_}")
        owner_ = self.owner
        print(f"Владелец: {owner_}")


    def set_color(self, new_color):
        new_color_ = str(new_color).lower()
        if new_color_ in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")
        return self.__color


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
vehicle1.set_color('black')
vehicle1.print_info()
