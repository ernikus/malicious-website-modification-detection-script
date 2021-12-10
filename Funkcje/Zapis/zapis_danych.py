from datetime import datetime
import os

def zapis(a):
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
        f = open(now+".txt", "a", -1, "utf-8")
        for i in range(0, len(a)):
            if (type(a[i])!= str):
                a[i] = str(a[i])
            f.write(a[i])
            f.write("\n")
        f.close()
    else:
        os.mkdir("logs")
        os.chdir("logs")
        f = open(now+".txt", "a", -1, "utf-8")
        for i in range(0, len(a)):
            if (type(a[i])!= str):
                a[i] = str(a[i])
            f.write(a[i])
            f.write("\n")
        f.close()


a=['dane', 88203, "inne dane"]
zapis(a);


#funkcja przyjmuje pojedyńcze elementy mogące być też tablicą jedno wymiarową do zapisu
#tworzy folder 'logs' a w nim plik z aktualną datą do którego zapisuje dane
#każda dana w osobnej linii
