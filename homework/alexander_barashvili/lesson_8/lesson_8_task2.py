import sys

sys.set_int_max_str_digits(100000)


def fibonacci_gener(limit=100000000000000000000000000000000000000000000000000000000000000000000000):
    f1, f2 = 0, 1
    count_f = 0
    while count_f < limit:
        yield f1
        f1, f2 = f2, f1 + f2
        count_f += 1


count = 1
for number in fibonacci_gener(100000000000000000000000000000000000000000000000000000000000000000000000000):
    if count in {5, 200, 1000, 100000}:
        print(f'Fibonacci number {count} is {number}')
    count += 1
    if count > 100000:
        break
