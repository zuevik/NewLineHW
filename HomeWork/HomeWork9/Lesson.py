import datetime
import time

def time_dec(func):
    def wrapper(n):
        start_time_dec = time.perf_counter()
        result = func
        end_time_dec = time.perf_counter()
        execution_time = end_time_dec - start_time_dec
        print("Время выполнения:", execution_time, "сек")
        return result
    return wrapper


@time_dec
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

res = calculate_factorial(5)
print(res)


def retry(num_retries):
    def decorator_dec(func):
        def wrapper(*args):
            for i in range(num_retries):
                try:
                    result = func(*args)
                    return result
                except ZeroDivisionError:
                    print('Error: ZeroDivisionError.Retrying...')
            print('Error: Maximum number of retries reached')
        return wrapper
    return decorator_dec






@retry(num_retries=10)

class CustomError(Exception):
    def __init__(self, message):
        self.message = message


def retry(num_retries):
    def decorator(func):
        def wrapper(*args):
            for i in range(num_retries):
                try:
                    result = func(*args)
                    return  result
                except ZeroDivisionError:
                    print('ZeroDivisionError, retrying')
            print('No result, error')
        return wrapper
    return decorator


@retry(num_retries=3)
def divide(a, b):
    return a / b

result = divide(10, 0)
print("Result:", result)
#

# import datetime
#
# class Hero:
#     count = 0
#     dof = datetime.date(1984, 5, 4)
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#         Hero.count += 1
#
#
#     def print_name(self):
#         print('I am ' + self.name)
#
#     def help(self, name_of_person):
#         print(f'I {self.name}! I will save you {name_of_person}')
#
#
#     @classmethod
#     def give_birthday(cls):
#         print(cls)
#         return cls('Spiderman2', 'паутина2')
#
#
#     @staticmethod
#     def saved(self):
#         print(' I save you')
#
#
# spiderman = Hero('Spiderman', 'паутина')
# spiderman.help('Мэри Джейн')
# spiderman.saved()
#
#
# print(spiderman.give_birthday())




class B:
    arg = 'Python'
    def g(self):
        return self.arg

print(B.arg)



class Father:
    def __init__(self):
        self.surname = 'Ивко'
        self.name = 'Денис'

class Son(Father):
    age = 10
    def __init__(self):
        super().__init__()
        self.name = 'Николай'

son = Son()
print(son.name, son.surname, son.age, sep = ' ')

MyType = type('MyType', (object,), {'a':1})
print(MyType)
print(MyType.a)


print(isinstance(son, (Son, int)))
print(isinstance(son, (Father)))













class Geom:

    def __init__(self):
        print('Geom')

class  Triangle(Geom):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

print(issubclass(Geom, list))
print(issubclass(Triangle, Geom))


class Car:

    def start(self, a, b = None):
        if b is not None:
             print(b - a)
        else:
            print(a)





car = Car()
car.start(40)
car.start(40, 45)




class Person(object):
    name: str = 'Mark'
    dob = datetime.date(2024, 8, 10)
    husband = None
    sex = 'male'

    def print(self):
        print(sex)
    @property
    def age(self):
        return(datetime.date.today() - self.dob).days // 365

    @age.deleter
    def age(self):
        self.dob = datetime.date(1, 1, 1)

    def is_married(self):
        return self.husband is not None

person = Person()
print(person.age)
print(person.is_married())
del person.age
print(person.age)


from dataclasses import dataclass

@dataclass
class Bill:
 table_number: int
 meal_amount: float
 served_by: str
 tip_amount: float = 0.0




bill_0 = Bill(table_number=5, meal_amount=50.5,
                  served_by="John", tip_amount=7.5)
bill_1 = Bill(table_number=5, meal_amount=50.5,
                  served_by="John", tip_amount=7.5)
print(bill_0 == bill_1)


class Car :

    def __doc__(self):
        return 'Car'

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return f'STR: Name of car: {self.name}'

    def __repr__(self):
        return f'REPR: Name of car: {self.name}'

    def __int__(self):
        return int(self.year)

    def __eg__(self, obj):
        return self.name == obj.name and self.year == obj.year


c = Car('Volvo', '1996')
c2 = Car('volvo', '1996')
print(c)
print(repr(c))
print(int(c))
print(c == c2)