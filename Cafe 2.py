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
        self.catch = defaultdict(int)

    def run(self):
        t = randint(3, 10)
        sleep(t)


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()
        self.guests = guests

    def guest_arrival(self, *guests):
        for guest in guests:
            table = self.find_free_table()
            if table:
                table.guest = guest
                guest.cafe = True
                print(f"{guest.name} сел(-а) за стол номер {table.number}")
                guest.start()
                sleep(1)
            else:
                print(f"{guest.name} в очереди")
                self.queue.put(guest)
                sleep(1)

    def discuss_guests(self, *guests):
        global guest_
        guest = None
        while not self.queue.empty():
            for table in self.tables:
                guest = table.guest
                guest.join()
                if table.guest != None and guest.is_alive() == False:
                    guest = table.guest
                    print(f"{guest.name} покушал(-а) и ушел(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    sleep(1)
                    table.guest = None
                    guest = self.queue.get(guest)
                    table.guest = guest
                    print((f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}"))
                    guest.start()
                    if self.queue.empty() == True:
                        guest_ = guest
                        break
                        self.closing_cafe()
    def closing_cafe(self):
        guest = guest_
        guest.join()
        sleep(3)
        for table in self.tables:
            if table.guest != None:
                guest = table.guest
                print(f"{guest.name} покушал(-а) и ушел(ушла)")
                print(f"Стол номер {table.number} свободен")
                table.guest = None
                sleep(1)
        print("Кафе закрылось!")

    def find_free_table(self):
        for table in self.tables:
            if table.guest is None:
                return table
                break


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
#Проверка последних столов.
cafe.closing_cafe()
