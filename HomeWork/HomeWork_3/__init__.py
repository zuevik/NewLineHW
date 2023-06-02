#1
print(round(-1.6))
print(round(2.99))

#2
str_1 = 'www.my_site.com#about'
print(str_1.replace('#', '/'))

#3
str1 = 'stroka'
str2 = 'ing'
str3 = str1 + str2
print(str3)

#4
str_4 = 'Ivan Ivanou'
str_4 = str_4.split()
str_4 = ' '.join(str_4[::-1])
print(str_4)

#5
str_5 = ' I am the tennisist '
str_5 = str_5.lstrip()
str_5 = str_5.rstrip()
print(str_5)

#6
school = {'1A': '23','1B': '26','1C': '28','2A': '21','2B': '21','2C': '29','3A': '31','3B': '19','3C': '27','4A': '25'}

#7
list_g = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print(list_g[1])

#8
str_1 = 'employ'
str_2 = 'employment'
print(str_1 in str_2)

#9

x = "My name is Agent Smith"
print(x[1]) #y
print(x[3:13:3]) #nesg

#10
list_m =  [1, 5, 2, 9, 2, 9, 1]
for i in list_m:
    if list_m.count(i) %2 != 0:
        print(i)

