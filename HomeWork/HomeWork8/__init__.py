import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


start_time_recurs = time.perf_counter()
result = factorial(5)
end_time_recurs = time.perf_counter()


result_time_recurs = end_time_recurs - start_time_recurs
print(result_time_recurs)





def factorial_func(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


start_time_func = time.perf_counter()
factorial_func(5)
end_time_func = time.perf_counter()

result_time_func = end_time_func - start_time_func
print(result_time_func)




def factorial_gen(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    yield result

start_time_gener = time.perf_counter()
generator = factorial_gen(5)
end_time_gener = time.perf_counter()



result_time_gener = end_time_gener - start_time_gener
print(result_time_gener)



#Декораторы

def typed_dec(func):

    def wrapper(a, b):
        if type(a) == int:
            a = str(a)
        if type(b) == int:
            b = str(b)
        return func(a, b)
    return wrapper


@typed_dec
def add_two_symbols(a, b):
    return a + b



print(add_two_symbols(2, 6))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))




def typed_dec_three(func):

    def wrapper(a, b, c):
        if type(a) == str:
            a = int(a)
        if type(b) == str:
            b = int(b)
        if type(c) == str:
            c = int(c)
        return func(a, b, c)
    return wrapper


@typed_dec_three
def add_three_symbols(a, b, c):
    return a + b + c


print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))


alphabet = ('abcdefghijklmnopqrstuvwxyz')
number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5:
 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12:
 'twelve',13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17:
 'seventeen', 18: 'eighteen', 19: 'nineteen'}




def sort_numbers_lexicographically(numbers):
    sorted_numbers = sorted(numbers, key = lambda x: number_names[x])
    return ' '.join(map(str, sorted_numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
result = sort_numbers_lexicographically(number_names)
print(result)

# def simple_calculator(*args):
#     result = 1
#     numbers = []
#     marks = []
#     for kwarg in args:
#         if type(kwarg) == int:
#             numbers.append(kwarg)
#         else:
#             marks.append(kwarg)
#     return numbers, marks
#
# print(simple_calculator(2**3 - 1 = 7))



