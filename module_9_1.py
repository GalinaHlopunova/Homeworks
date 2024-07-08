def apply_all_func(int_list, *functions):
    results = dict()
    for function in functions:
        key = function.__name__
        value = function(int_list)
        results[key] = value
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
