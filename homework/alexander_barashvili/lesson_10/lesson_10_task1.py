def finish_me(func):

    def wrapper(*args):
        func(*args)
        print('finished')
    return wrapper


@finish_me
def programmer(*args):
    print(args)


programmer('I', 'Love', 'Python')
