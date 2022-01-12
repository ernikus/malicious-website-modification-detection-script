# need full path to the two files
# print diffs between these two files
# def amountlines(f):
#     #x=(sum(1 for line in open(f)))
#     return (sum(1 for line in open(f)))

def checkHTML(f1, f2):

    import filecmp

    # shallow comparison
    # NOTE: here you can't write e.g."./xyz.txt"
    result = filecmp.cmp(f1, f2)
#    print(result)
    if(result==True):
        return(result)

    #~~~~~~~~~~~~~~~~~~~~~~~~~

    if result == False:
        # deep comparison
        result = filecmp.cmp(f1, f2, shallow=False)
#        print(result)
        if(result==True):
            return(result)

    #~~~~~~~~~~~~~~~~~~~~~~~~~

    if result == False:


        list = open(f1, 'r')
        lis = list.readlines()
        list2 = open(f2, 'r')
        lis2 = list2.readlines()
        f = open("diffHTML.txt", "w", -1, "utf-8")
        f1 = open("roznicaHTML.txt", "w", -1, "utf-8")
        lista = []; lista2 = []
    #    lista = [15, 'like', 77, 94, 'hajs']
    #    lista2 = [77, 15, 'like',94, 'hjs', 687]

        for line in lis:
            lista.append(line.strip())

        for line in lis2:
            lista2.append(line.strip())


        if (len(lista) == len(lista2)): #Sprawdzanie czy nastąpiła zmiana ilości plików
            roznica_set = set(lista) - set(lista2)
            roznica = []
            for id in roznica_set:
                roznica.append(id)
    #        print(len(roznica), "\n")
            for i in range(len(roznica)-1, 0 , -1):
    #            print(i)
                if ('google' in str(roznica[i])):
                    roznica.remove(roznica[i])

                elif ('"datatime"' in str(roznica[i])):
                    roznica.remove(roznica[i])

                elif ('"datetime"' in str(roznica[i])):
                    roznica.remove(roznica[i])
                else:
                    continue;

            #roznica = list(roznica_set)
            #print(roznica)  #wypisanie jaki z tych co były został zmieniony

            #informacja gdy nie ma zmiany ilościowej
#                print('Nastąpiła zmiana w lini(-ach): ' ,roznica);
            if len(roznica)>0:
                f.write('Nastąpiła zmiana w lini(-ach): \n');
                for line in roznica:
                    line = str(line)
                    f.write(line);
                    f.write("\n");
                #print('Nastąpiła zmiana w pliku(-ach) o hashach: ', roznica);
            #informacja jaki plik został zmieniony i informacja
            else:
                f.write('Nie nastąpiła zadna zmiana w kodzie strony: \n');
                return(False);
            #zmieniajac roznica_set = set(lista2) - set(lista) mozna tez uzyskac
            #hash pliku ktory w tych nowych jest inny

        #Sprawdzanie kiedy jest więcej plików niż było
        elif (len(lista2) > len(lista)):
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

            for i in range(len(lista3)-1, 0 , -1):
    #            print(i)
                if ('google' in str(lista3[i])):
                    lista3.remove(lista3[i])

                elif ('"datatime"' in str(lista3[i])):
                    roznica.remove(lista3[i])

                elif ('"datetime"' in str(lista3[i])):
                    lista3.remove(lista3[i])
                else:
                    continue;
    #       print("Hash(-e) plik(-u/-ów) które są inne: ", lista3)
            f.write("linia(-e), które zostały dodane i może zmienione: \n");
            for line in lista3:
                line = str(line)
                f.write(line);
                f.write("\n");


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

            for i in range(len(lista3)-1, 0 , -1):
    #            print(i)
                if ('google' in str(lista3[i])):
                    lista3.remove(lista3[i])

                elif ('"datatime"' in str(lista3[i])):
                    roznica.remove(lista3[i])

                elif ('"datetime"' in str(lista3[i])):
                    lista3.remove(lista3[i])
                else:
                    continue;
            #print('Hash(-e) plik(-u/-ów) który został usunięty: ', lista3)
            f.write('linia(-e), które zostały usunięte i może zmienione: \n');
            for line in lista3:
                line = str(line)
                f.write(line);
                f.write("\n");

        list.close()
        list2.close()
        f.close()
        return (result)

# ~ I am thinking about giving here only path to the right folder and in function specify the files to compare ~

#file_no1 = "/home/kali/Desktop/projekt/FIN/logs/10_01_2022_10/HTML.txt"
#file_no2 = "/home/kali/Desktop/projekt/FIN/logs/10_01_2022_11/HTML.txt"

#checkHTML(file_no1, file_no2)

# checkHTML()
