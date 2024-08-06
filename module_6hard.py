import math
from math import pi


class Figure:
    sides_count = 0
    sides1 = []

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = list(sides)
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_(self):
        if self.r in range(0, 256) and self.g in range(0, 256) and self.b in range(0, 256):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        cor_ = self.__is_valid_()
        if cor_ == True:
            self.__color[0] = self.r
            self.__color[1] = self.g
            self.__color[2] = self.b
        return self.__color

    def __is_valid_sides(self):
        k = len(self.new_sides)
        for j in range(0, k):
            if self.new_sides[j] > 0 and k == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        if len(self.__sides) != self.sides_count:
            self.__sides = self.sides1
        return self.__sides

    def __len__(self):
        P = sum(self.__sides)
        return int(P)

    def set_sides(self, *new_sides):
        self.new_sides = list(new_sides)
        val_ = self.__is_valid_sides()
        if val_ == True:
            self.__sides = self.new_sides
        return self.__sides


class Circle(Figure):
    sides_count = 1
    sides1 = [1]
    __radius = 0.0

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        super().__len__()

    def radius_(self):
        L = self.__len__()
        self.__radius = L / (2 * pi)
        return self.__radius

    def get_square(self):
        S = pi * self.radius_() ** 2
        S_Circle = round(S, 2)
        return S_Circle


class Triangle(Figure):
    sides_count = 3
    sides1 = [1, 1, 1]
    a = 0
    b = 0
    c = 0
    __height = 0.0
    sides_ = []

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        super().__len__()

    def height_(self):
        self.sides_ = self.get_sides()
        self.a = self.sides_[0]
        self.b = self.sides_[1]
        self.c = self.sides_[2]
        p = self.__len__() / 2
        __height = 2 / self.a * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return __height

    def get_square(self):
        self.sides_ = self.get_sides()
        self.a = self.sides_[0]
        S_ = 0.5 * self.a * self.height_()
        S_Triangle = round(S_, 2)
        return S_Triangle


class Cube(Figure):
    sides_count = 12
    sides1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    sides2 = []

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = list(sides)
        super().__len__()
        super().set_sides()
        super().get_sides()

    def get_sides(self):
        if len(self.__sides) == 1:
            k1 = self.__sides[0]
            self.__sides = [k1] * 12
        else:
            self.__sides = self.sides1
        return self.__sides

    def __is_valid_sides(self):
        k = len(self.new_sides)
        for j in range(0, k):
            if self.new_sides[j] > 0 and k == 1:
                return True
            else:
                return False

    def set_sides(self, *new_sides):
        self.new_sides = list(new_sides)
        val_ = self.__is_valid_sides()
        if val_ == True:
            self.__sides = self.new_sides
        return self.__sides

    def __len__(self):
        a = self.__sides[0]
        P = 12 * a
        return P

    def get_volume(self):
        a = self.__sides[0]
        V_Cube = a ** 3
        return V_Cube


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((255, 25, 36), 4, 3, 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
# Дополнительная проверка:
print(circle1.get_square())
print(triangle1.get_sides())
print(triangle1.get_color())
triangle1.set_sides(15)  # Не изменится
print(triangle1.get_sides())
triangle1.set_color(30, 250, 15)  # Изменится
print(triangle1.get_color())
print(triangle1.get_square())
print(triangle1.height_())
print(len(cube1))
print(len(triangle1))
cube1.set_sides(3, 6, 6, 6, 7, 8, 9, 7, 1, 2, 6, 2)  # Не изменяется
print(cube1.get_sides())
cube1.set_sides(3, 6, 6, 6, 7, 8, 9, 7, 1, 2, 6)  # Не изменяется
print(cube1.get_sides())
cube1.set_sides(25)  # Изменяется
print(cube1.get_sides())
