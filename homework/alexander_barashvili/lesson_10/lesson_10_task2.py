def repeat(func):

    def wrapper(*args, count=5):
        for i in range(count):
            func(*args)

    return wrapper


@repeat
def example(text):
    print(text)

@repeat
def example1():
    print('I Love Python')


example('print me', count=3)
example1()
