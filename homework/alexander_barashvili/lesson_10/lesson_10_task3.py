def calculator(func):

    def wrapper(number1, number2, operation=None):
        if operation is not None:
            func(number1, number2, operation)
        elif number1 == number2:
            operation = '+'
        elif number1 < 0 or number2 < 0:
            operation = '*'
        elif number1 > number2:
            operation = '-'
        elif number1 < number2:
            operation = '/'
        return func(number1, number2, operation)
    return wrapper


@calculator
def calc(first, second, operation=None):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


number_1, number_2 = (int(input("Enter first number: ")),
                      int(input("Enter second number: ")))

print(f"Result: {calc(number_1, number_2, '*')}")
