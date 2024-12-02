a = 'результат операции: 42'
b = 'результат операции: 54'
c = 'результат работы программы: 209'
d = 'результат: 2'

def print_summ_args(*args):
    for arg in args:
        arg = int(arg[arg.index(':') + 2:]) + 10
        print(arg)

print_summ_args(a, b, c, d)
