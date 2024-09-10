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
        k1 = round(enemy/self.power, 0)
        k = int(k1 + 1)
        print(f"{self.name} на нас напали!")
        for i in range(1, k):
            enemy -= self.power
            if enemy >= 0:
                sleep(1)
                print(f"{self.name} сражается {i} дней(дня)..., осталось {enemy} воинов.\n")
            else:
                print(f"{self.name} сражается {i} дней(дня)..., осталось 0 воинов.")
                sleep(1)
        print(f"{self.name} одержал победу спустя {k-1} дней(дня)!\n")


first_knight = Knight('Sir Lancelot', 15)
second_knight = Knight('Sir Galahad', 3)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
