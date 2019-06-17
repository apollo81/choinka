#petla while

# pobrac od użytkownika dowolna calkowita liczbe ( pominac sprawdzanie liczby )
#


# liczba = int(input('podaj liczbe calkowita: '))
#
# counter = 0
#
# while counter < value:
#     print('Python')
#     counter = counter + 1

value = int(input('podaj liczbe calkowita: '))

counter = 0
iteration_no = 0

while counter < value:
    iteration_no += 1
    print('Python', iteration_no)
    if iteration_no == 100:
        break