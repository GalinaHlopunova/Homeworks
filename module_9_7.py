import math


def is_prime(func):
    def wrapper(*args, **kwargs):
        s = func(*args, **kwargs)
        k = 0
        if s <= 1:
            print("Ни простое, ни составное")
        else:
            for i in range(2, int(math.sqrt(s)) + 1):
                if s % i == 0:
                    k +=1
            if k > 0:
                print("Составное")
            else:
                print("Простое")
        return s
    return wrapper


@is_prime
def sum_three(a, b, c):
    sum_ = a + b + c
    return sum_


result = sum_three(2, 3, 6)
print(result)
