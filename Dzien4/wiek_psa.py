# 2 = 10.5
# 3 =< 4

wiek = input('podaj wiek psa: ')
while not wiek.isdigit():
    wiek = input('podaj wiek psa: ')
wiek = int(wiek)
if wiek < 3:
    print(wiek *10.5)
else:
    print(21 + (wiek-2)*4)
