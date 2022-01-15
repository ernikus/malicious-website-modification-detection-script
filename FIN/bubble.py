# need full path to the two files
# print diffs between these two files
from PathFinder import PathFinder

def checkHTML(f1, f2):

    import filecmp
    path=PathFinder()
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
        path = path + "diffHTML.txt"
        f = open(path, "w", -1, "utf-8")
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
                elif(('<!--' in str(lista3[i])) and ('-->' in str(lista3[i]))):
                    lista3.remove(lista3[i])
                elif(('</div>' in str(lista3[i])) or ('<div>' in str(lista3[i]))):
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

            if No:
                f.write('Nastąpiła zmiana w lini(-ach): \n');
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
        else:
            lista3 = lista2[:]
            lista4 = lista[:]
            #Określenie elementów ktore są inne
            for x in range(len(lista)):
                try:
                    lista3.remove(lista[x])
                    #jeśli oprócz ilości jest zmiana również w pozostałych plikach
                except ValueError:
                    continue

            for x in range(len(lista2)):
                try:
                    lista4.remove(lista2[x])
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
                elif(('<!--' in str(lista3[i])) and ('-->' in str(lista3[i]))):
                    lista3.remove(lista3[i])
                elif(('</div>' in str(lista3[i])) or ('<div>' in str(lista3[i]))):
                    lista3.remove(lista3[i])
                else:
                    continue;

            for i in range(len(lista4)-1, 0 , -1):
                if ('google' in str(lista4[i])):
                    lista3.remove(lista4[i])
                elif ('"datatime"' in str(lista4[i])):
                    lista4.remove(lista4[i])
                elif ('"datetime"' in str(lista4[i])):
                    lista4.remove(lista4[i])
                elif(('<!--' in str(lista4[i])) and ('-->' in str(lista4[i]))):
                    lista4.remove(lista4[i])
                elif(('</div>' in str(lista4[i])) or ('<div>' in str(lista4[i]))):
                    lista4.remove(lista4[i])
                else:
                    continue;

            No=[]
            pomin=[]
            for x in range(0, len(lista3), 1):
#                for y in range(len(lista2)-1, -1, -1):
                for y in range(0, len(lista2)-1, 1):
                    if (lista3[x]==lista2[y]):# && !(y in pomin)):
                        if((y in pomin)==False):
                            pomin.append(y)
                            No.append(y+1)
                            #del lista2[y]
                            break;

            No1=[]
            pomin.clear()
            for x in range(0, len(lista4), 1):
#                for y in range(len(lista2)-1, -1, -1):
                for y in range(0, len(lista)-1, 1):
                    if (lista4[x]==lista[y]):# && !(y in pomin)):
                        if((y in pomin)==False):
                            pomin.append(y)
                            No1.append(y+1)
                            #del lista2[y]
                            break;

            if (len(No)>1):
                for n in range(len(No)-1, 0, -1):
                    for i in range(n):
                      if No[i] > No[i + 1]:
                        # swapping data if the element is less than next element in the array
                        No[i], No[i + 1] = No[i + 1], No[i]
                        lista3[i], lista3[i + 1] = lista3[i + 1], lista3[i]

            if (len(No1)>1):
                for n in range(len(No1)-1, 0, -1):
                    for i in range(n):
                      if No1[i] > No1[i + 1]:
                        # swapping data if the element is less than next element in the array
                        No1[i], No1[i + 1] = No1[i + 1], No1[i]
                        lista4[i], lista4[i + 1] = lista4[i + 1], lista4[i]

            no=0
            if(len(lista2) > len(lista)):
                f.write("linia(-e), które zostały dodane i może zmienione w nowym kodzie: \n");
            else:
                f.write("linia(-e), które zostały usuniete i może zmienione w nowym kodzie: \n");
            if No:
                for line in lista3:
                    line = str(line)
                    f.write("linia ");
                    f.write(str(No[no])); no+=1;
                    f.write(":\t\t");
                    f.write(line);
                    f.write("\n");

            f.write("\n")
            no=0
            if(len(lista) > len(lista2)):
                f.write("linia(-e), które zostały usuniete i może zmienione w starym kodzie: \n");
            else:
                f.write("linia(-e), które zostały dodane i może zmienione w starym kodzie: \n");
            if No:
                for line in lista4:
                    line = str(line)
                    f.write("linia ");
                    f.write(str(No1[no])); no+=1;
                    f.write(":\t\t");
                    f.write(line);
                    f.write("\n");



        list.close()
        list2.close()
        f.close()
        return (result)

# ~ I am thinking about giving here only path to the right folder and in function specify the files to compare ~

# file_no1 = "/home/kali/Desktop/sus-changes-on-webpage-script-main/logs/6. Find Lines (Try nr 2)/15_01_2022/HTML.txt"
# file_no2 = "/home/kali/Desktop/sus-changes-on-webpage-script-main/logs/6. Find Lines (Try nr 2)/15_01_2022_10_47_18/HTML.txt"

# checkHTML(file_no1, file_no2)

# checkHTML()
