from datetime import datetime
import os

def zapis(a, typ):
    #jeśli nie istnieje ścieżka do logów to stwórz. Powinno tylko za pierwszym razem wystąpić
    if (os.path.isdir("logs")==False):
        os.mkdir("logs")
    
    #pobranie aktualnej daty i czasu
    now = datetime.now()
    
    #zmiana daty na string
    now = now.strftime("%d_%m_%Y")#_%H:%M:%S)
    #print(now)

    #wyświetlenie aktualnej lokalizacji
    sciezka=os.getcwd();
    #print(sciezka)

    #sprawdzenie czy istnieje lokalizacja logs, jeśli nie udało się utworzyć to powinno stworzyć raz jeszcze
    if os.path.isdir("logs"):
        os.chdir("logs")
        #x = len(list(os.listdir()))+1
        #f = open("%d.txt" % x, "a", -1, "utf-8")
        if(typ == 'html'):
            f = open(now+"_"+typ+".txt", "a", -1, "utf-8")
            for i in range(0, len(a)):
                if (type(a[i])!= str):
                    a[i] = str(a[i])
                f.write(a[i])
                f.write("\n")
            f.close()
        elif(typ == 'js'):
            f = open(now+"_"+typ+".txt", "a", -1, "utf-8")
            for i in range(0, len(a)):
                if (type(a[i])!= str):
                    a[i] = str(a[i])
                f.write(a[i])
                f.write("\n")
            f.close()
        elif(typ=='hash'):
            f = open(now+"_"+typ+".txt", "a", -1, "utf-8")
            for i in range(0, len(a)):
                if (type(a[i])!= str):
                    a[i] = str(a[i])
                f.write(a[i])
                f.write("\n")
            f.close()
        else:
            print("nie wybrano typu zmiennej do zapisania");
    else:
        if(typ == 'html'):
            f = open(now+"_"+typ+".txt", "a", -1, "utf-8")
            for i in range(0, len(a)):
                if (type(a[i])!= str):
                    a[i] = str(a[i])
                f.write(a[i])
                f.write("\n")
            f.close()
        elif(typ == 'js'):
            f = open(now+"_"+typ+".txt", "a", -1, "utf-8")
            for i in range(0, len(a)):
                if (type(a[i])!= str):
                    a[i] = str(a[i])
                f.write(a[i])
                f.write("\n")
            f.close()
        elif(typ=='hash'):
            f = open(now+"_"+typ+".txt", "a", -1, "utf-8")
            for i in range(0, len(a)):
                if (type(a[i])!= str):
                    a[i] = str(a[i])
                f.write(a[i])
                f.write("\n")
            f.close()
        else:
            print("nie wybrano typu zmiennej do zapisania");





a=['dane', 88203, "inne dane"]

zapis(a, 'zdj');


#funkcja przyjmuje pojedyńcze elementy mogące być też tablicą jedno wymiarową do zapisu
#tworzy folder 'logs' a w nim plik z aktualną datą do którego zapisuje dane
#każda dana w osobnej linii
#żeby zapisać dane w odpowiednim folderze należy do środka funkcji dopisać odpowiednio "hash", "html" lub "js"
