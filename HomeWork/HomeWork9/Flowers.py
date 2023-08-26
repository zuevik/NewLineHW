class Bouquet:
    def __init__(self):
        self.bouquet = []




    def add_flower(self, *args):
        for arg in args:
            self.bouquet.append(arg)


    def flowers_cost(self):
        final_cost = 0
        for flower in self.bouquet:
            final_cost += flower.cost
        return final_cost


    def bouquet_freshness(self):
        bouquet_freshness = 0
        amount_of_flowers = 0
        for flower in self.bouquet:
            bouquet_freshness += flower.time_of_freshness
            amount_of_flowers += 1
        bouquet_freshness /= amount_of_flowers
        return bouquet_freshness


    def show_bouquet(self):
        print(f'Bouquet contains: {self.bouquet}')






class Accessories(Bouquet):
    def __init__(self, cost):
        super().__init__()
        self.accessories = []


class Ribbon(Accessories):
    def __init__(self, color, wide, long):
        super().__init__(cost = 4)


class Rubber(Accessories):
    def __init__(self, color):
        super().__init__(cost = 2)



class Foil(Accessories):
    def __init__(self, color, material):
        super().__init__(cost = 3)










class Flowers(Bouquet):
    def __init__(self, cost, color, time_of_freshness):
        super().__init__()
        self.cost = cost
        self.color = color
        self.time_of_freshness = time_of_freshness

    def show_info(self):
        print(f'Cost of the flowers: {self.cost} USD')
        print(f'Time of freshness: {self.time_of_freshness} hours')
        print(f'Flowers in the bouquets are: {self.bouquet}')

class chamomile(Flowers):
    def __init__(self):
        super().__init__(cost = 5, color = 'white', time_of_freshness = 12)



class hydrangea(Flowers):
    def __init__(self):
        super().__init__(cost = 6, color = 'purple', time_of_freshness = 15)



class rose(Flowers):
    def __init__(self):
        super().__init__(cost = 9, color = 'red', time_of_freshness = 13)



class tulip(Flowers):
    def __init__(self):
        super().__init__(cost = 8, color = 'yellow', time_of_freshness = 16)



class chrysanthemum(Flowers):
    def __init__(self):
        super().__init__(cost = 10, color = 'blue', time_of_freshness = 11)


chamomile_1 = chamomile()
hydrangea_1 = hydrangea()
rose_1 = rose()
tulip_1 = tulip()
chrysanthemum_1 = chrysanthemum()


my_bouquet = Bouquet()
my_bouquet.add_flower(chamomile_1, hydrangea_1, rose_1, tulip_1, chrysanthemum_1)
my_bouquet.add_flower(hydrangea_1)
my_bouquet.add_flower(rose_1)
my_bouquet.add_flower(tulip_1)
my_bouquet.add_flower(chrysanthemum_1)


Ribbon_red_40_50 = Ribbon('red', 40, 50)

print(f'Average cost of flowers: {my_bouquet.flowers_cost()}')
print(f'Average time of freshness of my bouquet: {my_bouquet.bouquet_freshness()}')


print(my_bouquet.show_info())