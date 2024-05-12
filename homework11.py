def test_function(*params):
    print(*params)


test_function(1, 2, [3, 4], 'строка', True)


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))
print(factorial(5))
print(factorial(6))
