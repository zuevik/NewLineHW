# 1
def rounder(x):
    print(round(x))


rounder(2.99)


# 2

def replacer(y):
    print(y.replace('#', '/'))


replacer('www.my_site.com#about')


# 3

def adder(x, y):
    z = x + y
    print(z)


adder('stroka', 'ing')


# 4
def revercer(x):
    x = x.split()
    x = ' '.join(x[::-1])
    print(x)


revercer('Ivan Ivanou')


# 5
def trepper(x):
    x = x.lstrip()
    x = x.rstrip()
    print(x)


trepper(' I am the tennisist ')
# 6
school = {'1A': '23', '1B': '26', '1C': '28', '2A': '21', '2B': '21', '2C': '29', '3A': '31', '3B': '19', '3C': '27',
          '4A': '25'}


# 7


def impact_1(x, y):
    print(x[y])


k = {1, 2, 3, 4, 5, 6}
impact_1(k, 1)


# 8
def rais(x, y):
    print(x in y)


rais('employ', 'employment')


# 9
def yell(x):
    print(x[1])
    print(x[3:13:3])


yell('My name is Agent Smith')

# 10
k = [1, 5, 2, 9, 2, 9, 1]
for i in k:
    if k.count(i) % 2 != 0:
        print(i)
