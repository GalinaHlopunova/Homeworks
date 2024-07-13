import random
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, mode='w+', encoding='utf8')
        file.writelines(f"{item}\n" for item in data_set)
        file = open(file_name, mode='r', encoding='utf8')
        d = file.read()
        file.close()
        return d

    return write_everything


print(result)
write = get_advanced_writer('example.txt')
print(write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке']))


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        word_ = random.choice(self.words)
        return word_


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
