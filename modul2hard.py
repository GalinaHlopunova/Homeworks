password = ""
n = int(input("Введите число от 3 до 20: "))
if n >= 3 and n <= 20:
    i, j = 1, 2
    while i < n:
        while j < n:
            if i!= n and j != n and n%(i+j) == 0:
                password += str(i) + str(j)
                j = j + 1
            else:
                j = j + 1
        else:
          i = i + 1
          j = i + 1
    print(f"Пароль для числа {n}: {password}")
else:
    print("Для данного числа пароля нет!")
