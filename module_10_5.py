import threading
from collections import defaultdict
from datetime import datetime
from time import sleep
from threading import Thread
from random import randint, random
from multiprocessing import Process, Pipe, Queue, Pool


def read_info(name):
    all_data = []
    file1 = open(name, "r")
    while True:
        line = file1.readline()
        all_data.append(line)
        if not line:
            break
    file1.close()



# with  Pool map read_info

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    start_time = datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time = datetime.now()
    execution_time = end_time - start_time
    print(f"{execution_time} (линейный)")



    start_time = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time = datetime.now()
    execution_time = end_time - start_time
    print(f"{execution_time} (многопроцессорный)")



