from datetime import datetime
import os
from PathFinder import PathFinder

def zapis(a, typ, h=24):
    #jeśli nie istnieje ścieżka do logów to stwórz. Powinno tylko za pierwszym razem wystąpić
    path = PathFinder()
    pathlog = path + '/logs'
    #print(path)
    if (os.path.isdir(pathlog)==False):
        os.mkdir(pathlog)

    a = path + a
    f1 = open(a, 'r')
    fr = f1.readlines()
    f1.close()

    f1 = []

    for line in fr:
        f1.append(line.strip())
    #pobranie aktualnej daty i czasu
    now = datetime.now()

    #zmiana daty na string
    if(h==24):
        now = now.strftime("%d_%m_%Y")#_%H:%M:%S)
    else:
        now = now.strftime("%d_%m_%Y_%H")#%M:%S)
    #print(now)

    newdir = path + 'logs/' + now;


    #wyświetlenie aktualnej lokalizacji
    #print(os.getcwd())

    #sprawdzenie czy istnieje lokalizacja logs, jeśli nie udało się utworzyć to powinno stworzyć raz jeszcze
    if os.path.isdir(newdir):
        os.chdir(newdir)
        if(typ == 'HTML'):
            f = open(typ+".txt", "w", -1, "utf-8")
            for i in range(0, len(f1)):
                if (type(f1[i])!= str):
                    f1[i] = str(f1[i])
                f.write(f1[i])
                f.write("\n")
        elif(typ == 'JS'):
            #print(os.getcwd())
            f = open(typ+".txt", "w", -1, "utf-8")
            for i in range(0, len(f1)):
                if (type(f1[i])!= str):
                    f1[i] = str(f1[i])
                f.write(f1[i])
                f.write("\n")
        elif(typ=='hash'):
            f = open(typ+".txt", "w", -1, "utf-8")
            for i in range(0, len(f1)):
                if (type(f1[i])!= str):
                    f1[i] = str(f1[i])
                f.write(f1[i])
                f.write("\n")
        elif(typ=='dJS'):
            f = open(typ+".txt", "w", -1, "utf-8")
            for i in range(0, len(f1)):
                if (type(f1[i])!= str):
                    f1[i] = str(f1[i])
                f.write(f1[i])
                f.write("\n")
        elif(typ=='dHTML'):
            f = open(typ+".txt", "w", -1, "utf-8")
            for i in range(0, len(f1)):
                if (type(f1[i])!= str):
                    f1[i] = str(f1[i])
                f.write(f1[i])
                f.write("\n")
        else:
            print("nie wybrano typu zmiennej do zapisania");
    else:
        os.mkdir(newdir)
        os.chdir(newdir)
        if(typ == 'HTML'):
            f = open(typ+".txt", "w", -1, "utf-8")
            for i in range(0, len(f1)):
                if (type(f1[i])!= str):
                    f1[i] = str(f1[i])
                f.write(f1[i])
                f.write("\n")
        elif(typ == 'JS'):
            #print(os.getcwd())
            f = open(typ+".txt", "w", -1, "utf-8")
            for i in range(0, len(f1)):
                if (type(f1[i])!= str):
                    f1[i] = str(f1[i])
                f.write(f1[i])
                f.write("\n")
        elif(typ=='hash'):
            f = open(typ+".txt", "w", -1, "utf-8")
            for i in range(0, len(f1)):
                if (type(f1[i])!= str):
                    f1[i] = str(f1[i])
                f.write(f1[i])
                f.write("\n")
        elif(typ=='dJS'):
            f = open(typ+".txt", "w", -1, "utf-8")
            for i in range(0, len(f1)):
                if (type(f1[i])!= str):
                    f1[i] = str(f1[i])
                f.write(f1[i])
                f.write("\n")
        elif(typ=='dHTML'):
            f = open(typ+".txt", "w", -1, "utf-8")
            for i in range(0, len(f1)):
                if (type(f1[i])!= str):
                    f1[i] = str(f1[i])
                f.write(f1[i])
                f.write("\n")
        else:
            print("nie wybrano typu zmiennej do zapisania");
    os.chdir(path)
    f.close()



#a=['dane', 88203, "inne dane"]

#zapis("diffJS.txt", 'JS');


#funkcja przyjmuje pojedyńcze elementy mogące być też tablicą jedno wymiarową do zapisu
#tworzy folder 'logs' a w nim plik z aktualną datą do którego zapisuje dane
#każda dana w osobnej linii
#żeby zapisać dane w odpowiednim folderze należy do środka funkcji dopisać odpowiednio "hash", "html" lub "js"
