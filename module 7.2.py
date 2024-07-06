import io

def custom_write(file_name, strings):
    strings_positions = dict()
    N = 0
    b = 0
    bs = 0
    l = len(strings)
    for i in range(0, l):
        item = strings[i]
        file = open(file_name, mode='w+', encoding='utf8')
        file.writelines(f"{item}\n")
        bs = file.tell()
        N += 1
        key = (N, b)
        value = item
        strings_positions[key] = value
        b += bs
        file.close()
    return strings_positions

strings = [
    "Text for tell.",
    "Используйте кодировку utf-8.",
    "Because there are 2 languages!",
    "Спасибо!"
    ]
result = custom_write('test.txt', strings)
print (result)
for elem in result.items():
    print(elem)
