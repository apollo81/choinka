zmienna = input('podaj liczbe od 1 do 10: ')
if zmienna.isdigit() == True and int(zmienna) in range(1,11):
    for mnoznik in range (1,11):
        print(mnoznik, "*", zmienna, "=", mnoznik*int(zmienna))
else:
    print('podałeś złą wartośc spróbój ponownie')



