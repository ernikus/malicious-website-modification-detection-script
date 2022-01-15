# need full path to the two files
# print diffs between these two files

def checkHTML(f1, f2):

    import filecmp

    # shallow comparison
    # NOTE: here you can't write e.g."./xyz.txt"
    result = filecmp.cmp(f1, f2)
    if(result==True):
        return(result)

    #~~~~~~~~~~~~~~~~~~~~~~~~~

    if result == False:
        # deep comparison
        result = filecmp.cmp(f1, f2, shallow=False)
        if(result==True):
            return(result)

    #~~~~~~~~~~~~~~~~~~~~~~~~~

    if result == False:

        list = open(f1, 'r')
        lis = list.readlines()
        list2 = open(f2, 'r')
        lis2 = list2.readlines()
        f = open("diffHTML.txt", "w", -1, "utf-8")
        lista = []; lista2 = []

        for line in lis:
            lista.append(line.strip())

        for line in lis2:
            lista2.append(line.strip())

#liczba linii html jest taka sama
        if (len(lista) == len(lista2)): #Sprawdzanie czy nastąpiła zmiana ilości plików
            #pokazujemy co sie zmienilo w nowym pliku
            lista3 = lista2[:]

            #Określenie elementów ktore są inne
            for x in range(len(lista)):
                try:
                    lista3.remove(lista[x])
                    #jeśli oprócz ilości jest zmiana również w pozostałych plikach
                except ValueError:
                    continue

            for i in range(len(lista3)-1, 0 , -1):
                if ('google' in str(lista3[i])):
                    lista3.remove(lista3[i])

                elif ('"datatime"' in str(lista3[i])):
                    lista3.remove(lista3[i])

                elif ('"datetime"' in str(lista3[i])):
                    lista3.remove(lista3[i])
                else:
                    continue;

            No=[]
            pomin=[]
            for x in range(0, len(lista3), 1):
                for y in range(len(lista2)-1, -1, -1):
                    if (lista3[x]==lista2[y]):# && !(y in pomin)):
                        if((y in pomin)==False):
                            pomin.append(y)
                            No.append(y+1)
                            #del lista2[y]
                            break;

            if (len(No)>1):
                for n in range(len(No)-1, 0, -1):
                    for i in range(n):
                      if No[i] > No[i + 1]:
                        # swapping data if the element is less than next element in the array
                        No[i], No[i + 1] = No[i + 1], No[i]
                        lista3[i], lista3[i + 1] = lista3[i + 1], lista3[i]

            no=0

            f.write('Nastąpiła zmiana w lini(-ach): \n');
            if No:
                for line in lista3:
                    line = str(line)
                    f.write("linia ");
                    f.write(str(No[no])); no+=1;
                    f.write(":\t\t");
                    f.write(line);
                    f.write("\n");

            #informacja jaki plik został zmieniony i informacja
            else:
                f.write('Nie nastąpiła zadna zmiana w kodzie strony: \n');
                return(False);

    #Sprawdzanie kiedy jest więcej linii niż było
        elif (len(lista2) > len(lista)):
            lista3 = lista2[:]

            #Określenie elementów ktore są inne
            for x in range(len(lista)):
                try:
                    lista3.remove(lista[x])
                    #jeśli oprócz ilości jest zmiana również w pozostałych plikach
                except ValueError:
                    continue

            for i in range(len(lista3)-1, 0 , -1):
                if ('google' in str(lista3[i])):
                    lista3.remove(lista3[i])

                elif ('"datatime"' in str(lista3[i])):
                    lista3.remove(lista3[i])

                elif ('"datetime"' in str(lista3[i])):
                    lista3.remove(lista3[i])
                else:
                    continue;

            No=[]
            pomin=[]
            for x in range(0, len(lista3), 1):
                for y in range(len(lista2)-1, -1, -1):
                    if (lista3[x]==lista2[y]):# && !(y in pomin)):
                        if((y in pomin)==False):
                            pomin.append(y)
                            No.append(y+1)
                            #del lista2[y]
                            break;

            if (len(No)>1):
                for n in range(len(No)-1, 0, -1):
                    for i in range(n):
                      if No[i] > No[i + 1]:
                        # swapping data if the element is less than next element in the array
                        No[i], No[i + 1] = No[i + 1], No[i]
                        lista3[i], lista3[i + 1] = lista3[i + 1], lista3[i]

            no=0
            f.write("linia(-e), które zostały dodane i może zmienione: \n");
            if No:
                for line in lista3:
                    line = str(line)
                    f.write("linia ");
                    f.write(str(No[no])); no+=1;
                    f.write(":\t\t");
                    f.write(line);
                    f.write("\n");


        #sprawdzenie kiedy jest mniej linii niz było
        else:
            lista3 = lista[:]

            for x in range(len(lista2)):
                try:
                    lista3.remove(lista2[x])
                except ValueError:
                    continue;

            for i in range(len(lista3)-1, 0 , -1):
                if ('google' in str(lista3[i])):
                    lista3.remove(lista3[i])

                elif ('"datatime"' in str(lista3[i])):
                    roznica.remove(lista3[i])

                elif ('"datetime"' in str(lista3[i])):
                    lista3.remove(lista3[i])
                else:
                    continue;

            No=[]
            pomin=[]
            for x in range(0, len(lista3), 1):
                for y in range(len(lista)-1, -1, -1):
                    if (lista3[x]==lista[y]):# && !(y in pomin)):
                        if((y in pomin)==False):
                            pomin.append(y)
                            No.append(y+1)
                            #del lista2[y]
                            break;
            print(lista3)
            print(No)
            if (len(No)>1):
                for n in range(len(No)-1, 0, -1):
                    for i in range(n):
                      if No[i] > No[i + 1]:
                        # swapping data if the element is less than next element in the array
                        No[i], No[i + 1] = No[i + 1], No[i]
                        lista3[i], lista3[i + 1] = lista3[i + 1], lista3[i]
            print(No)

            no=0
            f.write('linia(-e), które zostały usunięte i może zmienione: \n');
            if No:
                for line in lista3:
                    line = str(line)
                    f.write("linia ");
                    f.write(str(No[no])); no+=1;
                    f.write(":\t\t");
                    f.write(line);
                    f.write("\n");

        list.close()
        list2.close()
        f.close()
        return (result)

# ~ I am thinking about giving here only path to the right folder and in function specify the files to compare ~

# file_no1 = "/home/kali/Desktop/project/log/14_01_2022/HTML.txt"
# file_no2 = "/home/kali/Desktop/project/log/14_01_2022_09_00_41/HTML.txt"

# checkHTML(file_no1, file_no2)

# checkHTML()
