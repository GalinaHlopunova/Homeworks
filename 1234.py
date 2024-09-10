import threading
from collections import defaultdict
from datetime import datetime
from time import sleep
from threading import Thread
from random import randint, random
from queue import Queue, Empty


class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name, cafe, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.cafe = cafe

    def run(self):
        t = randint(3, 10)
        sleep(t)


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            self.queue.put(guest)
            guest.start()
            self.discuss_guests()
        for guest in guests:
            guest.join()

    def discuss_guests(self):
        while not self.queue.empty():
            self.queue.get(guest)
            table = self.find_free_table()
            if table is None:
                table.guest = guest
                print(f"{guest.name} сел(-а) за стол номер {table.number}")
            else:
                print(f"{guest.name} в очереди")
                self.queue.put(guest)
                sleep(1)

    def find_free_table(self):
        for table in self.tables:
            if table.guest is None:
                return table
            return None

    def leave_table(self, guest):
        for table in self.tables:
            if table.guest == guest:
                print(f"{guest.name} покушал(-а) и ушел(ушла)")
                print(f"Стол номер {table.number} свободен")
                table.guest = None
                self.discuss_guests()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name, cafe=None) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
for guest in guests:
    guest.cafe = cafe
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
# print((f"{Guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table_n}"))
while not self.queue.empty():
    self.queue.get(guest)
    table = self.find_free_table()
    if table:
        table.guest = guest
        print((f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}"))
        guest.start()
    else:
        for guest in self.guests:
            if self.leave_table() is None:
                print(f"{guest.name} покушал(-а) и ушел(ушла)")
                print(f"Стол номер {table.number} свободен")
                table.guest = None
                guest.join()