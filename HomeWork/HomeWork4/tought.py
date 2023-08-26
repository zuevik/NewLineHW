alphabet_down = ('abcdefghijklmnopqrstuvwxyz')
alphabet_up = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def find_the_most_common_letter_in_text(text):
    i = 0
    count_max = 0
    letter_max = ''
    while i < len(alphabet_up):
        count_of_incomes = text.count(alphabet_up[i]) + text.count(alphabet_down[i])
        if count_of_incomes > count_max:
            count_max = count_of_incomes
            letter_max = alphabet_down[i]
        i += 1
    print(letter_max, count_max)



find_the_most_common_letter_in_text('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum')


print(2.2 ** 2)