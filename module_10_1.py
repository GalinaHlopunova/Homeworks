from datetime import datetime
from time import sleep
from threading import Thread


def wite_words(word_count, file_name):
    k = int(word_count)
    name_ = str(file_name)
    with open(name_, 'w') as file:
        file.write('')
    for i in range(0, k):
        with open(name_, 'a') as file:
            file.write(f"Какое-то слово № {i + 1}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {name_}")
    #with open(name_, 'r') as file:
       # print(file.read())
    return file


start_time = datetime.now()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

end_time = datetime.now()
execution_time = end_time - start_time
print(f"Работа функций: {execution_time}")

start_time = datetime.now()

t1 = Thread(target=wite_words, args=(10, 'example5.txt'))
t2 = Thread(target=wite_words, args=(30, 'example6.txt'))
t3 = Thread(target=wite_words, args=(200, 'example7.txt'))
t4 = Thread(target=wite_words, args=(100, 'example8.txt'))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

end_time = datetime.now()
execution_time = end_time - start_time
print(f"Работа потоков: {execution_time}")
