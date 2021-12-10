def porownanie (lista, lista2):
    if len(lista) == len(lista2): #Sprawdzanie czy nastąpiła zmiana ilości plików
        roznica_set = set(lista) - set(lista2)
        roznica = list(roznica_set)
#        print(roznica)  #wypisanie jaki z tych co były został zmieniony

        #informacja gdy nie ma zmiany ilościowej
        if len(roznica) != 0:
            return('Nastąpiła zmiana w pliku(-ach) o hashach: ' ,roznica);
            #print('Nastąpiła zmiana w pliku(-ach) o hashach: ', roznica);
        #informacja jaki plik został zmieniony i informacja
        #else:
        #    print('Brak zmian w plikach .JS');    
        #zmieniajac roznica_set = set(lista2) - set(lista) mozna tez uzyskac
        #hash pliku ktory w tych nowych jest inny

    #Sprawdzanie kiedy jest więcej plików niż było
    elif len(lista2) > len(lista): 
        lista3 = lista2[:]
#        print('Liczba plików większa niż zapisana!')
        
        #Określenie elementów ktore są inne
        for x in range(len(lista)):
            try:
                lista3.remove(lista[x])
                #jeśli oprócz ilości jest zmiana również w pozostałych plikach
            except ValueError:
#                print('Jest więcej zmian niż tylko dodane pliki!')
                continue 
#       print("Hash(-e) plik(-u/-ów) które są inne: ", lista3)
        return("Hash(-e) plik(-u/-ów) które zostały dodane i może zmienione: ", lista3);


    #sprawdzenie kiedy jest mniej plikow niz było
    else: 
        lista3 = lista[:]
#        print('Liczba plików mniejsza niż zapisana!')

        for x in range(len(lista2)):
            try:
                lista3.remove(lista2[x])
            except ValueError:
#               print('Jest więcej zmian niż tylko dodane pliki!')
                continue;
        #print('Hash(-e) plik(-u/-ów) który został usunięty: ', lista3)
        return('Hash(-e) plik(-u/-ów) które zostały usunięte i może zmienione: ', lista3);




lis = [15, 'like', 77, 94, 'hajs']
lis2 = [77, 15, 'like',94, 'hjs', 687]

print(porownanie(lis, lis2))

#Funkcja przyjmuje dwie listy hashy. Najpierw porównuje ilość plików
#i jeśli jest taka sama jak zapisanych w logach porównuje hashe (lista z logów, nowa lista)
#jeśli natomiast liczba plików jest różna daje o tym informacje po czym
#sprawdza pozostałe pliki w razie jakby dodatkowy plik był przynętą dla przykładu
