## NOTE:
#Odnosze wrazenie ze to gowno nie robi prawidlowo porowania, niby usuwa ale nie usuwa znakow bialych
#po za tym to wydaje sie wszystko prawidlowo dzialac
#
#
#

import time
import os
from PathFinder import directory
from reqFusionScrap import FusionScrap
from bubble import checkHTML
from porownanie_hashy import porownanie
from zapis_danych import zapis
from info import email, info

#url = input("Podaj pelny url strony: ") #
url = "https://www.paniswojegoczasu.pl/blog/"

#podaj email na ktorego beda szly powiadomienia
#mail = input("Podaj swoj mail: ")
mail = ''

#podaj haslo do maila
#password = input("Podaj haslo do maila: ")
password = ''

print("Co jaki czas chcesz aby sprawdzac zmiany na stronie?\n")
#d = int(input("Podaj ilosc dni: "))
d=0
#h = int(input("Podaj ilosc godzin(jesli podasz wiecej niz 24 zostana one dodane do ilosci dni): "))
h=0.0042
#if(h<1):
#    exit()
#elif(d<0):
#    exit()
#elif(h>24):
#    x = int(h/24)
#    d += x
#    h = h - (24 * x)

if d==0:
    tim = 3600 * h
else:
    tim = 3600 * h + d * 24 * 3600

#w main tylko operowa lokazacja plikow
#pierwsze wykonanie

FusionScrap(url)
zapis("outputHTML.txt", "HTML"); #kod HTML
zapis("outputJS.txt", "JS");#hashe JS
zapis("hash.txt", "hash");#

os.remove('outputHTML.txt')
os.remove('outputJS.txt')
os.remove('hash.txt')

#sound
duration = 0.5  # seconds
freq = 600  # Hz
os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))


time.sleep(tim);

#h=4
while(True):
    log = directory() #aktualna pozycja najnowszego pliku w /home/kali/Desktop/projekt/logs/17_12_2021/
    pliki = [] #outputHTML.txt, outputJS.txt
    pliki.clear();
    pliki = FusionScrap(url) #lokalizacje plikow tymczasowych

    if (checkHTML(log+"HTML.txt", pliki[0]) == False): # diffHTML.txt jesli html sa rozne to sprawdzaj dalej -> sprawdz hashe
        porownanie(log+"hash.txt", "hash.txt") #diffJS.txt
        zapis("outputHTML.txt", "HTML", h); #kod HTML
        zapis("outputJS.txt", "JS", h);#hashe JS
        zapis("hash.txt", "hash", h);#
        zapis("diffHTML.txt", "dHTML", h);#info o HTML
        zapis("diffJS.txt", "dJS", h);#info o JS

        info('diffHTML.txt')
        info('diffJS.txt')
        print("\n=========================================================\n\n")
        if (mail!=''):
            email('diffHTML.txt','diffJS.txt', mail, password)

        os.remove('outputHTML.txt')
        os.remove('outputJS.txt')
        os.remove('diffHTML.txt')
        os.remove('diffJS.txt')
        os.remove('hash.txt')

    else:
        print("Nie nastąpiła zmiana w kodzie strony!")#info do admina na widok "brak zmian na stronie" albo zeby program byl cicho

    #sound
    os.system('play -nq -t alsa synth {} sine {}'.format(duration,freq))
    
    time.sleep(tim);
