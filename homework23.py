import os
import time

path = "C:\Windows\Help"
path_normalized = os.path.normpath(path)
for root, dirs, files in os.walk(path_normalized):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y.%H.%M", time.localtime(filetime))
        parent_dir = os.path.dirname(filepath)
        filesize = os.path.getsize(filepath)
        print(f"Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, "
              f"Родительская директория: {parent_dir}")
