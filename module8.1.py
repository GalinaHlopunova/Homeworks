def add_everything_up(a, b):
    try:
        s = a + b
        if type(s) == float:
            s = float('{:.3f}'.format(s))
        print(s)
    except TypeError:
        a = str(a)
        b = str(b)
        s = a + b
        print(s)



add_everything_up(123.456, "строка")
add_everything_up("яблоко", 4215)
add_everything_up("фрукт ", "яблоко")
add_everything_up(123.456, 7)
add_everything_up(12, 23)
