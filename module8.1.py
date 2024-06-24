def add_everything_up(a, b):
    s = 0
    try:
        s = a + b
        if type(s) == float:
            s = float('{:.3f}'.format(s))
    except TypeError:
        a = str(a)
        b = str(b)
        s = a + b
    return s


print(add_everything_up(123.456, "строка"))
print(add_everything_up("яблоко", 4215))
print(add_everything_up("фрукт ", "яблоко"))
print(add_everything_up(123.456, 7))
print(add_everything_up(12, 23))
