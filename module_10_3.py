import threading
from collections import defaultdict
from datetime import datetime
from time import sleep
from threading import Thread
from random import randint, random


class Bank(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.catch = defaultdict(int)
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, lock=None):
        global k
        k = 0
        for i in range(100):
            k += 1
            n1 = randint(50, 500)
            self.balance += n1
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'{i + 1}. Пополнение: {n1}. Баланс: {self.balance}')
        sleep(0.001)

    def take(self, lock=None):
        for j in range(100):
            n2 = randint(50, 500)
            print(f"{j + 1}. Запрос на {n2}")
            if n2 <= self.balance:
                self.balance -= n2
                print(f"Снятие: {n2}. Баланс: {self.balance}")
            else:
                print("Запрос отклонен, недостаточно средств")
                self.lock.acquire()
            if k == 100 and self.lock.locked():
                self.lock.release()
                break


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")
