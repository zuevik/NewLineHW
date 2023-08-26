# class MyFather:
#     def __init__(self, surname):
#         self.surname = surname
#
#     def say_my_surname(self):
#         print(f'Hello, my surname is {self.surname}')
#
#
#
#
# class Me(MyFather):
#     name = 'Artiom'
#
#     def __init__(self, name):
#         super().__init__('Zuev')
#         self.name = name
#
#     def print_my_name(self):
#         print(f'Say my name, you, dumbass. You are {self.surname} {self.name}')
#
# Father = MyFather('Zuev')
# Father.say_my_surname()
#
#
# myself = Me('Artiom')
# myself.say_my_surname()
# myself.print_my_name()



class CarBase:
    def __init__(self, brand):
        self.brand = brand

    def country_of_brand(self, country):
        self.country = country




class Car(CarBase):
    def __init__(self, brand , color, high, weight):
        super().__init__(brand)
        self.high = high
        self.color = color
        self.weight = weight

    def start(self):
        raise NotImplementedError('Метод start, должен быть определен в дочернем классе')


class interier(Car):
    def __init__(self, places, pedals, windows, brand, color, high, weight):
        super().__init__(brand, color, high, weight)
        self.places = places
        self.pedals = pedals
        self.windows = windows


    def _type_of_a_car(self):
        settings = self.places + self.windows + self.pedals
        if settings <= 8:
            type_of_a_car = 'GT'
        elif settings in range(9, 12):
            type_of_a_car = 'Sport'
        else:
            type_of_a_car = 'Family'
        print(type_of_a_car)


class PetrolEngine(CarBase):
    def start(self):
        print('Бензиновый двигатель заводим с помощью искры зажигания')

class ElectricEngine(CarBase):
    def start(self):
        print('Заводим электрический двигатель с помощью электромотора')

    def start_engine(engine):
        engine.start()


if __name__ == "__main__":
    our_engine = PetrolEngine('Porsche')
    our_second_engine = ElectricEngine('Porsche')


    our_engine.start()
    our_second_engine.start()







our_car = interier(2,2,3, 'Porsche', 'yellow', 1200, 900)
our_car._type_of_a_car()







