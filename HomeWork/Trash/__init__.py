# def fib(n, current = 0, previous = 1, result = [0]):
#     if n == 0:
#         return result
#     else:
#         result.append(current + previous)
#         return fib(n - 1, current + previous, current, result)
# print(fib(5))
#
#
#
# def fib_gen():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, b + a
#
#
# generator = fib_gen()
# for i in range(10):
#     print(next(generator), end = ' ')



# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#
#         return n * factorial(n - 1)
#
#
# print(factorial(9))
#
# class MyException(Exception):
#     pass
#
#
# def toy(kind):
#
#     def inner(color):
#         try:
#             if kind == 'Bears' and color == 'red':
#                 raise MyException('error')
#             else: print(f'Игрушка - {kind}, Цвет - {color}')
#         except MyException as e:
#             pass
#     return inner
#
# ball = toy('Ball')
# barbie = toy('Barbies')
# bear = toy('Bears')
#
# ball('red')
# ball('green')
# ball('blue')
# bear('green')
# bear('red')
# bear('blue')


def decorator(func):

    def wrapper(name, surname):
        print('Имя заказчика: ')
        func(name, surname)


    return wrapper

def decorator_2(func):

    def wrapper(name, surname):
        print('Имя пользователя: ')
        func(name, surname)


    return wrapper


@decorator
def print_name(name, surname):
    print(f'{name}, {surname}')


@decorator_2
def print_employ(name, surname):
    print(f'{name}, {surname}')


print_name(name = 'Bob', surname = 'Yong')
print_employ(name = 'Fly', surname = 'Dooge')









def count(iters):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('before')
            for i in range(iters):
                func(i)
        return wrapper
    return decorator



@count(iters = 10)
def func(a):
    print(a)

func()