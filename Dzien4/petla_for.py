# magic = 'abrakadabra'
# counter = 0
# char_to_count = 'a'
# consonants = 'brcd'
#
#
# for char in magic:
#     if char == char_to_count:
#         counter_1 += 1
#
# print(f'liczba wystapien znaku {char_to_count} wynosi: {counter_1}')

magic = 'abrakadabra'
vowels_counter = 0
consonants_counter = 0
vowels = 'a'
consonants = 'brcdk'

for char in magic:
    if char in vowels:
        vowels_counter += 1
    elif char in consonants:
        consonants_counter += 1
    else:
        continue
    print('char',char)

print('ilosc samoglosek', vowels_counter)
print('ilosc wspolglosek', consonants_counter)


