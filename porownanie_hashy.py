def porownanie (lista, lista2):
    if len(lista) == len(lista2): #Sprawdzanie czy wgl nastąpiły zmiany jeśli jest ich taka sama liczba
        roznica_set = set(lista) - set(lista2)
        roznica = list(roznica_set)
        print(roznica)

        if len(roznica) == 0:
            print('Brak zmian w plikach .JS')
        else:
            print('Nastąpiła zmiana w pliku(-ach) o hashach: ', roznica)
#zmieniajac roznica_set = set(lista2) - set(lista) mozna tez uzyskac
#hash pliku ktory w tych nowych jest inny

        
    elif len(lista2) > len(lista): #Sprawdzanie kiedy jest więcej plików niż było
        lista3 = lista2[:]
        print('Liczba plików większa niż zapisana!')
        
#Określenie elementów ktore są inne
        for x in range(len(lista)):
            try:
                lista3.remove(lista[x])
            except ValueError:
                print('Jest więcej zmian niż tylko dodane pliki!')
                continue
            
        print("Hashe plików które są inne: ", lista3)



    else: #sprawdzenie kiedy jest mniej plikow niz było
        lista3 = lista[:]
        print('Liczba plików mniejsza niż zapisana!')

        for x in range(len(lista2)):
            lista3.remove(lista2[x])
        print('Hash pliku który został usunięty: ', lista3)




#lis = [15, 'like', 77, 94, 'hajs']
#lis2 = [77, 15, 'like',94, 'hajs']

#porownanie(lis, lis2)

#Jeśli nie będziemy później potrzebować hashy do niczego a tylko to co zwróci funkcja czyli co się zmieniło
#to można będzie później pousuwać lista3 i operować na lista oraz lista2
#bo wtedy po prostu będziemy operować na oryginalnych listach a nie kopiach

#Funkcja przyjmuje dwie listy hashy. Najpierw porównuje ilość plików
#i jeśli jest taka sama jak zapisanych w logach porównuje hashe
#jeśli natomiast liczba plików jest różna daje o tym informacje po czym
#sprawdza pozostałe pliki w razie jakby dodatkowy plik był przynętą


