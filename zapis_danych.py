from datetime import datetime
import os

def zapis(a):
    if (os.path.isdir("logs")==False):
        os.mkdir("logs")
    
    #pobranie aktualnej daty i czasu
    now = datetime.now()
    
    #zmiana na string
    now = now.strftime("%d_%m_%Y")#_%H:%M:%S)
    #print(now)

    #wyświetlenie aktualnej lokalizacji
    sciezka=os.getcwd();
    #print(sciezka)

    #tworzenie folderu jeśli nie istnieje
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





a=['dane', 88203, "inne dane"]
zapis(a);
