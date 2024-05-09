def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(a = 1)
print_params(b = 'строка', c = True)
print_params(a = 1, b = 'строка', c = True)
print_params(b=25)
print_params(c = [1,2,3])
values_list = [3, 'class', True]
values_dict = {"a":"17", "b":"webinar", "c":"False"}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['unpacking', [3,4,5]]
print_params(*values_list_2, 42)