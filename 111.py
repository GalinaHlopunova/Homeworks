from collections import defaultdict
from datetime import datetime
from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = str(name)
        self.power = int(power)
        self.catch = defaultdict(int)

    def run(self):
        self.catch = defaultdict(int)
        enemy = 100
        k = 0
        print(f"{self.name} на нас напали!")
        while enemy > 0:
            k += 1
            enemy -= self.power
            if enemy >= 0:
                sleep(1)
                print(f"{self.name} сражается {k} дней(дня)..., осталось {enemy} воинов.\n")
            else:
                print(f"{self.name} сражается {k} дней(дня)..., осталось 0 воинов.")
                sleep(1)
        print(f"{self.name} одержал победу спустя {k} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print("Все битвы закончились!")

import threading
from collections import defaultdict
from datetime import datetime
from time import sleep
from threading import Thread
from random import randint, random
from queue import Queue, Empty


class Table:
    guest = None

    def __init__(self, number):
        self.number = number


class Guest(Thread):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.catch = defaultdict(int)
        self.name = name

    def run(self):
        self.catch = defaultdict(int)
        t = randint(3, 10)
        sleep(t)


class Cafe:
    def __init__(self, queue, *args, **kwargs):
        self.tables = list(tables)
        self.queue = Queue()
        self.guests = list(guests)

    def guest_arrival(self, *guests):
        self.guests = list(guests)
        for guest_cafe in guests:
            if __name__ == '__main__':
                main = Guest(guest_cafe)
                main.start()
                for table_n in self.tables:
                    if Table.guest is None:
                        Table.guest = Guest.name
                        print(f"{guest_cafe} сел(-а) за стол номер {table_n}")
                    else:
                        self.queue.put(main)
                        print(f"{main} в очереди")


    def discuss_guests(self):
        for guest_cafe in guests:
            table_empty = True
            for table_n in self.tables:
                if Table.guest is not None:
                    table_empty = False
                if table_empty == False and guest_cafe.is_alive():
                    print(f"{Guest.name} покушал(-а) и ушел(ушла)")
                    print(f"Стол номер {table_n} свободен")
                    Table.guest = None
                if Queue.empty(guest_cafe) == False and Table.guest == None:
                    self.queue.get(guest_cafe)
                    Table.guest = Guest.name
                    print((f"{Guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table_n}"))
                    Guest(guest_cafe)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

while not self.queue.empty():
    self.queue.get(guest)
    table = self.find_free_table()
    if table:
        table.guest = guest
        print((f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}"))
        guest.start()

 table = self.leave_table()
            if table:
                table.guest = guest
                print((f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}"))
                guest.start()


def leave_table(self):
    for table in self.tables:
        if table.guest != None and guest.cafe == False:
            guest = table.guest
            print(f"{guest.name} покушал(-а) и ушел(ушла)")
            print(f"Стол номер {table.number} свободен")
            table.guest = None
            guest.join()