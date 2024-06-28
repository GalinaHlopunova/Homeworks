class InvalidDataException(Exception):
    def __init__(self, message1, extra_info1):
        self.message1 = message1
        self.extra_info1 = extra_info1


class ProcessingException(Exception):
    def __init__(self, message2, extra_info2):
        self.message2 = message2
        self.extra_info2 = extra_info2


def year_birth(year1):
    if (year1 < 1900 or year1 > 2024):
        raise InvalidDataException ("Вы ввели некорректные дааные, год рождения не может быть равен", year1)
    return year1


def f_age(year2):
    age = 2024 - year2
    if age < 18:
        raise ProcessingException("Вам мало лет, всего", age)
    return age


def poem(year):
    year1 = year
    year2 = year
    try:
        year_birth(year1)
        f_age(year2)
        file = open('Blok.txt', "w+")
        file.write("Стихи о прекрасной даме.")
        file = open('Blok.txt', "r")
        f_poem = file.read()
        file.close()
        print(f_poem)
    except InvalidDataException as e:
        print(f"Сообщение об ощибке:  {e.message1} {e.extra_info1}.")
    except ProcessingException as e:
        print(f"Сообщение об ощибке:  {e.message2} {e.extra_info2}.")
    finally:
        print("Чтение завершено!")
    return


poem(int(input("Введите Ваш год рождения: ")))
