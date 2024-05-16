data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
total = 0


def sum_values(param):
    global total
    if isinstance(param, int):
        total += param
    elif isinstance(param, str):
        total += len(param)
    elif isinstance(param, dict):
        for key, value in param.items():
            sum_values(key)
            sum_values(value)
    elif isinstance(param, (list, tuple, set)):
        for i in param:
            sum_values(i)


for i in data_structure:
    sum_values(i)
print(total)
