start = int(input('podaj start:'))
end = int(input('podaj end: '))
my_list = list(range(start,end))





value = int(input("podaj poszukiwana liczbe:"))
found = False

for element in my_list:
    if element == value:
        print('Znaleziono', value)
        found = True

if not found:
    print('Nie znaleziono', value)          