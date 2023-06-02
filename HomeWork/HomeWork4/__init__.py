# 1
var_int = 10
var_float = 8.4
var_str = 'No'
big_int = var_int * 3.5
var_float = var_float - 4
print(var_int / var_float)
print(big_int / var_float)
var_str = 2 * var_str + 3 * 'Yes'
print(var_str)
print(var_int)
print(var_float)
print(big_int)

# 1  strings
str_1 = 'abcdefgh'
print(str_1[0:8:7])
print(str_1[2:6:3])

# 2  strings
str_3 = 'abcdefghijklmn'
print(str_3[0:7:1])
print(str_3[4:8:1])
print(str_3[3:13:3])
print(str_3[::-1])

# 3  strings
str_4 = 'my name is name'
str_main = str_4[0:11:1] + 'Artiom'
print(str_main)

# 4  strings

x = 'Hello World!'
print(x.index('W'))
print(x.count('l'))
print('"Hello" at the beginning:', x.startswith('Hello'))
print('"qwe" at the end:', x.endswith('qwe'))

# 1 lists
firs = [8, 9, 10, 11, 12, 13]
gears = [1, 2, 3, 4, 5, 6, 7]

# 2
print(firs[2])

# 3
gears[6] = 8
print(gears)

# 4
min_list = gears + firs
print(min_list)

# 5
fin_list = min_list[3:10:1]
print(fin_list)

# 6
fin_list = fin_list + [2] + [6]
print(fin_list)

# 7-8
k = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print('united list:', c)


# Логические операции
# 1
c = 8
d = 11

# 2
print(c * c > d * d and c * d > d + c)
print(c * c * d == c * c + 640 and c * d == c + 80)
print((c + c) * d == d + 165 and 321 + c == d + 318)
print((c + d) * d < d * d * 1312 and (d * d * d) * c > (c * c * c * c) * d)

# 3
g = 223
h = 234
print(g * h * 843 > g * c * 41311 or g + h + h + h > h + h + 134)
print(g > h or h > g)
print(h * 2131 < g * 2111 or h + 223 < g + g)
print(h * c * d * g > h * h * h or g * g * g > h * h * h)

# 4
str_5 = 'Hello'
str_6 = 'World'
str_99 = str_5 + ' ' + str_6
print(str_99)

# Dictionaries
school = {'1A': '23', '1B': '26', '1C': '28', '2A': '21', '2B': '21', '2C': '29', '3A': '31', '3B': '19', '3C': '27',
          '4A': '25'}
print(school['1A'])
school['1A'] = 24
print(school['1A'])
school['2B'] = 32
print(school['2B'])
school['3A'] = 25
print(school['3A'])
del school['1C']
print(school)

# Преобразование типов
# 1
str_s = 'Robin Singh'
str_new = str_s.split()
print(str_new)

# 2
list_name = [' Ivan ', ' Ivanou ']
str_city = ' Minsk '
str_country = ' Belarus'
print('Привет ' + list_name[1] + list_name[0] + '!' + 'Добро пожаловать в' + str_city + str_country)

# 3
list_lov = ["I", "love", "arrays", "they", "are", "my", "favorite"]
str_lov = list_lov
print(' '.join(str_lov))

# 4
list_tench = ['I', 'Love', 'To', 'Play', 'Football', 'So', 'Much', 'As', 'Tennis']
list_tench[3] = 'sampling'
del list_tench[8]
print(list_tench)

# 5
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = {}
for key in set(a.keys()).union(b.keys()):
    a_values = a.get(key)
    b_values = b.get(key)

    if a_values is None:
        a_values = None
    if b_values is None:
        b_values = None
    ab[key] = [a_values, b_values]
print(ab)

# 1*
m = [1, 5, 2, 9, 2, 9, 1]
for i in m:
    if m.count(i) % 2 != 0:
        print(i)

# 2*
alphabet_down = ('abcdefghijklmnopqrstuvwxyz')
alphabet_up = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def find_the_most_common_letter_in_text(text):
    i = 0
    count_max = 0
    letter_max = ''
    while i < len(alphabet_up):
        number_down = text.count(alphabet_down[i])
        number_up = text.count(alphabet_up[i])
        count_of_incomes = number_down + number_up
        if count_of_incomes > count_max:
            count_max = count_of_incomes
            letter_max = alphabet_down[i]
        i += 1
    print(letter_max, count_max)



find_the_most_common_letter_in_text('Hello World, abcd, Artem,GGGGGGGGGGGGGGGGG')





