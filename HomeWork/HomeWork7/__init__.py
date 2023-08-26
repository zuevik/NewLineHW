#1

first_task_lm = lambda x: 'Hello, ' + x

print(first_task_lm('Artiom'))

#2
list_name = ['Artiom', 'Olga', 'Enzo', 'Fabricci', 'Kuper']

second_task_lm = list(map(lambda name: f'Hello, {name}', list_name))

print(second_task_lm)

#1 Генераторы

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

def changing_generator(n):
    for i in n:
        yield i * -1

changer = changing_generator(numbers)

for number in changer:
    print(number)


#2
sentence = 'the quick brown fox jumps over the lazy dog'


def counting_of_letter_generator(text):
    new_text = text.split(' ')
    for word in new_text:
        try:
            if word == 'the':
                raise ValueError('Слово "the" исключено')
            result = len(word)
            yield result
        except ValueError as e:
            print(e)

generetor = counting_of_letter_generator(sentence)


for count in generetor:
    print(f'Кол-во букв в слове: {count}')



#3 шифр

alphabet_down = ('abcdefghijklmnopqrstuvwxyz')
alphabet_up = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
def cesar_encoder(text, step):
    i = 0
    final_text = ''
    index_of_final_letter = 0
    for letter in text:
        if letter in alphabet_down:
            index_of_final_letter = (alphabet_down.index(letter) + step) % len(alphabet_down)
            final_text += alphabet_down[index_of_final_letter]
        elif letter in alphabet_up:
            index_of_final_letter = (alphabet_up.index(letter) + step) % len(alphabet_up)
            final_text += alphabet_up[index_of_final_letter]
        else:
            final_text += letter
    print(final_text)
cesar_encoder('aaazz', 2)


def cesar_decoder(text, step):
    i = 0
    final_text = ''
    index_of_final_letter = 0
    for letter in text:
        if letter in alphabet_down:
            index_of_final_letter = (alphabet_down.index(letter) - step) % len(alphabet_down)
            final_text += alphabet_down[index_of_final_letter]
        elif letter in alphabet_up:
            index_of_final_letter = (alphabet_up.index(letter) - step) % len(alphabet_up)
            final_text += alphabet_up[index_of_final_letter]
        else:
            final_text += letter
    print(final_text)


cesar_decoder('cccbb', 2)