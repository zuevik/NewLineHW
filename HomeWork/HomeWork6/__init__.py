#1
with open('nums.txt', 'w') as f:
    f.writelines('1, 2, 3, 4, 5, 6, 7, 8, 9')


with open('nums.txt', 'r') as f:
    file_info = f.read()
    final_line = file_info.split(', ')
    print(final_line[0])
    print(final_line[1])
    print(final_line[-1])
    print(final_line[-2])

#2
with open('task_2_starter.txt', 'w') as file_2:
    file_2.writelines('1, 2, 3, 4, 5, 6, 7, 8, 9, 10')

with open('task_2_starter.txt', 'r') as file_2, open('task_2_even.txt', 'w') as even, open('task_2_odd.txt', 'w') as odd:
    file_mess_of_numbers = file_2.read()
    file_mess_of_numbers = file_mess_of_numbers.split(', ')
    file_mess_of_numbers = list(map(int, file_mess_of_numbers))
    for i in file_mess_of_numbers:
        if i % 2 == 0:
            even.write(str(i) + '\n')
        elif i % 2 == 1:
            odd.write(str(i) + '\n')


#3
with open('float_numbers_list_task_3.txt', 'w') as start_float:
    start_float.writelines('1.2, 7.1, 8.2, 10.9, 11.11, 2.43, 1.3123')

with open('float_numbers_list_task_3.txt', 'r') as start_float:
    start_float_info = start_float.read()
    start_float_info = start_float_info.split(', ')
    start_float_info = list(map(float, start_float_info))


with open('float_numbers_list_task_3.txt', 'w') as start_float:
    for i in start_float_info:
        i = i ** 2
        start_float.writelines(str(i) + '\n')

#4
with open('coded_1.bin', 'wb') as first_coded:
    str_1 = [1, 2, 1, 3, 54]
    arr_1 = bytearray(str_1)
    first_coded.write(arr_1)

with open('coded_2.bin', 'wb') as second_coded:
    str_2 = [13,51,36,62]
    arr_2 = bytearray(str_2)
    second_coded.write(arr_2)



with open('coded_1.bin', 'rb') as first_coded:
    first_binner_list = first_coded.read()


with open('coded_2.bin', 'rb') as second_coded:
    second_binner_list = second_coded.read()


with open('coded_1.bin', 'wb') as first_coded:
    first_coded.write(second_binner_list)



with open('coded_2.bin', 'wb') as second_coded:
    second_coded.write(first_binner_list)