find_the_most_common_letter_in_text('Hello worlD')

find_the_most_common_letter_in_text('Hello World!')


# Условия
# 1
def upper(x):
    if x > 0:
        x += 1
        print(x)
    else:
        print(x)


# 2
def finder(*args):
    sum = 0
    for arg in args:
        if arg > 0:
            sum += 1
        else:
            sum += 0
    print(sum)


finder(1, 2, 3)


# 3
def goyear(x):
    if x % 4 == 0 and x % 100 == 0 and x % 400 != 0:
        y = 365
    elif x % 4 == 0:
        y = 366
    else:
        y = 365
    print(y)


goyear(1200)


# 4
def liczer(x):
    if x == 1:
        print('Monday')
    elif x == 2:
        print('Tuesday')
    elif x == 3:
        print('Wednesday')
    elif x == 4:
        print('Thursday')
    elif x == 5:
        print('Friday')
    elif x == 6:
        print('Saturday')
    elif x == 7:
        print('Sunday')


liczer(6)


# 5
def masse(x, y):
    if x == 1:
        y = y * 1
        print(y)
    if x == 2:
        y = y / 1000000
        print(y)
    if x == 3:
        y = y / 1000
        print(y)
    if x == 4:
        y = y * 1000
        print(y)
    if x == 5:
        y = y * 100
        print(y)


masse(4, 1000)


# Цикл for
# 1
def sum_between_two_numbers(x, y):
    if y < x:
        print('First number must be more than the second one')
    else:
        total_sum = x
        for num in range(x, y):
            if x != y:
                x += 1
                total_sum += x
        print(total_sum)


sum_between_two_numbers(4, 7)


# 2
def sum_between_two_numbers_notdepend(x, y):
    if y < x:
        total_sum = y
        for num in range(y, x):
            if y != x:
                y += 1
                total_sum += y
        print(total_sum)
    else:
        total_sum = x
        for num in range(x, y):
            if x != y:
                x += 1
                total_sum += x
        print(total_sum)


sum_between_two_numbers_notdepend(4, 7)


def sum_grade_num(*args):
    multiple = 1
    sum_of_minuses = 0
    sum_of_minuse_numbers = 0
    for arg in args:
        if arg > 0:
            multiple = multiple * arg
        elif arg < 0:
            sum_of_minuse_numbers += 1
            sum_of_minuses += arg
    print('Multiple of numbers more than 0: ', multiple)
    print('Sum of minuse numbers: ', sum_of_minuse_numbers)
    print('Sum of number above 0: ', sum_of_minuses)


sum_grade_num(-5, -4, -3, -2, -1, 1, 2, 3, 4, 5)

# 4
swimmers_result_dict = {'Бекиш Александр': '21.07', 'Будник Алексей': '20,34', 'Гребень Анастасия': '22,12'
    , 'Давидович Татьяна': '30', 'Дешук Дмитрий': '24.01', 'Казак Анна': '28,17'}


def best_result_from_dictionary(dict):
    best_result = float('inf')
    for value in dict.values():
        value = float(value.replace(',', '.'))
        if value < best_result:
            best_result = value
    print(best_result)


best_result_from_dictionary(swimmers_result_dict)

# 5
list_of_numbers = [1, 5, 2, 9, 2, 9, 1]
for num in list_of_numbers:
    if list_of_numbers.count(num) % 2 != 0:
        print(num)


# Цикл while
# 1
def factorial_joke(x):
    result = 1
    counter = 1
    while counter <= x:
        result = result * counter
        counter += 1
    print(result)


factorial_joke(10)


# 2
def place_s1_s2(s1, s2):
    years = 0
    while s1 >= 0.1 * s2:
        s1 *= 2
        s2 *= 3
        years += 1
    print(s1)
    print(s2)
    print(years)


place_s1_s2(99, 1)


# 3
def how_much_numbers_in_number(x):
    counter = 1
    while x // 10 >= 1:
        x = x / 10
        counter += 1
    print(counter)


how_much_numbers_in_number(141241431)


# 4
def how_much_years_have(grandpa_year, kid_year):
    N = kid_year
    M = grandpa_year
    year = 0
    while M > 2 * N:
        M += 1
        N += 1
        year += 1
    print(f'Кол-во прошедших лет: ', {year})
    print(f'Возраст деда: ', {M})
    print(f'Возраст спиногрыза: ', {N})


how_much_years_have(57, 7)
